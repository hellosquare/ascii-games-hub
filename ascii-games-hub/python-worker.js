const PYODIDE_VERSION = '314.0.7';
const PYODIDE_BASE = `https://cdn.jsdelivr.net/pyodide/v${PYODIDE_VERSION}/full/`;

let sharedBuffer;
let control;
let textBuffer;
let pyodide;

function readTerminalInput(promptText = '') {
  Atomics.store(control, 0, 0);
  Atomics.store(control, 1, 0);
  self.postMessage({ type: 'input', prompt: String(promptText) });

  // The worker can block here without freezing the webpage.
  Atomics.wait(control, 0, 0);

  const length = Atomics.load(control, 1);
  let result = '';
  const chunkSize = 4096;
  for (let start = 0; start < length; start += chunkSize) {
    const chunk = textBuffer.subarray(start, Math.min(start + chunkSize, length));
    result += String.fromCharCode(...chunk);
  }
  return result;
}

self.onmessage = async event => {
  if (event.data.type !== 'run') return;

  sharedBuffer = event.data.sharedBuffer;
  control = new Int32Array(sharedBuffer, 0, 2);
  textBuffer = new Uint16Array(sharedBuffer, 8);

  try {
    if (!pyodide) {
      importScripts(`${PYODIDE_BASE}pyodide.js`);
      pyodide = await loadPyodide({ indexURL: PYODIDE_BASE });
    }

    pyodide.setStdout({ batched: text => self.postMessage({ type: 'stdout', text: `${text}\n` }) });
    pyodide.setStderr({ batched: text => self.postMessage({ type: 'stderr', text }) });
    pyodide.globals.set('terminal_input', readTerminalInput);

    self.postMessage({ type: 'ready' });

    const wrappedCode = `
import builtins

def _browser_input(prompt=''):
    return str(terminal_input(str(prompt)))

builtins.input = _browser_input

${event.data.code}
`;

    await pyodide.runPythonAsync(wrappedCode);
    self.postMessage({ type: 'done' });
  } catch (error) {
    self.postMessage({
      type: 'error',
      error: error && error.message ? error.message : String(error)
    });
  }
};
