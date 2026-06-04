# Architecture Notes — Problems & Solutions

## Problem 1: File Relations (Stale Documentation)

**When one file changes, the LLM doesn't know which other files must also be updated.**

This caused the audit to find 14 stale-doc issues — files that referenced old agent names, outdated permission models, or claimed `.opencode/` didn't exist. The agent logic was correct, but supporting docs were left behind.

### Solution: Dual-layer relation tracking

**Layer A — `FILE_RELATIONS.md` at repo root**

A one-pager listing every cross-file dependency. The LLM reads this before any edit.

```
coach.md → AGENTS.md (agents table)
         → STRUCTURE.md (if workflow changes)
         → skills/course-conventions/SKILL.md (workflow steps)

git-agent.md → AGENTS.md (add table row)
            → coach.md (add delegation + permission)

skills/* → coach.md (skills section)
         → COACH.md (if workflow rule changes)

progress-tracker.md → AGENTS.md (role description)
                    → coach.md (delegation map)

exercise-scaffolder.md → AGENTS.md (role description)
                       → coach.md (delegation map)
                       → skills/exercise-patterns/SKILL.md (reference)
```

**Layer B — `related:` field in YAML frontmatter of every `.opencode/` file**

```yaml
---
description: ...
related:
  - AGENTS.md
  - coach.md
  - skills/course-conventions/SKILL.md
---
```

Self-documenting per file. The LLM sees it when reading the file and knows what else to update.

**Fallback — `/verify-relations` command (optional)**

A subagent that cross-checks every agent/skill/command against documentation and reports what's stale. Run after any set of changes.

---

## Problem 2: Auto-Git Only at Cycle Boundaries

**Git-agent fires at coaching cycle boundaries (after progress-tracker, after scaffolder), but direct assistant edits (file deletes, config changes) have no automatic trigger.**

The audit deletion (`CHANGES.md` and `OPENCODE_CUSTOMIZATIONS.md`) was detected by git (`git status` showed deleted files) but never committed — the assistant forgot to fire git-agent because there was no coaching cycle involved.

### Solution: Hard rule in AGENTS.md

Add to `AGENTS.md` under the Hard Rules section:

```
6. After making ANY file change (edit, create, delete),
   immediately fire `git-agent` with message like
   `"auto: <short description>"`. Never leave uncommitted changes.
```

AGENTS.md is the orientation document the assistant re-reads at the start of every session. A hard rule there is structurally impossible to forget — it's re-read with every new conversation turn.

**Considered alternative:** Widening coach.md's trigger from "only after progress-tracker/scaffolder" to "after ANY subagent returns success". Rejected because it would fire git-agent after read-only operations (tester, reviewer), creating noisy empty commits.
