# AGENTS.md

Instructions for AI coding agents (Claude Code, Codex, Copilot, Cursor and others) working in this repository. Human contributors should start with [README.md](README.md). The maintainer's design notes are in `plan.md` when present; read it for intent, but this file and the code take precedence.

## Project overview

MLB Broadcaster Tool is a chat-based assistant for MLB broadcasters. A user asks a question; a Claude **research agent** decides what data is needed and fetches it; a Claude **presentation agent** turns the results into a structured report made of UI components (tables, bullet lists, charts).

| Area     | Location    | Tech |
| -------- | ----------- | ---- |
| Backend  | `backend/`  | Python 3.12+, FastAPI, Claude API, `MLB-StatsAPI` (imported as `statsapi`) |
| Frontend | `frontend/` | React (not scaffolded yet) |
| Data     | —           | SQL Server in Docker (historical pitch-by-pitch), MLB Stats API (live) |

## Setup

Backend:

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # macOS / Linux
pip install -r requirements.txt
```

Frontend: not set up yet. When it is, document install/run/build commands here.

## Commands

| Task             | Command (from `backend/`)          |
| ---------------- | ---------------------------------- |
| Install deps     | `pip install -r requirements.txt`  |
| Run tests        | `pytest`                           |

Update this table when run, lint, format or frontend commands are added.

## Architecture guidelines

- **Keep the layers separate.** The frontend talks to the backend only over the FastAPI HTTP API. The frontend never calls Claude, the MLB API or the database directly.
- **Backend layout** (grow into this; don't create empty modules ahead of need):
  - `app/main.py`: FastAPI app and routes
  - `app/agents/`: Claude agent logic (research, presentation)
  - `app/data/`: MLB Stats API client and SQL access
  - `app/schemas/`: Pydantic models for requests, responses and report components
- **Report components are a contract.** The presentation agent returns structured JSON (for example `{"type": "table", ...}`) that the React app renders. Define these shapes as Pydantic models in the backend and keep matching TypeScript types in the frontend. Change both together.
- **Historical vs live data:** historical aggregates come from SQL; current-day/live data comes from the MLB Stats API.

## Code conventions

Python:
- PEP 8, type hints on public functions, docstrings where intent isn't obvious.
- Keep external calls (Claude, MLB API, SQL) behind small wrapper functions so the rest of the code can be tested without network access.

React (once added):
- Functional components and hooks. Prefer TypeScript.
- One component per report widget type (table, list, chart, ...).

## Secrets and config

- The Claude API key and database credentials come from environment variables (for example `ANTHROPIC_API_KEY`), loaded from a local `.env` that is git-ignored. Never commit keys.
- When you add a new variable, add it to a `.env.example` with a placeholder value and mention it in README.md.

## Testing

- Backend tests live in `backend/tests/`, named `test_*.py`.
- Unit tests must not call the live MLB API, Claude or a real database. Mock them, or use saved JSON fixtures in `backend/tests/fixtures/`.
- Run the tests before reporting a task as done, and report failures honestly.

## Working with the MLB Stats API

- Wrapper docs: <https://github.com/toddrob99/MLB-StatsAPI/wiki>. It is unofficial and not supported by MLB.
- `statsapi.get(endpoint, params)` returns raw JSON and is the most flexible option. Functions like `standings()` and `boxscore()` return preformatted strings; prefer the `*_data()` variants or `get()` for anything you process.
- Verify IDs with `statsapi.lookup_team()` / `statsapi.lookup_player()` instead of hard-coding guesses (Toronto Blue Jays = `141`).
- Be polite to the API: cache within a session and avoid tight request loops.

## Git and pull requests

- Never commit `.venv/`, `node_modules/`, `.env` or build output (see `.gitignore`).
- Keep commits focused, with imperative messages ("Add standings endpoint").
- Don't push, force-push or rewrite history unless the maintainer asks.
- Update README.md when you add a user-facing feature, command or required env var.

## Boundaries

- Ask before adding new dependencies; pin approved Python deps in `backend/requirements.txt`.
- Don't change the license or the attribution section of README.md.
- If a task is ambiguous, ask instead of guessing.
