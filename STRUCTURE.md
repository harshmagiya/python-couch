# Structure

## a) What this repo is

This is a self-paced, test-driven Python course repo where the learner writes small `solution.py` functions for each exercise and an external AI coach (not bundled here) writes the tests, prompt, and theory, then reviews the solution against a rubric. The repo is the course material and the learner's progress state — nothing more.

## b) File inventory (top level)

| Path | Role | Owner |
|---|---|---|
| `README.md` | Short pointer to `COACH.md` | Coach |
| `COACH.md` | The contract: roles, rules, exercise workflow, folder layout | Coach |
| `STRUCTURE.md` | This file. Cold-start entry point for a model session | Coach |
| `rubric.md` | 7-point review checklist used after each green test | Coach |
| `progress.json` | Course state: cursor, completed list, weakness tags, spaced-repetition review queue | Coach (write) / Learner (read) |
| `pyproject.toml` | Python 3.11+, pytest config (`testpaths = ["lessons"]`) | Coach |
| `testutils.py` | `load_solution()` helper that imports each `solution.py` by file path with a unique module name, so 27 exercises with the same `solution.py` filename never collide | Coach |
| `.gitignore` | Excludes venv, caches, compiled files, the `NUL` PowerShell artifact, and Jupyter checkpoints | Coach |
| `lessons/` | All lesson folders (see lesson layout below) | Mixed |
| `notes/cheatsheet.md` | Short pattern ledger the coach maintains | Coach |
| `notes/mistakes.md` | Recurring-mistake ledger the coach maintains | Coach |

## c) Lesson layout

Every exercise lives at `lessons/<nn_topic>/ex<nn_name>/` and contains exactly these files:

| File | Owner | Editable by learner? | Purpose |
|---|---|---|---|
| `prompt.md` | Coach | No (read-only) | Task description, signature, examples, constraints, disallowed-builtins with A/B example, complexity requirement, reference to `theory.md` |
| `theory.md` | Coach | No (read-only) | Mental model, why-it-matters, pitfalls, edge cases. **Required for all exercises created from this point forward (see COACH.md §"Theory Requirement (Going-Forward Rule)").** Not present in `01_basics/` or `02_collections/`. |
| `solution.py` | Learner | **Yes — the only file the learner edits** | Contains the function under test. Starts as a `NotImplementedError` stub. |
| `test_solution.py` | Coach | No (read-only) | Pytest file. Tests are the definition of correct; the coach may strengthen them after green but never weaken. |

Current lesson inventory:

| Topic | Folder | Exercises | Has `theory.md`? |
|---|---|---|---|
| 01 Basics | `lessons/01_basics/` | ex01..ex05 | No (predates the rule) |
| 02 Collections | `lessons/02_collections/` | ex01..ex22 | No (predates the rule) |
| 03 ML Foundations | `lessons/03_ml_foundations/` | ex01..ex03 | Yes (paused, do not add to) |
| 03 Algorithmic Foundations | `lessons/03_algorithmic_foundations/` | ex01..ex16 | Yes (active) |
| 04 Numerical Python | `lessons/04_numerical_python/` | ex01..ex05 | Yes (active) |

## d) Recommended reading order for a new AI session

1. **`STRUCTURE.md`** (this file) — orient on the layout.
2. **`COACH.md`** — load the contract you must follow (no patches by default, hints before code, theory.md going-forward rule, review workflow).
3. **`progress.json`** — read `cursor` to find the current exercise, then read `completed` to know the learner's history, then read `weakness_tags` and `style_profile.watchlist` to know what to watch for in review.
4. **`rubric.md`** — the 7-point checklist you apply after every green test.
5. **`notes/mistakes.md`** — recurring mistakes to flag.
6. **`notes/cheatsheet.md`** — patterns the learner has internalized (don't re-teach these).
6.5. **`notes/future_plans.md`** — items the learner has explicitly deferred from earlier planning sessions. Read this so you don't re-propose them as if they were new.
7. **Current exercise's `prompt.md` + `theory.md`** — only then generate the prompt for the learner (or review their `solution.py` if one exists).

## e) No AI coach implementation lives in this repo

There is no OpenCode agent, no `.opencode/`, no `opencode.json`, no skill files, no subagent config, and no MCP server wired up in this checkout. The "AI coach" is an external AI (e.g. running inside an IDE or CLI) that reads `COACH.md` and behaves accordingly. If you are a model reading this repo, *you* are the coach for this session.

## f) Files explicitly out of scope for AI sessions

The files `opencode-reader-guide.md` and `opencode-reader.html` in the repo root are personal dev artifacts. AI coaches should ignore them and treat them as out of scope — they are not part of the course, not part of the contract, and not part of any review or generation. If a future session encounters them, do not read them as inputs to your behaviour.

## g) Future exercise formats (deferred, see `notes/future_plans.md` §2)

The current `exercises` all share the same shape: a `solution.py` the learner edits, a `test_solution.py` the AI owns, and a `theory.md` the AI owns. Three additional formats are planned but not yet implemented. Do not invent them on your own; the details are in `notes/future_plans.md`.

| Format | What the learner does | What the AI writes | Status |
|---|---|---|---|
| **Read-the-code** | Reads a `quarry.py` (no `solution.py`), writes a 1-2 paragraph explanation + bug + fix in a separate file | `quarry.py` (read-only), `prompt.md`, `theory.md`, `test_solution.py` (graded against a rubric) | Deferred (low priority) |
| **Write-the-tests** | Writes `test_solution.py` from scratch against a provided `solution.py` | `solution.py`, `prompt.md`, `theory.md`, a hidden reference test set, and a grading script (line coverage + false-positive rate on known-buggy solutions) | Deferred (low priority) |
| **Portfolio checkpoint** | Builds a small end-to-end artifact (e.g. a 50-line logistic-regression-from-scratch) | A relaxed `test_solution.py` (mostly "it runs and produces sensible numbers"), a `theory.md` linking to the underlying papers, and a `notes/portfolio/<name>/` directory the learner publishes | Deferred (revise after ~15 green exercises in `03_algorithmic_foundations`) |
| **Before-you-start diagnostic** | Solves 5-10 tagged problems so the AI can map a fresh learner to a starting exercise | A set of problems with per-problem `strategies` tags, and a scoring script that recommends the right lesson+exercise | Deferred (use case is future learners, not the current one) |
