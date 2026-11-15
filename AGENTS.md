# AGENTS.md

Instructions for AI coding agents (Claude Code, Codex, Copilot, Cursor and others) working in this repository. Human contributors should start with [README.md](README.md).

## Project overview

MLB Broadcaster Tool is a Python project that turns MLB Stats API data (standings, box scores, player and team stats) into broadcaster-friendly output such as game notes and quick-reference sheets.

- Language: Python 3.12+
- Main dependency: `MLB-StatsAPI` (imported as `statsapi`)
- Application code: `src/mlb_broadcaster_tool/`
- Tests: `tests/`

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS / Linux
pip install -r requirements.txt
```

## Commands

| Task          | Command                       |
| ------------- | ----------------------------- |
| Install deps  | `pip install -r requirements.txt` |
| Run tests     | `pytest`                      |

Update this table when lint, format or run commands are added.

## Code conventions

- Follow PEP 8. Use type hints on public functions.
- Keep API calls in one place (for example a `data/` or `api.py` module) so the rest of the code works with plain Python objects and can be tested without network access.
- Prefer small, pure functions for formatting stats into broadcast text.
- Docstrings on public functions: one line on what it does, plus args and return value when not obvious.
- No secrets in code. The MLB Stats API needs no key; if one is ever added, read it from an environment variable and document it in README.md.

## Testing

- Put tests in `tests/`, named `test_*.py`.
- Do not hit the live MLB API in unit tests. Mock `statsapi` calls or use saved JSON fixtures in `tests/fixtures/`.
- Run `pytest` before reporting a task as done, and report failures honestly.

## Working with the MLB Stats API

- Docs for the wrapper: <https://github.com/toddrob99/MLB-StatsAPI/wiki>
- Useful IDs: Toronto Blue Jays = `141`. Use `statsapi.lookup_team()` and `statsapi.lookup_player()` to find others; don't hard-code IDs you haven't verified.
- `statsapi.standings()`, `statsapi.boxscore()` and similar return preformatted strings; the `*_data()` variants return dicts. Prefer the `_data` versions for anything you need to process.
- Be polite to the API: cache results during a session and avoid tight loops of requests.

## Git and pull requests

- Never commit `.venv/`, `.env` or other local files (see `.gitignore`).
- Keep commits focused, with imperative messages ("Add standings formatter").
- Don't push, force-push or rewrite history unless the maintainer asks.
- Update README.md when you add a user-facing feature or command.

## Boundaries

- Ask before adding new runtime dependencies; add any that are approved to `requirements.txt` with a pinned version.
- Don't change the license or the attribution section of README.md.
- If a task is ambiguous, ask instead of guessing.
