---
description: Reset context mid-session with a fresh orientation summary. Fires resumer for current state, completed exercises, overdue reviews, and recurring habits.
subtask: true
---

# /resume

Fire the `resumer` subagent immediately.

Ask resumer for:
- Active exercise and its status
- Last 3 completed exercises
- Any overdue review_queue entries
- Any open bug_log entries for the current exercise
- Top 2 recurring habits from mistakes.md

Present the summary to the learner in this format:

---
Active: <lesson>/<exercise> (<status>)
Last done: <ex1>, <ex2>, <ex3>
Overdue reviews: <list or none>
Open bug_log: <yes + one line / no>
Watch for: <habit 1>, <habit 2>
---

Then ask: "What would you like to work on?"

This command works at any point in a session — start, middle, or
when context is getting full. If context was filling up, treat
this summary as the new starting point for the session.
