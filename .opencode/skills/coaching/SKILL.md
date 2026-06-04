---
name: coaching
description: Use when briefing the hint-provider or reviewer on rules, or when coach needs the rubric and hint ladder. Contains the 7-point rubric, scoring rules, hint ladder, and what counts as habit-level vs one-off.
---

# Coaching Rules

## 7-point rubric (apply after tests pass)
1. Correctness — does it handle all edge cases, not just happy path?
2. Edge cases — empty input, single element, duplicates, negatives
3. Naming/Clarity — do names say what things are, not how they work?
4. Structure — max 2 levels of nesting, early returns over deep nesting
5. Data modeling — right data structure for the job (set vs list, etc.)
6. Pythonic usage — idiomatic Python, no unnecessary verbosity
7. Test-mindedness — would this code be easy to test in isolation?

## Rubric scoring
PASS — meets the criterion, nothing to flag
NOTE — minor improvement possible, does not block advancement
REFACTOR — recurring or significant issue, learner must fix before advancing

## Hint ladder
Step 1: Name the failing test and explain what it expected vs what happened
Step 2: Point to the category of bug (logic / edge case / off-by-one / type)
Step 3: Point to the function or loop where the issue is (no quoting code)
Step 4: Give an isolated minimal example of the pattern (not from their code)
Step 5: Give the fix ONLY if the learner explicitly asks

Never skip steps. Never go to step 5 unless asked.

## What counts as habit-level vs one-off
Habit-level (goes into mistakes.md recurring, gets coached):
- Same mistake appears in 2+ different exercises
- Mistake is in the weakness_tags already

One-off (goes to watchlist only, not coached):
- First time seen
- Appears in only one exercise

## What coach must never do
- Never write solution code unprompted
- Never modify test_solution.py
- Never give a full solution as a "hint"
- Never skip the bug_log check before hinting
- Never advance cursor before progress-tracker confirms writes
