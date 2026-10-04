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

const params = new URLSearchParams(location.search);
const requestedGameId = Number(params.get('game') || 1);

boot();

async function boot() {
  setInputEnabled(false);
  restartButton.disabled = true;

  if (!window.crossOriginIsolated || typeof SharedArrayBuffer === 'undefined') {
    writeLine('SYSTEM ERROR: This site is not cross-origin isolated.', 'error');
    writeLine('Deploy with the included vercel.json file so the embedded terminal can pause Python while waiting for player input.', 'error');
    statusText.textContent = 'TERMINAL CONFIGURATION ERROR';
    return;
  }

  try {
    const gamesResponse = await fetch('games.json', { cache: 'no-store' });
    const games = await gamesResponse.json();
    currentGame = games.find(game => game.id === requestedGameId) || games[0];
    gameTitle.textContent = currentGame.title;
    document.title = `${currentGame.title} | ASCII Games Hub`;
    restartButton.disabled = false;
    await startGame();
  } catch (error) {
    writeLine(`SYSTEM ERROR: ${error.message}`, 'error');
    statusText.textContent = 'FAILED TO LOAD GAME';
  }
}

async function startGame() {
  if (worker) worker.terminate();
  output.innerHTML = '';
  waitingForInput = false;
  setInputEnabled(false);
  statusText.textContent = 'LOADING GAME...';
  writeLine('> INITIALIZING PYTHON...', 'system');

  const gameResponse = await fetch(currentGame.file, { cache: 'no-store' });
  if (!gameResponse.ok) throw new Error(`Could not load ${currentGame.file}`);
  const code = await gameResponse.text();

  // 2 Int32 values (state + length), then room for 32,764 UTF-16 characters.
  sharedBuffer = new SharedArrayBuffer(65536);
  control = new Int32Array(sharedBuffer, 0, 2);
  textBuffer = new Uint16Array(sharedBuffer, 8);

  worker = new Worker('python-worker.js');
  worker.onmessage = handleWorkerMessage;
  worker.onerror = (event) => {
    writeLine(`WORKER ERROR: ${event.message}`, 'error');
    statusText.textContent = 'GAME STOPPED';
    setInputEnabled(false);
  };

  worker.postMessage({ type: 'run', code, sharedBuffer });
}

function handleWorkerMessage(event) {
  const message = event.data;

  if (message.type === 'ready') {
    statusText.textContent = 'RUNNING';
    writeLine('> PYTHON READY. STARTING GAME...', 'system');
    writeLine('');
    return;
  }

  if (message.type === 'stdout') {
    writeText(message.text);
    return;
  }

  if (message.type === 'stderr') {
    writeLine(message.text, 'error');
    return;
  }

  if (message.type === 'input') {
    if (message.prompt) writeText(message.prompt);
    waitingForInput = true;
    statusText.textContent = 'WAITING FOR PLAYER';
    setInputEnabled(true);
    input.focus();
    return;
  }

  if (message.type === 'done') {
    waitingForInput = false;
    setInputEnabled(false);
    statusText.textContent = 'GAME COMPLETE';
    writeLine('');
    writeLine('[ GAME FINISHED — PRESS RESTART TO PLAY AGAIN ]', 'system');
    return;
  }

  if (message.type === 'error') {
    waitingForInput = false;
    setInputEnabled(false);
    statusText.textContent = 'PYTHON ERROR';
    writeLine('');
    writeLine(message.error, 'error');
  }
}

form.addEventListener('submit', event => {
  event.preventDefault();
  if (!waitingForInput) return;

  const answer = input.value;
  writeLine(`> ${answer}`, 'user');
  input.value = '';
  waitingForInput = false;
  setInputEnabled(false);
  statusText.textContent = 'RUNNING';

  const safeAnswer = answer.slice(0, textBuffer.length);
  for (let i = 0; i < safeAnswer.length; i++) {
    textBuffer[i] = safeAnswer.charCodeAt(i);
  }
  Atomics.store(control, 1, safeAnswer.length);
  Atomics.store(control, 0, 1);
  Atomics.notify(control, 0, 1);
});

restartButton.addEventListener('click', () => startGame().catch(error => {
  writeLine(`SYSTEM ERROR: ${error.message}`, 'error');
}));

function setInputEnabled(enabled) {
  input.disabled = !enabled;
  sendButton.disabled = !enabled;
}

function writeLine(text = '', className = '') {
  const line = document.createElement('div');
  line.className = `terminal-line ${className}`.trim();
  line.textContent = text;
  output.appendChild(line);
  output.scrollTop = output.scrollHeight;
}

function writeText(text = '') {
  // Keep student ASCII art intact while allowing output that does not end in a newline.
  const normalized = String(text).replace(/\r\n/g, '\n');
  const parts = normalized.split('\n');
  parts.forEach((part, index) => {
    if (index < parts.length - 1) {
      writeLine(part);
    } else if (part !== '') {
      const line = document.createElement('div');
      line.className = 'terminal-line';
      line.textContent = part;
      output.appendChild(line);
      output.scrollTop = output.scrollHeight;
    }
  });
}
