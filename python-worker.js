const PYODIDE_BASE =
  'https://cdn.jsdelivr.net/pyodide/v314.0.7/full/';

let sharedBuffer;
let control;
let textBuffer;
let pyodide;


// ------------------------------------------------------------
// LOAD PYODIDE AS AN ES MODULE
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
// GET INPUT FROM THE WEBSITE TERMINAL
// ------------------------------------------------------------

function readTerminalInput(promptText = '') {

  // Reset shared input state
  Atomics.store(control, 0, 0);
  Atomics.store(control, 1, 0);

  // Tell runner.js we need input
  self.postMessage({
    type: 'input',
    prompt: String(promptText)
  });

  // Pause Python until the player submits an answer.
  // This is safe because we're inside a Web Worker.
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
// RECEIVE GAME FROM runner.js
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
    // SEND PRINT() OUTPUT TO THE WEBSITE
    // --------------------------------------------------------

    pyodide.setStdout({

      batched: text => {

        self.postMessage({
          type: 'stdout',
          text: `${text}\n`
        });

      }

    });


    // --------------------------------------------------------
    // SEND PYTHON ERRORS TO THE WEBSITE
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
    // CONNECT OUR HTML TERMINAL TO PYTHON input()
    // --------------------------------------------------------

    pyodide.globals.set(
      'terminal_input',
      readTerminalInput
    );


    // Python is ready!
    self.postMessage({
      type: 'ready'
    });


    // --------------------------------------------------------
    // REPLACE PYTHON input()
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
    // RUN STUDENT CODE
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
      // NORMAL GAME EXIT
      //
      // Students may use:
      //
      // exit()
      // quit()
      //
      // Python throws SystemExit internally.
      // That should NOT appear as an error to the player.
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
