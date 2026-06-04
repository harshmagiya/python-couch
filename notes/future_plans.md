# Future Plans (Deferred Work + Resume Notes)

This file is the durable handoff document for any future AI session or
for the learner working without AI. It records:

1. **The state of the world at the end of the 2026-06-02 session** —
   so the next session knows exactly what's already done and what's a
   pre-existing decision not to undo.
2. **Items the learner has explicitly deferred** — from earlier
   planning sessions. Do not re-propose these as if they were new.
3. **Items the learner has explicitly rejected** — never re-propose
   these.
4. **Open suggestions the learner wants to discuss** — placeholder
   section for the learner to fill in.

A future AI session should:
- Read `STRUCTURE.md` first.
- Read this file **second**, before generating any new exercise or
  making any structural change.
- Update this file when a deferred item is acted on (move it to "done"
  with a date, or strike it through with a one-line note).

---

## 1. State of the world at end of 2026-06-02 session

### Files added or created (new)

- `notes/bug_log.md` — header + one example entry. The AI coach
  contract now requires a learner to write a 1-paragraph bug-archaeology
  entry in this file before asking the AI for a hint on a failing test
  (per `COACH.md` step 4a).
- `tools/check_lint.py` — runs `python -m ruff check .` and exits with
  the same return code. The CI gate is now:
  `pytest -q && python tools/check_lint.py`.
- `lessons/03_algorithmic_foundations/ex04_kadane_max_subarray/`
  (4 files: `prompt.md`, `theory.md`, `solution.py` stub, `test_solution.py`).
- `lessons/03_algorithmic_foundations/ex09_tree_bfs_level_order/`
  (4 files).
- `lessons/03_algorithmic_foundations/ex10_tree_dfs_inorder/`
  (4 files).
- `lessons/03_algorithmic_foundations/ex13_climb_stairs/`
  (4 files).
- `lessons/03_algorithmic_foundations/ex14_lis/`
  (4 files).
- `lessons/03_algorithmic_foundations/ex15_edit_distance/`
  (4 files).
- `lessons/03_algorithmic_foundations/ex16_top_k_streaming/`
  (4 files).

### Files deleted

- `lessons/03_algorithmic_foundations/ex04_container_with_most_water/`
- `lessons/03_algorithmic_foundations/ex09_reverse_linked_list/`
- `lessons/03_algorithmic_foundations/ex10_has_cycle/`

### Files edited

- All 12 `lessons/03_algorithmic_foundations/ex*_*/theory.md` files
  now end with an "## ML/research connection" section (1 descriptive
  sentence + 1 named library/function example).
- `progress.json`:
  - Added `strategies: list[str]` to all 26 `completed` entries.
  - Added a new top-level `scaffolding` key with pre-declared
    `strategies` for all 16 not-yet-started exercises in
    `03_algorithmic_foundations` (12 in the main track + 4 in the
    extension).
  - Nothing else was changed. `last_updated` is still `"2026-06-02"`,
    `schema_version` still `"1.0"`, all 26 `review_queue` entries
    unchanged.
- `COACH.md`:
  - Step 4 in "Exercise Workflow" now requires both `pytest -q` and
    `python tools/check_lint.py` to be green; failing lint is treated
    the same as failing test.
  - New step 4a — the "Bug-archaeology rule" — added: the coach must
    not provide a hint on a failing test until the learner has written
    a 1-paragraph entry in `notes/bug_log.md`.
- `STRUCTURE.md`:
  - New section (f): "Files explicitly out of scope for AI sessions"
    documents that `opencode-reader-guide.md` and `opencode-reader.html`
    are personal dev artifacts and should be ignored.
  - Reading order (d) now has a step 6.5 that points to this file.
- `notes/cheatsheet.md`:
  - Added an "Algorithmic Foundations track" follow-on section with
    one-liners for Kadane's, sliding window, tree BFS, and tree DFS.
  - Added a "Patterns practiced" section with rough coverage counts
    from `01_basics` + `02_collections` and a "Coming" list for
    `03_algorithmic_foundations`. The "Done" list says **recursion,
    DP, trees, heap, binary search, sliding window, backtracking are
    all 0** in the completed set, and the "Coming" list enumerates
    where they will land.
- `pyproject.toml`:
  - Added `ruff>=0.5.0` to the `dev` optional-dependencies.
  - Added `[tool.ruff]` and `[tool.ruff.lint]` configuration.
    Selected rules: `E, F, W, I, UP, B, SIM`. Ignored: `E501`.
    `line-length = 100`, `target-version = "py311"`.

### Final pytest + lint state

- `python -m pytest -q` — 187 passed, 200 failed.
  - All 200 failures are `NotImplementedError` stubs (the learner has
    not started any of the 12 main-track or 4 extension exercises yet).
  - The 13 pre-existing `03_ml_foundations` stub failures are unchanged.
  - Zero regressions in `01_basics/` or `02_collections/`.
- `python -m ruff check .` — All checks passed.
- `python tools/check_lint.py` — exits 0.

### Cursor and review queue

- `progress.json.cursor` still points at
  `03_algorithmic_foundations/ex01_bsearch_index`. The learner has
  not started any exercise in the new track yet.
- `progress.json.review_queue` is unchanged from the spaced-repetition
  schedule the learner confirmed in the 2026-06-02 turn (26 entries
  from 2026-06-02 through 2026-11-24).

### The `NUL.bak` situation

- The file `NUL.bak` (14,793 bytes) at the repo root is a stale
  pre-2026-06-02 snapshot of `progress.json` (taken before the
  housekeeping pass). It is preserved by user choice and is **not**
  in `.gitignore`. Future AI sessions must treat it as out of scope.

---

## 2. Items explicitly deferred (do not re-propose as new)

### 2.1 Numerical Python mini-track (proposed 2026-06-02)

Insert a new lesson `04_numerical_python/` (or `04_numerical_python/`
positioned between `02_collections` and `03_algorithmic_foundations`)
covering:

- Vectorized thinking: numpy arrays, broadcasting, masking, axis
  semantics. The "think in arrays, not loops" mindset that PyTorch /
  TensorFlow / JAX code requires.
- Numerical stability: log-sum-exp, stable softmax, Kahan summation.
  Why `np.exp(x) / np.exp(x).sum()` overflows and what to do instead.
- Basic probability + sampling + reproducibility: seeds, RNG, simple
  distributions, why a fixed seed makes a notebook experiment
  reproducible.
- Basic linear algebra ops: dot product, norm, matmul, eigendecomposition
  intuition. Not a full LA course — just enough to read papers.
- A "no loops" constraint on a few exercises, to force the vectorized
  habit. Use `np.where` / boolean masking / broadcasting instead of
  Python for-loops.

**Why deferred**: the algorithmic track (`03_algorithmic_foundations`,
16 scaffolded exercises) takes priority. Doing both at once dilutes
focus. Revisit after `ex16_top_k_streaming` is green and the learner
has done the spaced-repetition review of `01_basics` / `02_collections`.

**Estimated effort**: 8-12 exercises scaffolded. Same template as the
algorithmic track. ~3 hours of authoring.

### 2.2 Read-the-code exercise format

A new exercise type where the learner does *not* edit `solution.py`.
Instead, the prompt says:

> Given the 30-50 line function in `quarry.py` (read-only, no
> `solution.py`), do three things:
> 1. Describe in plain English what it does.
> 2. Identify any bug, smell, or non-obvious behavior.
> 3. Propose a one-sentence fix.

Tests assert the explanation matches a rubric. The infrastructure
needs a `quarry.py` per exercise, a scoring rubric, and probably a
custom test that does fuzzy text matching (or a multi-choice answer
file the learner fills in).

**Why deferred**: requires the learner to have built confidence in
writing code first. The read-the-code muscle is best trained after
~20 green exercises in the algorithmic track.

**Estimated effort**: 4-6 exercises + the `quarry.py` infrastructure.
~4 hours.

### 2.3 Write-the-tests exercise format

The inverse of the current format. The exercise gives the learner:

- A function signature and docstring.
- A problem statement in `prompt.md`.
- A reference `solution.py` (so the learner's tests have something
  to run against).

The learner writes `test_solution.py` from scratch. The test file
itself is graded (a hidden reference test set is run against the
learner's tests, and the learner's tests are run against known
correct and known-buggy reference solutions to score coverage and
false-positive rate).

**Why deferred**: same as 2.2. Also requires more infrastructure
than the read-the-code format (a way to grade tests, not just code).

**Estimated effort**: 4 exercises + grading infrastructure. ~5 hours.

### 2.4 Portfolio-piece checkpoints

Every ~15 green exercises, insert a "checkpoint" exercise that asks
the learner to build a small end-to-end thing:

- Logistic regression from scratch with toy 2-D data.
- A decision tree stub using only `02_collections` primitives.
- A softmax classifier on MNIST (no PyTorch — just numpy).
- A tiny bag-of-words text classifier.
- A beam-search decoder (5-10 lines, reusing the heap from ex16).

The output is a real artifact, useful for a portfolio later. Tests
assert it runs and produces sensible numbers (e.g. "loss decreases
over 100 steps", "accuracy > 80% on held-out test").

**Why deferred**: the learner has 0 green exercises in the new
algorithmic track so far. Way too early. Revisit after ex08 (or
earlier if the learner finishes fast).

**Estimated effort**: 1 checkpoint = 2-3 hours of scaffold and
test-writing. Plan 4-5 checkpoints across the whole course.

### 2.5 Before-you-start diagnostic

A 5-10 problem pre-test that tells a fresh learner where to start.
Each problem tags 1-2 strategies; the diagnostic maps strategy
coverage to a recommended starting exercise.

**Why deferred**: the learner has no CS background and explicitly said
linear 01 -> 02 -> 03 is fine for them right now. The diagnostic is
useful for *future* learners who pick up this course, not for the
current one.

**Estimated effort**: ~1 hour (5 problems + a scoring script).

### 2.6 Git cheatsheet was DEFERRED in the previous turn but is small

Earlier on 2026-06-02, the plan included creating
`notes/git_cheatsheet.md`. It was deferred in this session. It is
**small and useful** — a 1-2 page reference doc with the 8 commands
the learner will use 95% of the time (`init`, `add`, `commit`, `diff`,
`log`, `status`, `restore`, `branch`), the repo's commit-message
convention, and a "what NOT to do" section (no blind `git add .`).

**Estimated effort**: ~20 minutes.

**Recommendation**: do this one next. It is the lowest-effort deferred
item and the only one that does not require new exercise design.

---

## 3. Items explicitly rejected (do not re-propose)

### 3.1 Time-on-task tracking in `progress.json`

Proposed: per-exercise fields `attempts`, `time_minutes_approx`,
`opened_at`, `green_at`. The learner's habit-level insight from this
data would be huge (e.g. "you consistently take 25+ min on
sliding-window — that's a real gap, not noise").

**Rejected by learner on 2026-06-02**: "feels too much pressure".
The learner asked not to add it. **Do not re-propose.**

### 3.2 Ruff format mode

Proposed: also enable `ruff format` in addition to `ruff check`, run
via a pre-commit or editor save hook.

**Rejected by learner on 2026-06-02**: the learner wants lint only
(`ruff check`), no auto-format. **Do not re-propose.**

### 3.3 Re-summarising `due_utc` semantics

The learner raised a question about whether `review_queue[*].due_utc`
was a spaced-repetition schedule or a completion-date log. The data
shows it is a spaced-repetition schedule (field name + `reason:
"spaced_repetition"` + 1-3 day offsets from `completed_utc`). The
learner confirmed the spaced-repetition interpretation. **Do not
re-litigate.**

### 3.4 Resuming `03_ml_foundations`

The lesson is paused (the AI scaffolded 3 exercises in
`ex01_confusion_metrics`, `ex02_stratified_split`, `ex03_leakage_detection`
but the theory was too dense too fast). The learner did not ask to
resume it. The 3 pre-existing stub failures (13 tests) remain until
either (a) the lesson is resumed with a redesigned gentler ramp, or
(b) the lessons are removed entirely. **Do not extend
`03_ml_foundations` further without an explicit learner request.**

---

## 4. Open suggestions the learner wants to discuss (placeholder)

The learner said on 2026-06-02:

> "i do have some suggestions for the phase 5 file/stuff which we can
> discuss after u are done with the first 4 phases"

So this section is reserved for the learner's own suggestions. When
the learner comes back with their suggestions, list each one here as
a sub-section with:

- **What the suggestion is** (1-2 lines).
- **Status**: pending / accepted / rejected.
- **Notes** (any context or constraints).

Example format:

```
### 4.1 [Learner's suggestion title]
- **What**: (1-2 lines)
- **Status**: pending
- **Notes**: (constraints, related exercises, etc.)
```

---

## 5. How a future AI session should resume

When the next session opens:

1. Read `STRUCTURE.md` (orient on layout).
2. Read this file (`notes/future_plans.md`) — it tells you what was
   done last time and what is still open.
3. Read `progress.json` — read `cursor` to find the learner's
   position. The expected position is somewhere in
   `03_algorithmic_foundations/ex01_bsearch_index` through
   `ex16_top_k_streaming`, depending on how much the learner has
   done since 2026-06-02.
4. Read `notes/cheatsheet.md` and `notes/mistakes.md` to learn the
   learner's current style profile and recurring issues.
5. Read `notes/bug_log.md` to see the recent bug history. If the
   learner has been logging bugs, that is the right place to look
   for what to focus review on.
6. Apply the new contract: when a test fails, the learner has
   already written a `bug_log` entry. The AI must not provide a hint
   without that entry (or an explicit "skip the log for this one").
7. Apply the new contract: `pytest -q` AND `python tools/check_lint.py`
   must both be green before an exercise is considered done.
8. Generate the next exercise or apply the user's current request.

If a deferred item in section 2 is being acted on, move it to "done"
at the bottom of this file with the date and a one-line summary of
what was done. Do not leave it in section 2.

If a new deferred item is added (during this session), append it to
section 2 with the date and a one-paragraph description.

---

## 6. Done since 2026-06-02 (moved out of section 2)

### 6.1 — 2.6 Git cheatsheet (2026-06-02)

- **Status**: done.
- **File added**: `notes/git_cheatsheet.md`.
- **What was done**: 1-page reference doc with the 8 git commands
  the learner will use 95% of the time (`init`, `status`, `diff`,
  `add`, `commit`, `log`, `restore`, `branch`, plus the `remote` /
  `push` / `pull` triple), the repo's `<type>(<scope>): <subject>`
  commit-message convention with good/bad examples, and a "What
  NOT to do" section covering the 5 most common mistakes
  (`git add .` without checking status, committing broken tests,
  `commit --amend` after push, force-push to main, fighting
  line-ending warnings).
- **Why this is the right next step after 2.6**: 20 minutes of work
  for a durable reference the learner can keep open while doing
  the spaced-repetition review of `01_basics` and `02_collections`.

### 6.2 — 2.1 Numerical Python mini-track (2026-06-02, partial)

- **Status**: scaffolded (5 of 8-12 planned exercises done). Not
  fully done; the remaining 3-7 exercises are out of scope for the
  current session but the pattern is established.
- **Files added**:
  - `lessons/04_numerical_python/ex01_column_stats/` (4 files).
  - `lessons/04_numerical_python/ex02_subtract_row_mean/` (4 files).
  - `lessons/04_numerical_python/ex03_clip_outliers/` (4 files).
  - `lessons/04_numerical_python/ex04_logsumexp/` (4 files).
  - `lessons/04_numerical_python/ex05_softmax_rows/` (4 files).
  - Total: 20 new files.
- **Files edited**:
  - `progress.json`: added `04_numerical_python` to `lessons` and
    added a `scaffolding["04_numerical_python"]` block with
    pre-declared `strategies` for all 5 exercises. Schema still
    v1.0-compatible.
  - `STRUCTURE.md`: added `04 Numerical Python | ex01..ex05` row
    to the lesson-inventory table. Also fixed the existing row
    for `03 Algorithmic Foundations` (was `ex01..ex12`, now
    `ex01..ex16` to reflect the 4-extension exercises added on
    2026-06-02).
  - `STRUCTURE.md`: added new section (g), "Future exercise
    formats (deferred, see `notes/future_plans.md` §2)" that
    documents the 4 deferred formats (read-the-code, write-the-
    tests, portfolio checkpoint, before-you-start diagnostic) so
    a future AI session sees the format roadmap without having to
    re-read section 2 of this file.
- **Pattern established** (use this to add the remaining 3-7
  exercises):
  - **Topic 1 — vectorised reductions**: `ex01_column_stats`
    (axis reduction), future `ex06_*` (row-wise / column-wise
    `argmax`/`argsort`).
  - **Topic 2 — broadcasting**: `ex02_subtract_row_mean`
    (the `keepdims=True` shape dance), future `ex07_*`
    (outer product, einsum warmup).
  - **Topic 3 — boolean masking**: `ex03_clip_outliers`
    (`np.where` cascade), future `ex08_*` (vectorised "select and
    replace" by mask).
  - **Topic 4 — numerical stability**: `ex04_logsumexp`
    (max-subtraction trick).
  - **Topic 5 — softmax / cross-entropy**: `ex05_softmax_rows`
    (combines broadcasting + stability).
  - All 5 exercises follow the same template as the algorithmic
    track: `prompt.md` (with complexity requirement, disallowed
    examples, A/B examples, theory reference), `theory.md` (mental
    model + pitfalls + ML connection), `solution.py` (NotImplementedError
    stub), `test_solution.py` (AST-only constraint checks plus
    functional tests).
- **Final pytest + ruff state after this batch**:
  - `python -m pytest -q` — 251 failed, 195 passed. All 51 new
    failures are `NotImplementedError` stubs. ruff: All checks
    passed. check_lint.py: exit 0.

### 6.3 — 2.2, 2.3, 2.4, 2.5 still deferred (2026-06-02)

- **Status**: not done. The format documents are now in
  `STRUCTURE.md` section (g), but the actual exercise infrastructure
  (quarry.py format, hidden reference test set, portfolio
  publishing, diagnostic scoring) is still future work.
- **Revisit when**: 2.4 (portfolio checkpoint) is the most
  important — revisit after ~15 green exercises in
  `03_algorithmic_foundations`. 2.2 and 2.3 (read-the-code,
  write-the-tests) are nice-to-haves that can be done in any
  order. 2.5 (diagnostic) is for future learners.
