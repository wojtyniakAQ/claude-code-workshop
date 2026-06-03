# 2 · How it works (10 min)

You've now built two things. Here's the mental model, in plain English.

## Five things to remember

1. **It's a coworker, not a search box.** It's opinionated, it can't read your
   mind, but it's great at following clear instructions and adjusting when you
   tell it to. Treat it like a sharp new hire: be specific, give feedback.

2. **It works in *your* files.** Everything it makes is a real file in your
   folder that you own. (Remember reveal-in-Finder.) It's not trapped in a chat.

3. **You can give it standing instructions.** There's a file called `CLAUDE.md`
   in your folder -- think of it as the "house rules" Claude reads every time.
   Put a preference there once and you never have to repeat it.

4. **Long chats fill up.** If a conversation gets very long, type `/compact` and
   it tidies up and keeps going. Anything important lives in a file, so it's safe.

5. **You're in control.** It asks before doing anything real, and nothing happens
   that you didn't approve. It will not break your laptop.

## Try it: the house-rules demo

Open `CLAUDE.md` and add one line (or just ask Claude to add it):

> Always use my brand color, a warm amber #F5A623, as the main accent color in anything you build.

Now ask for a quick build and watch it obey *without being reminded*:

> Make me a simple welcome page for my team. Just show it to me.

The amber shows up because Claude read the house rules. Set a preference once;
it sticks.
