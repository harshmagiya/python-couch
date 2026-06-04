# CHANGES.md — OpenCode Architecture Implementation

**Date:** 2026-06-04
**Author:** opencode agent
**Summary:** Initial implementation of OpenCode architecture for the Python course coaching workflow.

---

## What Was Added

### New directory: `.opencode/`

```
.opencode/
├── opencode.json                          ← config: sets coach as default agent
├── agents/
│   ├── coach.md                           ← primary orchestrator agent
│   ├── resumer.md                         ← file-reading proxy/assistant
│   ├── tester.md                          ← runs pytest + lint, explains failures
│   ├── hint-provider.md                   ← hints with bug-archaeology gate
│   ├── reviewer.md                        ← post-green rubric review
│   ├── exercise-scaffolder.md             ← creates new exercise folders (pre-existing, restored)
│   └── progress-tracker.md               ← sole write agent for state files
├── skills/
│   ├── course-conventions/SKILL.md        ← workflow rules on demand
│   ├── exercise-patterns/SKILL.md         ← exercise creation template
│   └── coaching/SKILL.md                 ← rubric + hint ladder rules
└── commands/
    ├── resume.md                          ← orient or reset mid-session
    └── coach-review.md                   ← trigger rubric review
```

### New file: `CHANGES.md` (this file)

---

## Detailed File Inventory

### 1. `.opencode/opencode.json`

**Purpose:** Project-level OpenCode configuration.

**Content:**
```json
{
  "$schema": "https://opencode.ai/config.json",
  "default_agent": "coach"
}
```

**Key design choices:**
- `$schema` enables IDE validation against OpenCode's published schema.
- `default_agent: "coach"` makes every new session in this repo open in coach mode automatically.
- No agent registration needed — OpenCode auto-discovers agents from `.opencode/agents/`.
- No skills registration needed — OpenCode auto-discovers skills from `.opencode/skills/`.
- No command registration needed — OpenCode auto-discovers commands from `.opencode/commands/`.

---

### 2. Agent Files (7 total)

All agents use YAML frontmatter with `description`, `mode`, and `permission` fields. The body is the agent's prompt/instructions.

#### 2.1 `.opencode/agents/coach.md`

**Role:** Primary orchestrator. The agent the learner talks to during every coaching session.

**Frontmatter:**
```yaml
description: Thin orchestrator for the Python course coaching workflow. Delegates file reading, testing, hints, reviews, scaffolding, and tracking to subagents. Never reads or writes files directly.
mode: primary
permission:
  edit: deny
  bash: deny
  task: allow
```

**Key design choices:**
- `mode: primary` — this is the default agent for new sessions.
- `task: allow` — coach must be able to invoke subagents (resumer, tester, hint-provider, reviewer, exercise-scaffolder, progress-tracker).
- `edit: deny` and `bash: deny` — coach never reads files or runs commands directly.
- Hard rules are in the prompt (re-read every generation), not in a skill (which could be forgotten if context fills past 50%).

#### 2.2 `.opencode/agents/resumer.md`

**Role:** Coach's permanent file-reading proxy. Reads state and exercise files, returns summaries only.

**Frontmatter:**
```yaml
description: Coach's file-reading proxy. Reads state and exercise files, returns summaries only. Never writes, never gives hints, never coaches.
mode: subagent
permission:
  edit: deny
  bash: deny
  task: deny
```

**Key design choices:**
- `task: deny` — resumer does not spawn further subagents.
- `edit: deny` and `bash: deny` — read-only proxy.
- Returns summaries in a fixed format for consistent orientation.

#### 2.3 `.opencode/agents/tester.md`

**Role:** Runs pytest and lint on the current exercise, explains failures in plain English.

**Frontmatter:**
```yaml
description: Runs pytest and lint on the current exercise and explains failures in plain English. Does not give hints or fixes.
mode: subagent
permission:
  edit: deny
  bash: allow
  task: deny
```

**Key design choices:**
- `bash: allow` — tester runs `pytest -q` and `python tools/check_lint.py`.
- Does not give hints — only diagnoses.
- Gets a fresh context window per invocation, so no state accumulation between exercises.

#### 2.4 `.opencode/agents/hint-provider.md`

**Role:** Gives hints after the bug-archaeology rule is satisfied.

**Frontmatter:**
```yaml
description: Gives hints after the bug-archaeology rule is satisfied. Enforces the bug-log gate at the agent level. Never gives solutions or code.
mode: subagent
permission:
  edit: deny
  bash: deny
  task: deny
```

**Key design choices:**
- Enforces bug-archaeology gate at the agent level (if no bug_log entry, returns a message telling coach to ask for one).
- Follows the 5-step hint ladder from the coaching skill.
- Never gives code, even as an example.

#### 2.5 `.opencode/agents/reviewer.md`

**Role:** Post-green rubric reviewer. Checks solution.py against the 7-point rubric.

**Frontmatter:**
```yaml
description: Post-green rubric reviewer. Checks solution.py against the 7-point rubric after all tests pass. Returns structured review with pass/note/refactor for each criterion.
mode: subagent
permission:
  edit: deny
  bash: deny
  task: deny
```

**Key design choices:**
- Loads the coaching skill for rubric details.
- Returns a structured review in a fixed format.
- Checks weakness_tags to see if any recurring habits appear in this solution.

#### 2.6 `.opencode/agents/exercise-scaffolder.md`

**Role:** Creates new exercise folders with all 4 required files. Pre-existing agent, restored after accidental deletion.

**Frontmatter:**
```yaml
description: Creates a complete 4-file exercise folder (prompt.md, theory.md, solution.py stub, test_solution.py with AST-only constraint checks) for a given topic, difficulty, and strategy list. Reads COACH.md and STRUCTURE.md conventions first.
mode: subagent
permission:
  task: deny
  bash: deny
  edit:
    "*": deny
    "lessons/**": allow
```

**Key design choices:**
- Reads COACH.md, STRUCTURE.md, and testutils.py directly for context.
- Follows a reference exercise for style consistency.
- Uses scoped edit permissions (only `lessons/**` allowed).
- AST-only constraint checks in test files (no runtime mocking).

#### 2.7 `.opencode/agents/progress-tracker.md`

**Role:** The sole write agent for progress.json and notes files.

**Frontmatter:**
```yaml
description: The sole write agent for progress.json and notes files. Called after a completed exercise (tests pass + review done). Writes to exactly 4 files and no others.
mode: subagent
permission:
  edit: allow
  bash: deny
  task: deny
```

**Key design choices:**
- `edit: allow` — but only for `progress.json`, `notes/cheatsheet.md`, `notes/mistakes.md`, `notes/bug_log.md`.
- Narrow file scope ensures if something goes wrong with writes, there's exactly one agent to debug.
- Updates all state files in a specific order: progress.json → mistakes.md → cheatsheet.md → bug_log.md.

---

### 3. Skill Files (3 total)

All skills use YAML frontmatter with `name` and `description` fields. The body is the skill's content.

#### 3.1 `.opencode/skills/course-conventions/SKILL.md`

**Purpose:** The essential operating rules from COACH.md, condensed to ~80 lines. Loaded by coach only when unsure about a workflow rule mid-session. Not loaded at startup.

**Frontmatter:**
```yaml
name: course-conventions
description: Use when coach needs to recall the exact workflow rules, bug-archaeology requirement, theory.md going-forward rule, and coaching contract from COACH.md. Do not load at startup.
```

**Content covers:**
- What this course is
- Tests are law
- Coaching contract (hints before code, no solution injection)
- Bug-archaeology rule
- theory.md going-forward rule
- Exercise workflow (5 steps)
- Exercise folder layout
- After green workflow

#### 3.2 `.opencode/skills/exercise-patterns/SKILL.md`

**Purpose:** The exact template for creating new exercises. Loaded by exercise-scaffolder before creating files, and by coach when briefing exercise-scaffolder on exercise format.

**Frontmatter:**
```yaml
name: exercise-patterns
description: Use when scaffolding a new exercise or briefing the exercise-scaffolder on exercise format. Contains the exact file templates for prompt.md, theory.md, solution.py, and test_solution.py.
```

**Content covers:**
- Naming convention
- prompt.md structure (task, signature, complexity, disallowed, constraints, hints)
- theory.md structure (mental model, why it matters, common pitfalls)
- solution.py structure (docstring, NotImplementedError stub)
- test_solution.py structure (constraint checks, functional tests, edge cases)

#### 3.3 `.opencode/skills/coaching/SKILL.md`

**Purpose:** The rubric and hint ladder rules. Loaded by reviewer and hint-provider. Not loaded by coach directly.

**Frontmatter:**
```yaml
name: coaching
description: Use when briefing the hint-provider or reviewer on rules, or when coach needs the rubric and hint ladder. Contains the 7-point rubric, scoring rules, hint ladder, and what counts as habit-level vs one-off.
```

**Content covers:**
- 7-point rubric (correctness, edge cases, naming/clarity, structure, data modeling, Pythonic usage, test-mindedness)
- Rubric scoring (PASS, NOTE, REFACTOR)
- Hint ladder (5 steps, never skip, never go to step 5 unless asked)
- What counts as habit-level vs one-off
- What coach must never do

---

### 4. Command Files (2 total)

Commands use YAML frontmatter with `description` and `mode` fields. The body is the command's prompt template.

#### 4.1 `.opencode/commands/resume.md`

**Purpose:** Works both at session start AND mid-session when context is getting full. Fires resumer for a fresh orientation summary.

**Frontmatter:**
```yaml
description: Reset context mid-session with a fresh orientation summary. Fires resumer for current state, completed exercises, overdue reviews, and recurring habits.
mode: subagent
```

**Content:** Instructions to fire resumer and present a formatted summary.

#### 4.2 `.opencode/commands/coach-review.md`

**Purpose:** Trigger a rubric review on the current exercise.

**Frontmatter:**
```yaml
description: Trigger a rubric review on the current exercise. Fires the reviewer subagent and presents the structured rubric result.
mode: subagent
```

**Content:** Instructions to load coaching skill, ask resumer for exercise name, fire reviewer, and present result.

---

## Corrections

After the initial implementation, the following corrections were made (2026-06-04):

- **Restored `exercise-scaffolder.md`**: This pre-existing agent was accidentally deleted. It was restored from the original content. It is more thorough than the initially created `scaffolder.md` — it reads COACH.md/STRUCTURE.md directly, follows a reference exercise, and includes AST-only constraint check patterns.
- **Deleted `scaffolder.md`**: The newly created version was redundant with the pre-existing `exercise-scaffolder.md` and less detailed.
- **Updated `coach.md`**: Delegation map and skills section now reference `exercise-scaffolder` instead of `scaffolder`.
- **Updated `CHANGES.md`**: All references to `scaffolder` updated to `exercise-scaffolder`.

---

## What Was NOT Changed

The following existing files were not modified:
- `COACH.md` — the contract is unchanged; the OpenCode architecture implements it.
- `STRUCTURE.md` — the file inventory is unchanged; `.opencode/` is a new addition.
- `rubric.md` — the rubric is unchanged; it's now loaded by the coaching skill.
- `pyproject.toml` — pytest config is unchanged; tester uses the same commands.
- `testutils.py` — unchanged; exercises continue to use `load_solution()`.
- All `lessons/` content — unchanged; exercises are untouched.
- All `notes/` content — unchanged; state files are read/written by the new agents.
- `.gitignore` — unchanged; `.opencode/` is not excluded (it's part of the project).

---

## Architecture Decisions

### 1. Why hard rules are in coach.md prompt, not in a skill

Skills can be forgotten if context fills past 50%. Prompt instructions are re-read with every single token generation — structurally impossible to forget. The 5 hard rules are invariant behavioral constraints that must never be violated, so they belong in the prompt itself.

### 2. Why coach.md doesn't read files directly

Coach never reads files so its context stays lean across a long session. Every time coach needs to know anything about the repo state, exercise content, or learner history, it asks resumer. Resumer reads the files, summarizes the relevant parts, and returns only what coach asked for. This keeps coach's context clean because resumer's reads happen in resumer's own context, and only the summary crosses back to coach.

### 3. Why tester/reviewer/hint-provider each get fresh context windows

Each gets a fresh context window per invocation, so they will never accumulate state between exercises. This prevents a long debug loop from filling up coach's context.

### 4. Why progress-tracker is the sole write agent

Write bugs corrupt progress.json. Only progress-tracker can write, with a narrow file scope. If something goes wrong with file writes, there is exactly one agent to debug.

### 5. Why commands are separate .md files

OpenCode supports both JSON (in opencode.json) and markdown files (in .opencode/commands/) for commands. The file-based format is chosen for maintainability — each command's prompt template is a separate readable file rather than an inline JSON string.

### 6. Why skills have explicit frontmatter

OpenCode's skill loader requires `name` and `description` fields in YAML frontmatter. Skills without these are filtered out and never surfaced to the model.

---

## Usage

### Starting a session

1. Open OpenCode in this repo directory.
2. Coach is automatically selected as the default agent.
3. Coach asks resumer for orientation.
4. Coach presents a 3-line summary.
5. Learner says "let's go" or types `/resume` for full orient.

### Exercise loop

1. Learner reads prompt.md and theory.md.
2. Learner implements solution.py.
3. Learner says "I think it's ready" → coach fires tester.
4. On fail: coach checks for bug_log entry → if yes, fires hint-provider.
5. On pass: coach fires reviewer → shows rubric result → fires progress-tracker → fires exercise-scaffolder.

### Context filling up mid-session

1. Learner types `/resume`.
2. Resumer reads state files, returns 20-line summary.
3. Coach treats this as the new session baseline.

---

## Verification

After restarting OpenCode in this repo:
1. Verify coach is selected as default agent.
2. Verify `/resume` command is available.
3. Verify `/coach-review` command is available.
4. Test the exercise loop with a sample exercise.
