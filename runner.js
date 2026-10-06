const output = document.getElementById('terminal-output');
const form = document.getElementById('terminal-form');
const input = document.getElementById('terminal-input');
const sendButton = form.querySelector('button');
const restartButton = document.getElementById('restart-button');
const statusText = document.getElementById('status-text');
const gameTitle = document.getElementById('game-title');

let worker = null;
let sharedBuffer = null;
let control = null;
let textBuffer = null;
let currentGame = null;
let waitingForInput = false;

// Terminal rendering state
let terminalCurrentLine = null;
let terminalCurrentSpan = null;
let currentAnsiClass = '';
let ansiBuffer = '';
let readingAnsi = false;
let utf8Decoder = new TextDecoder('utf-8');

const params = new URLSearchParams(location.search);
const requestedGameId = Number(params.get('game') || 1);

boot();

async function boot() {
  setInputEnabled(false);
  restartButton.disabled = true;

  if (
    !window.crossOriginIsolated ||
    typeof SharedArrayBuffer === 'undefined'
  ) {
    writeLine(
      'SYSTEM ERROR: This site is not cross-origin isolated.',
      'error'
    );

    writeLine(
      'Deploy with the included vercel.json file so the embedded terminal can pause Python while waiting for player input.',
      'error'
    );

    statusText.textContent = 'TERMINAL CONFIGURATION ERROR';

    return;
  }

  try {
    const gamesResponse = await fetch(
      'games.json',
      { cache: 'no-store' }
    );

    const games = await gamesResponse.json();

    currentGame =
      games.find(game => game.id === requestedGameId) ||
      games[0];

    gameTitle.textContent = currentGame.title;

    document.title =
      `${currentGame.title} | ASCII Games Hub`;

    restartButton.disabled = false;

    await startGame();

  } catch (error) {
    writeLine(
      `SYSTEM ERROR: ${error.message}`,
      'error'
    );

    statusText.textContent = 'FAILED TO LOAD GAME';
  }
}

async function startGame() {
  if (worker) {
    worker.terminate();
  }

  output.innerHTML = '';

  resetTerminalState();

  waitingForInput = false;
  setInputEnabled(false);

  statusText.textContent = 'LOADING GAME...';

  writeLine(
    '> INITIALIZING PYTHON...',
    'system'
  );

  const gameResponse = await fetch(
    currentGame.file,
    { cache: 'no-store' }
  );

  if (!gameResponse.ok) {
    throw new Error(
      `Could not load ${currentGame.file}`
    );
  }

  const code = await gameResponse.text();

  sharedBuffer =
    new SharedArrayBuffer(65536);

  control =
    new Int32Array(
      sharedBuffer,
      0,
      2
    );

  textBuffer =
    new Uint16Array(
      sharedBuffer,
      8
    );

  worker = new Worker(
    'python-worker.js',
    { type: 'module' }
  );

  worker.onmessage = handleWorkerMessage;

  worker.onerror = event => {
    writeLine(
      `WORKER ERROR: ${event.message}`,
      'error'
    );

    statusText.textContent = 'GAME STOPPED';

    setInputEnabled(false);
  };

  worker.postMessage({
    type: 'run',
    code,
    sharedBuffer
  });
}

function handleWorkerMessage(event) {
  const message = event.data;

  // -----------------------------
  // PYTHON READY
  // -----------------------------

  if (message.type === 'ready') {
    statusText.textContent = 'RUNNING';

    writeLine(
      '> PYTHON READY. STARTING GAME...',
      'system'
    );

    writeLine('');

    return;
  }

  // -----------------------------
  // RAW PYTHON OUTPUT
  // -----------------------------

  if (message.type === 'stdout-byte') {
    handleTerminalByte(message.byte);
    return;
  }

  // -----------------------------
  // FALLBACK STDOUT
  // -----------------------------

  if (message.type === 'stdout') {
    writeText(message.text);
    return;
  }

  // -----------------------------
  // STDERR
  // -----------------------------

  if (message.type === 'stderr') {
    writeLine(
      message.text,
      'error'
    );

    return;
  }

  // -----------------------------
  // PYTHON input()
  // -----------------------------

  if (message.type === 'input') {

    if (message.prompt) {
      writeText(message.prompt);
    }

    waitingForInput = true;

    statusText.textContent =
      'WAITING FOR PLAYER';

    setInputEnabled(true);

    input.focus();

    return;
  }

  // -----------------------------
  // GAME COMPLETE
  // -----------------------------

  if (message.type === 'done') {
    waitingForInput = false;

    setInputEnabled(false);

    statusText.textContent =
      'GAME COMPLETE';

    terminalCurrentLine = null;
    terminalCurrentSpan = null;

    writeLine('');

    writeLine(
      '[ GAME FINISHED — PRESS RESTART TO PLAY AGAIN ]',
      'system'
    );

    return;
  }

  // -----------------------------
  // PYTHON ERROR
  // -----------------------------

  if (message.type === 'error') {
    waitingForInput = false;

    setInputEnabled(false);

    statusText.textContent =
      'PYTHON ERROR';

    terminalCurrentLine = null;
    terminalCurrentSpan = null;

    writeLine('');

    writeLine(
      message.error,
      'error'
    );
  }
}


// --------------------------------------------------
// PLAYER INPUT
// --------------------------------------------------

form.addEventListener(
  'submit',
  event => {

    event.preventDefault();

    if (!waitingForInput) {
      return;
    }

    const answer = input.value;

    terminalCurrentLine = null;
    terminalCurrentSpan = null;

    writeLine(
      `> ${answer}`,
      'user'
    );

    input.value = '';

    waitingForInput = false;

    setInputEnabled(false);

    statusText.textContent = 'RUNNING';

    const safeAnswer =
      answer.slice(
        0,
        textBuffer.length
      );

    for (
      let i = 0;
      i < safeAnswer.length;
      i++
    ) {
      textBuffer[i] =
        safeAnswer.charCodeAt(i);
    }

    Atomics.store(
      control,
      1,
      safeAnswer.length
    );

    Atomics.store(
      control,
      0,
      1
    );

    Atomics.notify(
      control,
      0,
      1
    );
  }
);


// --------------------------------------------------
// RESTART
// --------------------------------------------------

restartButton.addEventListener(
  'click',
  () => {

    startGame().catch(
      error => {

        writeLine(
          `SYSTEM ERROR: ${error.message}`,
          'error'
        );

      }
    );

  }
);


// --------------------------------------------------
// ENABLE / DISABLE INPUT
// --------------------------------------------------

function setInputEnabled(enabled) {
  input.disabled = !enabled;
  sendButton.disabled = !enabled;
}


// --------------------------------------------------
// RESET TERMINAL STATE
// --------------------------------------------------

function resetTerminalState() {
  terminalCurrentLine = null;
  terminalCurrentSpan = null;

  currentAnsiClass = '';

  ansiBuffer = '';
  readingAnsi = false;

  utf8Decoder =
    new TextDecoder('utf-8');
}


// --------------------------------------------------
// WRITE NORMAL COMPLETE LINE
// --------------------------------------------------

function writeLine(
  text = '',
  className = ''
) {
  terminalCurrentLine = null;
  terminalCurrentSpan = null;

  const line =
    document.createElement('div');

  line.className =
    `terminal-line ${className}`.trim();

  line.textContent = text;

  output.appendChild(line);

  output.scrollTop =
    output.scrollHeight;
}


// --------------------------------------------------
// WRITE NORMAL TEXT
// --------------------------------------------------

function writeText(text = '') {
  for (const character of String(text)) {
    handleTerminalCharacter(character);
  }
}


// --------------------------------------------------
// GET CURRENT TERMINAL LINE
// --------------------------------------------------

function getCurrentTerminalLine() {
  if (!terminalCurrentLine) {
    terminalCurrentLine =
      document.createElement('div');

    terminalCurrentLine.className =
      'terminal-line';

    output.appendChild(
      terminalCurrentLine
    );

    terminalCurrentSpan = null;
  }

  return terminalCurrentLine;
}


// --------------------------------------------------
// GET CURRENT COLORED SPAN
// --------------------------------------------------

function getCurrentTerminalSpan() {
  const line =
    getCurrentTerminalLine();

  if (
    !terminalCurrentSpan ||
    terminalCurrentSpan.dataset.ansiClass !== currentAnsiClass
  ) {
    terminalCurrentSpan =
      document.createElement('span');

    terminalCurrentSpan.dataset.ansiClass =
      currentAnsiClass;

    if (currentAnsiClass) {
      terminalCurrentSpan.className =
        currentAnsiClass;
    }

    line.appendChild(
      terminalCurrentSpan
    );
  }

  return terminalCurrentSpan;
}


// --------------------------------------------------
// RAW BYTE FROM PYTHON
// --------------------------------------------------

function handleTerminalByte(byte) {
  const decoded =
    utf8Decoder.decode(
      new Uint8Array([byte]),
      { stream: true }
    );

  if (!decoded) {
    return;
  }

  for (const character of decoded) {
    handleTerminalCharacter(character);
  }
}


// --------------------------------------------------
// HANDLE TERMINAL CHARACTER
// --------------------------------------------------

function handleTerminalCharacter(character) {

  // -----------------------------
  // Currently reading an ANSI code
  // -----------------------------

  if (readingAnsi) {
    ansiBuffer += character;

    // ANSI color commands normally end with "m"
    if (character === 'm') {
      applyAnsiCode(ansiBuffer);

      ansiBuffer = '';
      readingAnsi = false;
    }

    // Avoid broken / endless ANSI sequences
    else if (ansiBuffer.length > 30) {
      ansiBuffer = '';
      readingAnsi = false;
    }

    return;
  }


  // -----------------------------
  // ESCAPE character starts ANSI
  // -----------------------------

  if (character === '\x1b') {
    readingAnsi = true;
    ansiBuffer = '';

    return;
  }


  // -----------------------------
  // NEWLINE
  // -----------------------------

  if (character === '\n') {
    terminalCurrentLine = null;
    terminalCurrentSpan = null;

    output.scrollTop =
      output.scrollHeight;

    return;
  }


  // -----------------------------
  // CARRIAGE RETURN
  // -----------------------------

  if (character === '\r') {
    const line =
      getCurrentTerminalLine();

    line.innerHTML = '';

    terminalCurrentSpan = null;

    output.scrollTop =
      output.scrollHeight;

    return;
  }


  // -----------------------------
  // NORMAL CHARACTER
  // -----------------------------

  const span =
    getCurrentTerminalSpan();

  span.textContent += character;

  output.scrollTop =
    output.scrollHeight;
}


// --------------------------------------------------
// ANSI COLOR HANDLER
//
// Handles Python codes like:
//
// \033[31m = red
// \033[32m = green
// \033[33m = yellow
// \033[34m = blue
// \033[0m  = reset
// --------------------------------------------------

function applyAnsiCode(sequence) {

  // Sequence looks like:
  // [31m
  // [0m
  // [1;31m

  const match =
    sequence.match(
      /^\[([0-9;]*)m$/
    );

  if (!match) {
    return;
  }

  const codes =
    match[1] === ''
      ? [0]
      : match[1]
          .split(';')
          .map(Number);


  for (const code of codes) {

    switch (code) {

      // RESET
      case 0:
        currentAnsiClass = '';
        break;


      // NORMAL COLORS

      case 30:
        currentAnsiClass =
          'ansi-black';
        break;

      case 31:
        currentAnsiClass =
          'ansi-red';
        break;

      case 32:
        currentAnsiClass =
          'ansi-green';
        break;

      case 33:
        currentAnsiClass =
          'ansi-yellow';
        break;

      case 34:
        currentAnsiClass =
          'ansi-blue';
        break;

      case 35:
        currentAnsiClass =
          'ansi-magenta';
        break;

      case 36:
        currentAnsiClass =
          'ansi-cyan';
        break;

      case 37:
        currentAnsiClass =
          'ansi-white';
        break;


      // BRIGHT COLORS

      case 90:
        currentAnsiClass =
          'ansi-bright-black';
        break;

      case 91:
        currentAnsiClass =
          'ansi-bright-red';
        break;

      case 92:
        currentAnsiClass =
          'ansi-bright-green';
        break;

      case 93:
        currentAnsiClass =
          'ansi-bright-yellow';
        break;

      case 94:
        currentAnsiClass =
          'ansi-bright-blue';
        break;

      case 95:
        currentAnsiClass =
          'ansi-bright-magenta';
        break;

      case 96:
        currentAnsiClass =
          'ansi-bright-cyan';
        break;

      case 97:
        currentAnsiClass =
          'ansi-bright-white';
        break;
    }
  }

  // Force a fresh span after a color change
  terminalCurrentSpan = null;
}
