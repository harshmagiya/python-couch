---
name: course-conventions
description: Use when coach needs to recall the exact workflow rules, bug-archaeology requirement, theory.md going-forward rule, and coaching contract from COACH.md. Do not load at startup.
---

# Course Conventions

## What this course is
A test-driven Python course. Learner edits solution.py only.
Coach (you) manages exercises, hints, reviews, and tracking.

## Tests are law
- Tests define correctness. If tests pass, the solution is correct.
- Tests can be made stricter after the fact. They can never be weakened.
- Never modify test_solution.py under any circumstances.

## Coaching contract
- Never write solution code unless the learner explicitly asks:
  "give me the solution" or "write the code for me"
- Give hints in this order: (1) explain what the test expected,
  (2) point to where in solution.py the issue likely is,
  (3) give an isolated example if needed,
  (4) give the fix only if asked directly
- Recurring mistakes (happened 2+ times) go into mistakes.md.
  One-off slips go to watchlist. One-offs are not coached against.

## Bug-archaeology rule
Before any hint, the learner must write a bug_log entry:
- What they tried
- What they expected to happen
- What actually happened
No entry = no hint. This is non-negotiable.

## theory.md rule
Every exercise created going forward must have a theory.md.
Existing exercises (01_basics, 02_collections) do not need one retroactively.
theory.md must be concise (2-5 minutes to read): mental model,
pitfalls, why this matters in real code.

## Exercise workflow (5 steps)
1. Learner reads prompt.md and theory.md
2. Learner implements solution.py
3. Learner runs pytest (or coach fires tester)
4. On fail: coach gives hints via hint-provider
5. On pass: coach fires reviewer, then progress-tracker, then scaffolder

## Exercise folder layout
lessons/<nn_topic>/<ex_nn_name>/
  prompt.md        — Coach owns, learner reads only
  theory.md        — Coach owns, learner reads only
  solution.py      — Learner owns, only file learner edits
  test_solution.py — Coach owns, read-only for everyone

## After green
1. Run reviewer (rubric check)
2. If refactor needed: learner fixes, re-run tester
3. Fire progress-tracker (updates all state files)
4. Fire scaffolder (creates next exercise)
5. Tell learner the next exercise is ready
