Repository quick notes (high-signal)

- Target project: viikko3/login — this is the interactive web app with Robot tests. Most debugging, runs and tests target that folder.

- uv-managed Python environment: viikko3/login is pinned with uv (`.python-version`, `uv.lock`). Always run Python commands through uv from inside `viikko3/login` so the correct interpreter and deps are used.
  - Start the app (required to be running while tests execute):
    uv run python3 src/index.py
  - Run Robot tests (app must be running):
    uv run robot src/tests

- Tests assume the app is at http://localhost:5001 (hardcoded in `viikko3/login/src/tests/resource.robot`). Do not change the port without updating the tests.

- Browser tests require Node + Playwright browsers. Install Node deps in `viikko3/login` with `npm ci` or `npm install` and then `npx playwright install` to fetch browser binaries.

- The app uses in-memory user storage (no DB). Tests call `POST /tests/reset` to clear state — useful for manual resets: `curl -X POST http://localhost:5001/tests/reset`.

- Key files:
  - App: `viikko3/login/src/index.py` and `viikko3/login/src/app.py`
  - Tests: `viikko3/login/src/tests/*.robot`
  - Test helper: `viikko3/login/src/AppLibrary.py` (creates users and calls reset)
  - Python metadata: `viikko3/login/pyproject.toml`

If you want the per-project AGENTS.md expanded with exact uv-run examples and troubleshooting notes, tell me which machine/CI environment you'll run in and I'll add them.
