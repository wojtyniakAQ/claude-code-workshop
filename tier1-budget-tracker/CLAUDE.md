# Penny Lane Financial Planner

## Project overview

A personal finance web application with a music analytics bonus feature.
See PRD.md for full product requirements.

## Tech stack

- **Python 3.12** with **FastAPI** for the backend
- **Jinja2** templates for HTML rendering
- **SQLite** for persistence (use the `sqlite3` stdlib module, no ORM)
- **Plotly.js** for interactive charts (loaded via CDN, rendered client-side)
- **Pandas** for data analysis tasks only (not for simple CRUD)

## Conventions

- Use `uv` for all package management. Never use `pip` directly.
- Keep the app in a single file: `app.py`. Do not split into multiple modules.
- Keep all HTML templates in a `templates/` directory using Jinja2.
- Store the SQLite database as `penny_lane.db` in the project root.
- Use raw SQL via `sqlite3` -- do not introduce SQLAlchemy or any ORM.
- Run the app with: `uv run uvicorn app:app --reload`

## Code style

- Type hints on all function signatures.
- No inline imports -- all imports at the top of the file.
- Keep functions short and focused. Prefer clarity over cleverness.

## Data

- `data/streams.csv` contains sample music streaming data for analysis.
- When importing CSV data, always load into a SQLite table, then query from there.
