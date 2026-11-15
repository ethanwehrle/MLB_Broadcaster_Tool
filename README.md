# MLB Broadcaster Tool

A Python toolkit for pulling MLB stats, standings and box scores into a form a broadcaster can use on air: quick lookups, game notes and storylines.

> **Status:** early development. Things will change.

## Features

- [ ] Team and player lookup
- [ ] Standings snapshot
- [ ] Box score summaries for the most recent game
- [ ] Pre-game notes sheet (matchups, streaks, milestones)
- [ ] Export to Markdown / PDF

## Tech stack

- Python 3.12+
- [MLB-StatsAPI](https://github.com/toddrob99/MLB-StatsAPI), a wrapper around the public MLB Stats API

## Getting started

### Prerequisites

- Python 3.12 or newer
- Git

### Install

```bash
git clone https://github.com/<your-username>/MLB_Broadcaster_Tool.git
cd MLB_Broadcaster_Tool

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### Quick example

```python
import statsapi

statsapi.lookup_team("blue jays")    # Toronto's team id is 141
print(statsapi.standings())

game_pk = statsapi.last_game(141)
print(statsapi.boxscore(game_pk))
```

## Project structure

```
MLB_Broadcaster_Tool/
├── src/
│   └── mlb_broadcaster_tool/   # Application code
├── tests/                      # Tests (pytest)
├── AGENTS.md                   # Instructions for AI coding agents
├── CLAUDE.md                   # Points Claude Code at AGENTS.md
├── requirements.txt
├── LICENSE
└── README.md
```

## Running tests

```bash
pip install pytest
pytest
```

## Contributing

Issues and pull requests are welcome. For larger changes, open an issue first so we can discuss the approach.

1. Fork the repo and create a branch: `git checkout -b feature/my-change`
2. Commit your changes with a clear message
3. Push and open a pull request

## Data and attribution

Data comes from the MLB Stats API. Use of MLB data is subject to MLB Advanced Media's terms: <http://gdx.mlb.com/components/copyright.txt>. This project is not affiliated with or endorsed by Major League Baseball.

## License

[MIT](LICENSE)
