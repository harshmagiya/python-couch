# Git Cheatsheet (Learner Reference)

You will use git 95% of the time with 8 commands. Master these, leave the
rest for when you actually need them. **Do not memorise git — memorise
the workflow below and let git's error messages guide the rest.**

## Setup (once per machine)

```powershell
git config --global user.name  "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
git config --global core.autocrlf true   # Windows: convert line endings on checkout, not on commit
```

The repo is already a git repo with a remote at `origin/main`. The AI
coach auto-commits and pushes at each exercise boundary. If you want
to commit mid-session, use the commands below — otherwise the coach
handles it.

The `.gitignore` covers `__pycache__`, `.venv`, `.pytest_cache`,
`.claude/`, `.ruff_cache/`, and `NUL` artifacts, so you do not need
to write one.

## The 8 commands you will actually use

In rough order of how often you'll reach for them.

### 1. `git status` — what changed?

```powershell
git status
```

Run this **before every other git command**. It tells you which files
are untracked, modified, or staged. If the output is empty, you have
nothing to commit. Read it like a to-do list.

### 2. `git diff` — what did I change in the working tree?

```powershell
git diff                  # unstaged changes
git diff --staged         # staged changes (about to be committed)
```

`q` to exit the pager.

### 3. `git add` — stage specific files

```powershell
git add path/to/file.py
git add notes/cheatsheet.md
```

**Stage by name, not by wildcard.** `git add .` is fine once you have
checked `git status` and confirmed every listed file is intentional.
Until then, name each file. The "What NOT to do" section below has
more on this.

### 4. `git commit` — record a snapshot of staged changes

```powershell
git commit -m "Add ex07 sliding window: prompt + theory + 14 tests"
```

The `-m` flag is for a **one-line subject**. For longer messages,
drop `-m` and git will open your editor:

```powershell
git commit
# editor opens with:
#   <type>(<scope>): <subject>
#   <blank line>
#   <body explaining WHY, not WHAT>
#   <blank line>
#   <footer>
```

### 5. `git log` — see commit history

```powershell
git log                       # full
git log --oneline -20         # one-line, last 20
git log --oneline --graph     # branch visualisation
```

`q` to exit.

### 6. `git restore` — undo a working-tree change

```powershell
git restore path/to/file.py            # discard unstaged edits
git restore --staged path/to/file.py   # unstage (keeps the edit)
```

`git restore` is the **safe** undo. It does not touch commit history.

### 7. `git branch` — list / create / switch branches

```powershell
git branch                  # list local branches
git branch try-ex07         # create "try-ex07" branch (still on main)
git switch try-ex07         # move to it
git switch main             # back to main
git branch -d try-ex07      # delete the branch (safe: refuses if not merged)
```

A branch is a **named pointer to a commit**. Use one per exercise
attempt if you want to experiment without losing the working version:
branch off main, try stuff, throw the branch away or merge it back.

### 8. `git remote` + `git push` / `git pull` — sync with GitHub

```powershell
git remote add origin https://github.com/<you>/<repo>.git   # first time only
git push -u origin main                                     # first push
git push                # subsequent pushes
git pull                # fetch + merge
```

If you create a GitHub repo later, the repo's `Settings -> Pages` can
publish the lessons folder as a static site. That is a future item —
do not set it up today.

## Commit message convention (this repo)

```
<type>(<scope>): <subject>
```

- `type` is one of: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`.
- `scope` is the lesson or area: `01_basics`, `02_collections`,
  `03_algorithmic_foundations`, `coach`, `notes`, `meta`.
- `subject` is a **lowercase imperative** ("add", not "added" or
  "adds") and **does not end in a period**.

Examples (good):

```
feat(03_algorithmic_foundations): add ex07 longest substring no-repeat
fix(03_algorithmic_foundations): ex04 kadane: tighten off-by-one test for k=0
docs(notes): add patterns-practiced section to cheatsheet
chore(meta): bump schema_version to 1.1
refactor(coach): combine step 4 pytest + lint into one gate
```

Examples (bad):

```
updated stuff
ex07
fixed bug
WIP
```

The subject is what `git log --oneline` shows, so make it readable.

## What NOT to do

These are the mistakes that cost the most time. They are listed in
the order learners actually hit them.

### Don't `git add .` blindly

```powershell
git add .   # DON'T do this without first running `git status`
```

If you have a `__pycache__` folder, a `.env` with secrets, or a
random test file in the wrong folder, `git add .` will pick it up.
A "fix-secret-leak" commit afterwards is much harder than just
`git add path/to/specific/file.py` in the first place.

The right habit: run `git status`, read the list, `git add` only the
files you intend.

### Don't commit broken tests

The contract is "green before commit". If `pytest -q` and
`python tools/check_lint.py` are not both clean, **do not commit**.
WIP commits are fine on a throwaway branch; never on `main`.

### Don't `git commit --amend` after pushing

`--amend` rewrites history. If you have already pushed, it will
silently break the next person's `git pull`. Only use `--amend` on
commits that have **not** been pushed.

### Don't `git push --force` to "main"

Same reason. Force-pushes rewrite history and will trip up any
collaborator (including future-you on another machine). Force-push
is fine on your own throwaway branch.

### Don't fight line-ending warnings

On Windows you will sometimes see "LF will be replaced by CRLF" the
first time you `git add` a file. That is `core.autocrlf` doing its
job. The fix is the setup line at the top of this file, not a
hand-edit of every file.

## One-day reference workflow

```powershell
# 1. orient
cd "C:\Users\harsh\Desktop\projects\learning python"
git status

# 2. make changes
#    (edit solution.py, theory.md, etc.)

# 3. review
git status                    # what changed?
git diff                      # how exactly?

# 4. gate
pytest -q
python tools/check_lint.py

# 5. stage + commit
git add path/to/specific/file.py   # by name
git commit -m "feat(03_algorithmic_foundations): add ex07 solution"

# 6. push (if you have a remote)
git push
```

If any of the above fails, **read the error message**. Git's errors
are usually specific and tell you the next command to run. Do not
panic and `git reset --hard` — that is the most destructive undo
and the hardest to recover from.
