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

// Used to simulate terminal-style output
let terminalCurrentLine = null;
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

    statusText.textContent =
      'TERMINAL CONFIGURATION ERROR';

    return;
  }

  try {
    const gamesResponse = await fetch(
      'games.json',
      { cache: 'no-store' }
    );

    const games = await gamesResponse.json();

    currentGame =
      games.find(
        game => game.id === requestedGameId
      ) || games[0];

    gameTitle.textContent =
      currentGame.title;

    document.title =
      `${currentGame.title} | ASCII Games Hub`;

    restartButton.disabled = false;

    await startGame();

  } catch (error) {
    writeLine(
      `SYSTEM ERROR: ${error.message}`,
      'error'
    );

    statusText.textContent =
      'FAILED TO LOAD GAME';
  }
}

async function startGame() {
  if (worker) {
    worker.terminate();
  }

  output.innerHTML = '';

  // Reset terminal output state
  terminalCurrentLine = null;
  utf8Decoder = new TextDecoder('utf-8');

  waitingForInput = false;

  setInputEnabled(false);

  statusText.textContent =
    'LOADING GAME...';

  writeLine(
    '> INITIALIZING PYTHON...',
    'system'
  );

  const gameResponse =
    await fetch(
      currentGame.file,
      { cache: 'no-store' }
    );

  if (!gameResponse.ok) {
    throw new Error(
      `Could not load ${currentGame.file}`
    );
  }

  const code =
    await gameResponse.text();

  // 2 Int32 values:
  // [0] input state
  // [1] input length
  //
  // Remaining memory stores
  // UTF-16 player input.
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

  // IMPORTANT:
  // Pyodide 314 uses an ES module worker.
  worker =
    new Worker(
      'python-worker.js',
      { type: 'module' }
    );

  worker.onmessage =
    handleWorkerMessage;

  worker.onerror =
    event => {
      writeLine(
        `WORKER ERROR: ${event.message}`,
        'error'
      );

      statusText.textContent =
        'GAME STOPPED';

      setInputEnabled(false);
    };

  worker.postMessage({
    type: 'run',
    code,
    sharedBuffer
  });
}

function handleWorkerMessage(event) {
  const message =
    event.data;

  // -----------------------------
  // PYTHON READY
  // -----------------------------

  if (message.type === 'ready') {
    statusText.textContent =
      'RUNNING';

    writeLine(
      '> PYTHON READY. STARTING GAME...',
      'system'
    );

    writeLine('');

    return;
  }

  // -----------------------------
  // RAW TERMINAL OUTPUT
  //
  // This is the important part
  // that handles \r properly.
  // -----------------------------

  if (message.type === 'stdout-byte') {
    handleTerminalByte(
      message.byte
    );

    return;
  }

  // -----------------------------
  // OLD/FALLBACK STDOUT
  //
  // Keeping this here means the
  // runner still works if stdout
  // is ever sent normally.
  // -----------------------------

  if (message.type === 'stdout') {
    writeText(
      message.text
    );

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
      writeText(
        message.prompt
      );
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

    // Finish any unfinished output line
    terminalCurrentLine = null;

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

    writeLine('');

    writeLine(
      message.error,
      'error'
    );
  }
}

// --------------------------------------------------
// PLAYER SUBMITS INPUT
// --------------------------------------------------

form.addEventListener(
  'submit',
  event => {

    event.preventDefault();

    if (!waitingForInput) {
      return;
    }

    const answer =
      input.value;

    // Make sure typed input begins
    // on its own display line.
    terminalCurrentLine = null;

    writeLine(
      `> ${answer}`,
      'user'
    );

    input.value = '';

    waitingForInput = false;

    setInputEnabled(false);

    statusText.textContent =
      'RUNNING';

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
// RESTART BUTTON
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
  input.disabled =
    !enabled;

  sendButton.disabled =
    !enabled;
}

// --------------------------------------------------
// WRITE A COMPLETE LINE
// --------------------------------------------------

function writeLine(
  text = '',
  className = ''
) {

  // Any normal writeLine call means
  // we are starting a new line.
  terminalCurrentLine = null;

  const line =
    document.createElement('div');

  line.className =
    `terminal-line ${className}`.trim();

  line.textContent =
    text;

  output.appendChild(
    line
  );

  output.scrollTop =
    output.scrollHeight;
}

// --------------------------------------------------
// WRITE NORMAL TEXT
// --------------------------------------------------

function writeText(text = '') {

  const normalized =
    String(text)
      .replace(
        /\r\n/g,
        '\n'
      );

  const parts =
    normalized.split('\n');

  parts.forEach(
    (part, index) => {

      if (
        index <
        parts.length - 1
      ) {
        writeLine(
          part
        );

      } else if (
        part !== ''
      ) {

        const line =
          getCurrentTerminalLine();

        line.textContent +=
          part;

        output.scrollTop =
          output.scrollHeight;
      }

    }
  );
}

// --------------------------------------------------
// GET OR CREATE CURRENT TERMINAL LINE
// --------------------------------------------------

function getCurrentTerminalLine() {

  if (!terminalCurrentLine) {

    terminalCurrentLine =
      document.createElement('div');

    terminalCurrentLine.className =
      'terminal-line';

    terminalCurrentLine.textContent =
      '';

    output.appendChild(
      terminalCurrentLine
    );

  }

  return terminalCurrentLine;
}

// --------------------------------------------------
// HANDLE RAW PYTHON OUTPUT BYTE
//
// This makes browser output behave
// more like a real terminal.
// --------------------------------------------------

function handleTerminalByte(byte) {

  // -----------------------------
  // NEWLINE \n
  // -----------------------------

  if (byte === 10) {

    terminalCurrentLine =
      null;

    output.scrollTop =
      output.scrollHeight;

    return;
  }

  // -----------------------------
  // CARRIAGE RETURN \r
  //
  // This is what progress bars
  // and blinking text use.
  //
  // Instead of creating a new
  // line, clear the current line
  // and rewrite it.
  // -----------------------------

  if (byte === 13) {

    const line =
      getCurrentTerminalLine();

    line.textContent =
      '';

    output.scrollTop =
      output.scrollHeight;

    return;
  }

  // -----------------------------
  // NORMAL UTF-8 CHARACTER
  // -----------------------------

  const text =
    utf8Decoder.decode(
      new Uint8Array([
        byte
      ]),
      {
        stream: true
      }
    );

  if (text) {

    const line =
      getCurrentTerminalLine();

    line.textContent +=
      text;

    output.scrollTop =
      output.scrollHeight;
  }
}
