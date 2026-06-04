# python-coach-course

Self-paced, test-driven Python course. Learner edits `solution.py`. AI coach
manages exercises, hints, reviews, and progress tracking.

## Repo Layout

| Path | Role |
|---|---|
| `COACH.md` | Contract: roles, rules, exercise workflow |
| `STRUCTURE.md` | File inventory, lesson layout, conventions |
| `rubric.md` | 7-point review checklist |
| `progress.json` | Course state (cursor, completions, weaknesses) |
| `testutils.py` | `load_solution()` helper for importing exercise solutions |
| `pyproject.toml` | Python 3.11+, pytest config, ruff config |
| `lessons/<topic>/<exN_name>/` | Exercises: `prompt.md`, `theory.md`, `solution.py`, `test_solution.py` |
| `notes/mistakes.md` | Recurring mistakes ledger |
| `notes/cheatsheet.md` | Patterns ledger |
| `notes/bug_log.md` | Bug-archaeology log (learner writes before asking hints) |
| `notes/future_plans.md` | Deferred features, not yet implemented |

## OpenCode Architecture (`.opencode/`)

### Agents

| Agent | File | Role |
|---|---|---|
| **coach** | `agents/coach.md` | Primary orchestrator. Never reads/writes files. Delegates everything. |
| **resumer** | `agents/resumer.md` | File-reading proxy. Reads state + exercise files, returns summaries. |
| **tester** | `agents/tester.md` | Runs `pytest -q` + `python tools/check_lint.py`. Diagnoses failures. |
| **hint-provider** | `agents/hint-provider.md` | Gives hints. Enforces bug-archaeology gate (no entry = no hint). |
| **reviewer** | `agents/reviewer.md` | Post-green 7-point rubric review. |
| **exercise-scaffolder** | `agents/exercise-scaffolder.md` | Creates 4-file exercise folders (reads COACH.md + STRUCTURE.md first). |
| **progress-tracker** | `agents/progress-tracker.md` | Sole write agent. Updates progress.json + notes/*.md. |

### Skills (loaded on demand, not at startup)

| Skill | File | When to load |
|---|---|---|
| `course-conventions` | `skills/course-conventions/SKILL.md` | Workflow rules, bug-archaeology, contract |
| `exercise-patterns` | `skills/exercise-patterns/SKILL.md` | Exercise file templates |
| `coaching` | `skills/coaching/SKILL.md` | Rubric, hint ladder, habit vs one-off rules |

### Commands

| Command | File | What it does |
|---|---|---|
| `resume` | `commands/resume.md` | Fires resumer, returns 1-screen orientation summary |
| `coach-review` | `commands/coach-review.md` | Fires reviewer, shows rubric result |

## Workflow

1. **Session start**: coach fires resumer → presents 3-line summary → asks "ready?"
2. **Exercise loop**: learner codes → coach fires tester → pass → reviewer → progress-tracker → exercise-scaffolder
3. **On fail**: coach checks bug_log → if yes, fires hint-provider → learner fixes → re-test
4. **Context full**: learner types `/resume` → resumer returns 20-line summary → new baseline

## Hard Rules

1. Never read files directly — ask resumer.
2. Never write solution.py unless learner explicitly asks for the solution.
3. No hint without a bug_log entry (bug-archaeology rule).
4. Never advance cursor before progress-tracker confirms writes.
5. Tests are law — never weaken or modify tests.

## Conventions

- `theory.md` required for all new exercises (going-forward rule).
- `solution.py` starts as `NotImplementedError` stub only.
- Disallowed builtins must have A/B examples in prompt.
- Habit-level mistakes (2+ exercises) go into `mistakes.md`; one-offs go to watchlist only.
- Coach never gives code as a "hint" — follows the 5-step hint ladder.
