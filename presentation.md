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

## Paperback Writer

Good workflow for a new project:
0. Initialize the repo and project with applicable
1. Describe the problem you're solving, **what** you want to build, ask Claude to *interview* you about the idea, ask it write a `PRD.md`
2. Tell about your preferences, **how** you want to build that—programming languages, frameworks, etc. ask to put it in `CLAUDE.md` or `docs/ARCHITECTURE.md`
3. For large projects
	1. Ask to prepare implementation doc and put it in a file, e.g. `docs/IMPLEMENTATION_PLAN.md`
	2. Go through the plan one by one

---

## Hey Claude

*Take a sad codebase and make it better*

Always start complex work in plan mode (`/plan`):
- Claude reads the codebase, asks clarifying questions, proposes an approach
- You review and adjust *before* any code is written
- Cheap to throw away a plan, expensive to throw away code

Don't get attached to code. Get attached to:
- **Business logic** -- the rules and decisions
- **Data flow** -- how information moves through the system
- Code is just the current expression of those things. Let Claude rewrite it.

---

## Twist and gcloud

Claude Code wraps any CLI tool you already use:
- `gcloud` -- deploy, configure, inspect resources
- `kubectl` -- manage clusters and pods
- `terraform` -- infrastructure as code
- Any CLI that prints text, Claude can read and act on

Example: "Deploy this app to Cloud Run in the staging project"
- Claude runs `gcloud run deploy`, reads the output, fixes config issues, retries

---

## Fixing a Hole

*Where the bugs get in and stop my mind from wandering*

Claude Code is not just for writing code:
- **Log analysis** -- "here's a stack trace, find the root cause"
- **Test scripts** -- "write a script that reproduces this bug"
- **Data inspection** -- "query the database and tell me why this row is wrong"
- **Incident response** -- paste an alert, ask Claude to investigate

The pattern: give Claude *context* (logs, errors, data), ask a *question*, let it explore.

---

## Ticket to Ride

### Issues

- "Look at issue #42 and implement what it describes"
- "Create an issue for the bug we just found"
- Claude reads issue descriptions, comments, labels -- full context

### Pull requests

- "Create a PR for my current changes"
- "Review PR #15 and leave comments"
- "Look at the failing checks on my PR and fix them"

### Code review

- "Read the comments on my PR and address them"
- Claude reads reviewer feedback, makes changes, pushes -- you just approve

All through `gh` -- no browser needed.

---

## Norwegian Worktree

Claude handles all of git for you:
- Commits with meaningful messages
- Branch management, merges, conflict resolution
- Interactive rebase? Just describe what you want rearranged.

### Worktrees

- Claude can spin up a git worktree to work on a task in isolation
- Your main branch stays untouched while it experiments
- If it works, merge. If not, throw it away.
- Great for "try this risky refactor without breaking anything"

---

## Don't Let Me Down

Three permission modes to match your comfort level:
- **Ask every time** -- Claude asks before each file edit or command (start here)
- **Auto-allow common tools** -- allow reads, globs, greps automatically
- **YOLO mode** -- Claude runs everything without asking (use with caution)

Start restrictive, loosen as you build trust. You can always say no to a
specific action even in permissive modes.

CLAUDE.md is also a guardrail: "never run `rm -rf`", "never push to main",
"always run tests before committing"

---

## In My Life

*There are places I remember*

Claude Code remembers across conversations:
- Project conventions it learned the hard way
- Your preferences ("don't use ternary operators", "always add type hints")
- External references (where docs live, which Slack channel to check)

Stored in `~/.claude/` and `.claude/` -- just markdown files you can read and edit.

Tell Claude "remember this" and it will. Tell it "forget that" and it does.

---

## With a Little Help from My Friends

Three tiers, increasing autonomy:

1. **Penny Lane** -- paste a prompt, get a working app (~15 min)
2. **Savings Copilot** -- collaborate with Claude: write PRD, plan, test (~20 min)
3. **Dev Workflows** -- fix a buggy script, create PRs, analyze data (~20 min)

Go at your own pace. Finishing tier 1 is a success. Tier 3 is a bonus.

`cd tier1-budget-tracker` and open `INSTRUCTIONS.md`