# 0 · Say hello (6 min)

Goal: open the app, set up your folder in one paste, and see Claude come alive.
No git, no terminal, no setup.

## Open an empty folder
1. Open the **Claude Code desktop app**.
2. Click the **Code** tab.
3. Click **Select folder**. Make a **new empty folder** (e.g. on your Desktop,
   call it `workshop`) and open it.

## Get today's files (paste this once)

Paste this whole block as your first message. Claude will download today's files
into your folder:

> Set up my workshop folder. Download these files exactly as they are, and put the four data files inside a `data` subfolder:
> - https://raw.githubusercontent.com/wojtyniakAQ/claude-code-workshop/main/vp-workshop/starter/CLAUDE.md → save as CLAUDE.md here in the top folder
> - https://raw.githubusercontent.com/wojtyniakAQ/claude-code-workshop/main/vp-workshop/starter/data/jan.csv → save in data/
> - https://raw.githubusercontent.com/wojtyniakAQ/claude-code-workshop/main/vp-workshop/starter/data/feb.csv → save in data/
> - https://raw.githubusercontent.com/wojtyniakAQ/claude-code-workshop/main/vp-workshop/starter/data/mar.csv → save in data/
> - https://raw.githubusercontent.com/wojtyniakAQ/claude-code-workshop/main/vp-workshop/starter/data/notes.txt → save in data/
>
> Then tell me what you set up.

If Claude says it couldn't find or download the files (a "404" or "not found"),
don't worry -- tell your facilitator and they'll hand you today's backup copy.

If a small box pops up asking permission to run something, click **Allow** -- that
just means Claude is asking before it acts. You're in control; that's normal.

(You just watched it fetch files and organize a folder for you. That's the job.)

## Your first message

Now the fun one:

> Make a file called `hello.html` with my name in big friendly letters and a button that fires confetti when I click it. Then show it to me.

Replace "my name" with your actual name if you like.

## What to notice
- Claude **wrote a real file** and it popped up in the preview on the right.
- Click the confetti button. You made that, by asking.
- You never opened a code editor, a terminal, or installed anything.

You just talked, and it built something. That's the whole game.
