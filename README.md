# MLB Broadcaster Tool

A chat-based research assistant for MLB broadcasters. Ask a question in plain English and get back a structured report with real data and sources you can use on air.

Example questions:

- "How does Clement do against right-handed batters?"
- "How do Aaron Judge's last ten at-bats compare to the rest of his season and career?"
- "Any fun social media trends or topics about Kirk?"

> **Status:** early development. Things will change.

## How it works

1. **Research agent** (Claude) works out what data the question needs and fetches it.
2. **Data layer** answers from two sources:
   - **Historical:** pitch-by-pitch data stored in SQL Server (Docker) and aggregated with SQL
   - **Live:** the MLB Stats API, for current games and the latest numbers
3. **Presentation agent** (Claude) turns the results into a report built from UI components (tables, bullet lists, charts) rather than a plain text reply.

## Tech stack

| Layer    | Tech |
| -------- | ---- |
| Frontend | React |
| Backend  | Python, FastAPI |
| AI       | Claude API |
| Data     | SQL Server (Docker), [MLB-StatsAPI](https://github.com/toddrob99/MLB-StatsAPI) |

## Project structure

```
MLB_Broadcaster_Tool/
├── backend/
│   ├── app/              # FastAPI app, agents, data access
│   ├── tests/            # pytest tests
│   └── requirements.txt
├── frontend/             # React app
├── AGENTS.md             # Instructions for AI coding agents
├── CLAUDE.md             # Points Claude Code at AGENTS.md
├── LICENSE
└── README.md
```

## Getting started

### Prerequisites

- Python 3.12+
- Node.js 20+ (for the frontend)
- Docker (for SQL Server)
- A Claude API key

### Backend

```bash
git clone https://github.com/<your-username>/MLB_Broadcaster_Tool.git
cd MLB_Broadcaster_Tool/backend

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### Frontend

Not set up yet. Instructions will go here once the React app is created.

## Running tests

```bash
cd backend
pytest
```

## Contributing

Issues and pull requests are welcome. For larger changes, open an issue first so we can discuss the approach.

## Data and attribution

Live data comes from the MLB Stats API via [MLB-StatsAPI](https://github.com/toddrob99/MLB-StatsAPI) by [Todd Roberts](https://github.com/toddrob99). Use of MLB data is subject to MLB Advanced Media's terms: <http://gdx.mlb.com/components/copyright.txt>. This project is not affiliated with or endorsed by Major League Baseball.

## License

[MIT](LICENSE)
