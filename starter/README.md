# Penny Lane Financial Planner

A hands-on Claude Code workshop project.

## Setup

### 1. Install uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Install Claude Code

```bash
npm install -g @anthropic-ai/claude-code
```

### 3. Clone and install

```bash
git clone <repo-url>
cd penny-lane
uv sync
```

### 4. Verify

```bash
uv run python -c "import fastapi; print('Ready!')"
```

## Running the app

Once Claude Code builds your app:

```bash
uv run uvicorn app:app --reload
```

Then open http://localhost:8000 in your browser.

## Workshop instructions

See [WORKSHOP.md](WORKSHOP.md) for the exercise.
