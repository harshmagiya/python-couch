---
description: Trigger a rubric review on the current exercise. Fires the reviewer subagent and presents the structured rubric result.
subtask: true
---

# /coach-review

Load the `coaching` skill.
Ask resumer for the current exercise name and path.
Fire the `reviewer` subagent on the current exercise.
Present the structured rubric result to the learner.
If REFACTOR is flagged, ask the learner if they want to fix it now.
Do not propose fixes. Do not write code.
