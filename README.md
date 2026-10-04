# ASCII Games Hub

A static Vercel website for hosting 24 student-made text/ASCII Python games.

## How it works

- `index.html` is the game menu.
- `play.html` is one reusable terminal page.
- `games.json` stores game titles and Python file paths.
- `games/game01.py` through `games/game24.py` are the student games.
- `python-worker.js` loads Pyodide and runs Python in a Web Worker.
- `runner.js` connects Python `print()` and `input()` to the on-page terminal.
- `vercel.json` enables the browser isolation needed for the terminal input bridge.

Pyodide is pinned to version 314.0.7.

## Add a student's game

1. Open the matching file in `games/`, for example `games/game07.py`.
2. Delete the placeholder code.
3. Paste the student's Python program into that file.
4. Open `games.json` and rename `Game 7` to the real game title.
5. Commit and push to GitHub. Vercel will redeploy automatically if the repository is connected.

Example:

```json
{"id":7,"title":"Escape from Mars","file":"games/game07.py"}
```

## Student code that works best

This hub is designed for normal console-based Python using:

- `print()`
- `input()`
- variables
- `if / elif / else`
- `while` and `for` loops
- functions
- booleans
- `random`
- ASCII art

Browser Python cannot access a student's computer like desktop Python can. Avoid programs that depend on local files, Tkinter, Pygame desktop windows, or operating-system-specific features.

## Deploy to Vercel

1. Create a GitHub repository.
2. Upload all files and folders from this project to the repository root.
3. In Vercel, choose **Add New Project** and import the GitHub repository.
4. No framework is required. Leave the project as a static site and deploy.
5. Keep `vercel.json` in the repository root. It is required for the embedded terminal input system.

## Important local-testing note

Opening `index.html` directly from Finder/Explorer will not fully work because browsers block `fetch()` and SharedArrayBuffer features for `file://` pages. Test the deployed Vercel URL, or use a local server that sends the same isolation headers as `vercel.json`.
