# Verification Prompt — Comprehensive State Checker

Read-only verification across 6 categories. Run this against the repo to find inconsistencies, stale docs, permission drift, and flow gaps.

## 1. Agent Inventory

- List all `.md` files in `.opencode/agents/`
- Count them
- Open `AGENTS.md` — does the agents table match the count?
- Are all agent names identical between the table and the filenames?
- Is every name in `coach.md`'s `permission.task` map also a real file?
- Are there any agent files not referenced in `coach.md`'s task map?

## 2. Permission Audit

- Read every agent file's frontmatter
- Flag any agent with `bash: allow` that is NOT tester or git-agent
- Flag any agent with `edit: allow` that has no scope restriction
- Flag any agent with `task: allow` that is NOT coach
- Verify coach's task map has `"*": deny` as the catch-all
- Verify tester has `edit: deny`
- Verify git-agent has `edit: deny` and `task: deny`
- Verify resumer has `edit: deny`, `bash: deny`, `task: deny`

## 3. Skill Inventory

- List all directories under `.opencode/skills/`
- For each, read `SKILL.md` frontmatter — does `name` match the directory?
- Does `description` exist?
- Are skills referenced in `coach.md`'s SKILLS section present on disk?
- Search all skill files for outdated agent names: `"scaffolder"` (should be `"exercise-scaffolder"`), old agent names, old file paths.

## 4. Command Inventory

- List all files in `.opencode/commands/`
- For each, check frontmatter has `description` + `subtask: true`
- Flag any with `mode: subagent` (should be `subtask: true`)
- Are commands referenced in `AGENTS.md` or `coach.md` present on disk?

## 5. Documentation vs Reality

- `AGENTS.md` — does the workflow section match `coach.md`'s DELEGATION MAP?
- `COACH.md` — does the exercise workflow (steps 4-9) include auto-commit?
- `STRUCTURE.md` — does section (e) still claim `.opencode/` doesn't exist?
- `notes/git_cheatsheet.md` — does it still say "not a git repo"?
- `LEARNER_GUIDE.md` — does post-green section mention auto-commit?

## 6. Delegation Flow

- Trace the exercise loop: coach → tester → reviewer → progress-tracker → git-agent → exercise-scaffolder → git-agent
- Are there any cycles (A calls B calls A)?
- Are there any dead ends (agent returns but coach has no next step)?
- Is every subagent's `mode: subagent` correct?
- Does any agent call a subagent that doesn't exist in coach's task map?

## Report Format

```
Category: <name>
  CHECK: <description>
  RESULT: PASS | FAIL | WARN
  DETAIL: <one-line explanation if FAIL or WARN>
---
```

End with an overall verdict: **PASS** (all checks green), **MINOR** (only WARNs), or **FAIL** (any FAIL).
