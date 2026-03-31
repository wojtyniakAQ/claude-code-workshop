# Penny Lane Financial Planner

## Project overview

A personal finance web application.
See PRD.md for full product requirements.

## Tech stack

- **Python 3.12** with **FastAPI** for the backend
- **Jinja2** templates for HTML rendering
- **SQLite** for persistence (use the `sqlite3` stdlib module, no ORM)
- **Plotly.js** for interactive charts (loaded via CDN, rendered client-side)
## Conventions

- Use `uv` for all package management. Never use `pip` directly.
- Keep the app in a single file: `app.py`. Do not split into multiple modules.
- Keep all HTML templates in a `templates/` directory using Jinja2.
- Store the SQLite database as `penny_lane.db` in the project root.
- Use raw SQL via `sqlite3` -- do not introduce SQLAlchemy or any ORM.
- Run the app with: `uv run uvicorn app:app --reload`
- After building the app, start the server automatically so the user can test right away.

## Code style

- Type hints on all function signatures.
- No inline imports -- all imports at the top of the file.
- Keep functions short and focused. Prefer clarity over cleverness.

## Important

- Before using any library API, check the installed version and verify the
  usage matches that version's API. Library APIs change between major
  versions -- do not assume the latest docs apply.

