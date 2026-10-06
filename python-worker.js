const PYODIDE_BASE =
  'https://cdn.jsdelivr.net/pyodide/v314.0.7/full/';

let sharedBuffer;
let control;
let textBuffer;
let pyodide;


// ------------------------------------------------------------
// LOAD PYODIDE
// ------------------------------------------------------------

async function initializePyodide() {
  if (pyodide) {
    return pyodide;
  }

  const module = await import(
    `${PYODIDE_BASE}pyodide.mjs`
  );

  pyodide = await module.loadPyodide({
    indexURL: PYODIDE_BASE
  });

  return pyodide;
}


// ------------------------------------------------------------
// READ PLAYER INPUT FROM THE WEBSITE TERMINAL
// ------------------------------------------------------------

function readTerminalInput(promptText = '') {

  // Reset input state
  Atomics.store(control, 0, 0);
  Atomics.store(control, 1, 0);

  // Tell runner.js that Python is waiting for input
  self.postMessage({
    type: 'input',
    prompt: String(promptText)
  });

  // Pause the worker until the player submits an answer
  Atomics.wait(
    control,
    0,
    0
  );

  const length = Atomics.load(
    control,
    1
  );

  let result = '';

  const chunkSize = 4096;

  for (
    let start = 0;
    start < length;
    start += chunkSize
  ) {

    const chunk = textBuffer.subarray(
      start,
      Math.min(
        start + chunkSize,
        length
      )
    );

    result += String.fromCharCode(
      ...chunk
    );
  }

  return result;
}


// ------------------------------------------------------------
// RECEIVE GAME CODE FROM runner.js
// ------------------------------------------------------------

self.onmessage = async event => {

  if (event.data.type !== 'run') {
    return;
  }

  sharedBuffer =
    event.data.sharedBuffer;

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

  try {

    // --------------------------------------------------------
    // START PYTHON
    // --------------------------------------------------------

    await initializePyodide();


    // --------------------------------------------------------
    // RAW PYTHON OUTPUT
    //
    // Important:
    // using RAW output lets the browser terminal correctly
    // handle \r carriage returns used by loading bars,
    // animations, blinking text, etc.
    // --------------------------------------------------------

    pyodide.setStdout({

      raw: byte => {

        self.postMessage({
          type: 'stdout-byte',
          byte
        });

      }

    });


    // --------------------------------------------------------
    // PYTHON ERROR OUTPUT
    // --------------------------------------------------------

    pyodide.setStderr({

      batched: text => {

        self.postMessage({
          type: 'stderr',
          text
        });

      }

    });


    // --------------------------------------------------------
    // CONNECT JAVASCRIPT INPUT TO PYTHON
    // --------------------------------------------------------

    pyodide.globals.set(
      'terminal_input',
      readTerminalInput
    );


    // Tell the website Python is ready
    self.postMessage({
      type: 'ready'
    });


    // --------------------------------------------------------
    // REPLACE PYTHON'S NORMAL input()
    // --------------------------------------------------------

    const wrappedCode = `
import builtins

def _browser_input(prompt=''):
    return str(
        terminal_input(
            str(prompt)
        )
    )

builtins.input = _browser_input


${event.data.code}
`;


    // --------------------------------------------------------
    // RUN STUDENT GAME
    // --------------------------------------------------------

    try {

      await pyodide.runPythonAsync(
        wrappedCode
      );


      self.postMessage({
        type: 'done'
      });


    } catch (error) {

      const errorText =
        error &&
        error.message
          ? error.message
          : String(error);


      // ------------------------------------------------------
      // HANDLE exit() / quit()
      //
      // Students often use exit() to end their games.
      // Pyodide treats that internally as SystemExit.
      //
      // We want it to count as a normal game ending.
      // ------------------------------------------------------

      if (
        errorText.includes(
          'SystemExit'
        )
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
        error &&
        error.message
          ? error.message
          : String(error)

    });

  }

};
