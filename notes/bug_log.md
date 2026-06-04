# Bug Log (Learner-Maintained)

This file is the durable record of bugs the learner has hit, the
root-cause hypothesis, and the fix. It exists to make every failure
a retrievable artifact instead of a one-off event.

## How it works

Before asking the AI coach for a hint on a failing test, the learner
writes 1 short paragraph in this file using the format below. The
coach must not provide a hint until the entry exists (per
`COACH.md` step 4a, the "Bug-archaeology rule"). The 60-second
discipline of writing the entry is the point.

## Format

```
## YYYY-MM-DD — <lesson>/<exercise>

- **Tried:** (1-2 lines; what your code does, in plain English)
- **Expected:** (1 line; what you thought would happen)
- **Happened:** (1 line; the actual test failure, copy-pasted)
- **Root cause hypothesis:** (1 line; your best guess, even if wrong)
```

The hypothesis doesn't have to be correct. The act of writing it down
catches half the bugs by itself.

## Example entry

```
## 2026-02-07 — 01_basics/ex04_read_int_lines

- **Tried:** loop over `text.splitlines()`, call `int(line)` inside
  a bare `try: ... except:` and skip the line on failure.
- **Expected:** the test for `ValueError` on bad input would pass
  because I "handled" the exception.
- **Happened:** `pytest` failed with "no exception raised" for a
  case that expected `ValueError` to propagate.
- **Root cause hypothesis:** my `except:` swallowed the error and
  the function silently returned. I should have `raise ValueError(...)`
  explicitly inside the `except` block, or caught only the specific
  exception. Also, "bare `except`" hides real bugs (KeyboardInterrupt,
  MemoryError).
```
