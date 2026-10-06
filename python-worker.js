const PYODIDE_VERSION = '314.0.7';

const PYODIDE_SOURCES = [
  {
    script: `https://cdn.jsdelivr.net/pyodide/v${PYODIDE_VERSION}/full/pyodide.js`,
    base: `https://cdn.jsdelivr.net/pyodide/v${PYODIDE_VERSION}/full/`
  },
  {
    script: `https://cdn.jsdelivr.net/npm/pyodide@${PYODIDE_VERSION}/pyodide.js`,
    base: `https://cdn.jsdelivr.net/npm/pyodide@${PYODIDE_VERSION}/`
  }
];

let sharedBuffer;
let control;
let textBuffer;
let pyodide;

// --------------------------------------------------
// LOAD PYODIDE WITH FALLBACK
// --------------------------------------------------

async function initializePyodide() {
  if (pyodide) return pyodide;

  let lastError = null;

  for (const source of PYODIDE_SOURCES) {
    try {
      importScripts(source.script);

      pyodide = await loadPyodide({
        indexURL: source.base
      });

      return pyodide;
    } catch (error) {
      lastError = error;
    }
  }

  throw new Error(
    `Could not load Pyodide from any CDN.\n\n${String(lastError)}`
  );
}


// --------------------------------------------------
// READ INPUT FROM THE HTML TERMINAL
// --------------------------------------------------

function readTerminalInput(promptText = '') {
  Atomics.store(control, 0, 0);
  Atomics.store(control, 1, 0);

  self.postMessage({
    type: 'input',
    prompt: String(promptText)
  });

  // Worker pauses here until runner.js wakes it up.
  Atomics.wait(control, 0, 0);

  const length = Atomics.load(control, 1);

  let result = '';
  const chunkSize = 4096;

  for (let start = 0; start < length; start += chunkSize) {
    const chunk = textBuffer.subarray(
      start,
      Math.min(start + chunkSize, length)
    );

    result += String.fromCharCode(...chunk);
  }

  return result;
}


// --------------------------------------------------
// RUN STUDENT GAME
// --------------------------------------------------

self.onmessage = async event => {
  if (event.data.type !== 'run') return;

  sharedBuffer = event.data.sharedBuffer;
  control = new Int32Array(sharedBuffer, 0, 2);
  textBuffer = new Uint16Array(sharedBuffer, 8);

  try {
    await initializePyodide();

    // Send normal Python output to the terminal.
    pyodide.setStdout({
      batched: text => {
        self.postMessage({
          type: 'stdout',
          text: `${text}\n`
        });
      }
    });

    // Send Python errors/warnings to the terminal.
    pyodide.setStderr({
      batched: text => {
        self.postMessage({
          type: 'stderr',
          text
        });
      }
    });

    // Make our JavaScript terminal-input function available in Python.
    pyodide.globals.set(
      'terminal_input',
      readTerminalInput
    );

    self.postMessage({
      type: 'ready'
    });


    // --------------------------------------------------
    // CUSTOM input()
    //
    // Replace Python's normal input() with our website
    // terminal version.
    // --------------------------------------------------

    const wrappedCode = `
import builtins

def _browser_input(prompt=''):
    return str(terminal_input(str(prompt)))

builtins.input = _browser_input

${event.data.code}
`;

    try {
      await pyodide.runPythonAsync(wrappedCode);

      self.postMessage({
        type: 'done'
      });

    } catch (error) {
      const errorText =
        error && error.message
          ? error.message
          : String(error);

      // Students use exit() and quit() to end games.
      // Pyodide reports that as SystemExit.
      // Treat it as a normal game ending.
      if (
        errorText.includes('SystemExit')
      ) {
        self.postMessage({
          type: 'done'
        });

        return;
      }

      throw error;
    }

  } catch (error) {
    self.postMessage({
      type: 'error',
      error:
        error && error.message
          ? error.message
          : String(error)
    });
  }
};
