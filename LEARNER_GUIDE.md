# Learner Guide

This is a self-paced Python course. You write small functions; the
coach AI writes the tests, the prompt, and the theory. The contract is
"tests are the definition of correct". You don't need a CS background;
the prompts and theory are written to be read on their own.

If you only read one document, read this one. If you want the deep
detail on a specific thing, the pointers at the bottom tell you where
to look.

## The basic loop

For every exercise, in this order:

1. **Open your current exercise.** It's whatever `progress.json` says
   under `cursor`. As of the last update, that's
   `03_algorithmic_foundations/ex01_bsearch_index`.
2. **Read `prompt.md` and `theory.md`.** The prompt tells you what to
   build; the theory explains the mental model and the common pitfalls.
3. **Edit only `solution.py`.** The other three files in the folder
   (`prompt.md`, `theory.md`, `test_solution.py`) are read-only.
4. **Run the gate:**
   ```powershell
   pytest -q
   python tools/check_lint.py
   ```
   Both must be green. If either fails, fix the code. Don't disable a
   rule to make ruff happy.
5. **Stop and wait for the coach's review.** The coach looks at your
   solution against `rubric.md` and either moves on or asks you to
   refactor. Don't move on by yourself.

That's the whole loop. Five steps, repeated ~30-50 times.

## The 4 commands you will actually use

```powershell
pytest -q                      # run all tests
python tools/check_lint.py     # run the linter
# git add ... && git commit -m "..."  # auto-done by coach; see notes/git_cheatsheet.md
# (optional) open progress.json to see your cursor and review queue
```

You do not need to memorise anything else. The rest of git, pytest, and
ruff is in the cheatsheet files in `notes/`.

## When you're stuck: the 60-second rule

A test failed. Before you ask the AI for a hint, write a 1-paragraph
entry in `notes/bug_log.md`:

```
## YYYY-MM-DD — <lesson>/<exercise>
- Tried: ...
- Expected: ...
- Happened: ...     (paste the actual test message)
- Root cause hypothesis: ...   (best guess, doesn't have to be right)
```

The act of writing the entry catches half the bugs by itself. The
coach is **not allowed** to give you a hint until this entry exists
(that's the "bug-archaeology rule" in `COACH.md`). If you already
know the answer, write a one-liner like
"obvious typo: variable `x` should be `n`. skip the log for this one"
and the coach can move on.

## After green: review, then next

Once both `pytest -q` and `python tools/check_lint.py` are green, the
coach does a short style/structure review. You do not run this; the
coach does. The coach might:

- Move on to the next exercise (most common).
- Ask you to refactor a recurring pattern (e.g. "you keep using
  quadratic list membership — let's use a set here").
- Strengthen the tests with a new edge case (this is allowed; tests
  are the source of truth).

The coach then updates `progress.json` and `notes/cheatsheet.md`,
auto-commits everything to git, pushes to remote, and generates the
next exercise folder.

## Spaced repetition is automatic

`progress.json` has a `review_queue` with 26 entries from the
exercises you've already finished. The schedule starts at 7 days after
you completed each one and stretches out to ~6 months. On a day where
you have a review due, the exercise is part of your "session work" —
you re-solve it (or at least re-explain your solution) before moving
on. This is the part of the course that turns "I solved it once" into
"I still remember it six months later". You do not have to schedule
it; the queue tells you.

## Things that are easy to get wrong

- **Don't write code in `test_solution.py`.** The tests are the AI's
  job. If you think a test is wrong, ask the coach to fix it.
- **Don't disable a ruff rule to make lint pass.** The lint failure
  is the same as a test failure. Fix the code.
- **Don't skip the `bug_log.md` entry.** The 60 seconds of writing it
  is the point.
- **Don't move to the next exercise before the coach has reviewed.**
  Review is short, but it is part of the loop.
- **Don't try to game the review queue by clearing it all at once.**
  The schedule is the schedule; doing today's review today is the
  intent.

## Where to look when you want more detail

- `COACH.md` — the full contract (read this if you want to know what
  the coach is *allowed* to do).
- `STRUCTURE.md` — the file layout (read this if you're an AI session
  or if you want to know why a file exists).
- `notes/cheatsheet.md` — pattern reference, short.
- `notes/git_cheatsheet.md` — git reference, 1 page.
- `notes/bug_log.md` — your bug history. Starts with one example
  entry; you append to it.
- `notes/mistakes.md` — recurring mistakes the coach has flagged.
- `notes/future_plans.md` — items the course has explicitly deferred
  (so a future AI session doesn't re-propose them as new).
- `progress.json` — your state (cursor, completed list, review queue,
  style profile, weakness tags).
- `rubric.md` — the 7-point review checklist the coach uses.

## One paragraph summary

Open your current exercise, read the prompt and theory, edit
`solution.py`, run `pytest -q` and `python tools/check_lint.py` until
both are green, log a quick `bug_log` entry if you got stuck, and wait
for the coach's review. The coach updates state and gives you the
next exercise. Repeat. The review queue keeps old exercises warm.
