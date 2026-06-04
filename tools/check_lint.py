"""Lint gate for the course.

Runs `ruff check .` against the repo and propagates the exit code.
A failing lint is treated the same as a failing test: fix the code, do
not disable the rule. Per COACH.md, the workflow is:

    pytest -q
    python tools/check_lint.py

Both must be green before an exercise is considered done.

Why a separate script (not in pytest): pyproject.toml's `testpaths` is
`["lessons"]` and we don't want to break that scope. Keeping the lint
gate as its own command also makes it clear in the workflow that lint
is a separate, equally-mandatory check.
"""

from __future__ import annotations

import subprocess
import sys


def main() -> int:
    result = subprocess.run(
        [sys.executable, "-m", "ruff", "check", "."],
        check=False,
    )
    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
