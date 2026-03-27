## All You Need is Claude

My job today is to convince you that you *can* use Claude Code for everything—not just code generation

- PRD drafting—*gimme some ideas*
- CLAUDE.md management
- Creating memories together

And technical stuff as well:
- **Git**: checkouts, merges, conflict resolution
- **GitHub**: tasks, pull requests, comments
- **Operations**: builds, deployments, configuration
- **GCP**: everything that `gcloud` allows
- **Debugging**: log analysis, test scripts, root cause analysis

---

## Let it Code

Treat CC like a coworker:
- It's opinionated and holds strong opinions
- Terribly at guessing and reading your mid
- But good at following clear instructions and adjusting to preferences
- Needs a reminder from time to time

---

## While My CLAUDE.md Gently Leads

### CLAUDE.md

- Project-wide shared preferences
- Should focus on project structure, languages/frameworks preferences
- Links to detailed @docs
- Keep it short (under 40k bytes)

### .claude/CLAUDE.md or CLAUDE.local.md

- Personal per-project preferences
- e.g. separate directory for keeping notes you're not going to commit in

### ~/.claude/CLAUDE.md

- Personal preferences across all the projects
- e.g. use `jujustsu` instead of `git`

---

## PRD writer

Good workflow for a new project:
0. Initialize the repo and project with applicable
1. Describe the problem you're solving, **what** you want to build, ask Claude to *interview* you about the idea, ask it write a `PRD.md`
2. Tell about your preferences, **how** you want to build that—programming languages, frameworks, etc. ask to put it in `CLAUDE.md` or `docs/ARCHITECTURE.md`
3. For large projects
	1. Ask to prepare implementation doc and put it in a file, e.g. `docs/IMPLEMENTATION_PLAN.md`
	2. Go through the plan one by one

---
###