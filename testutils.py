"""Testing utilities.

This course repo uses many exercises with a shared file basename like
`test_solution.py` and `solution.py`. When running the entire test suite,
Python's normal import caching can cause module name collisions.

`load_solution()` imports the sibling `solution.py` via its file path and gives
it a unique module name, so each exercise test file always tests its own
solution.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path
from types import ModuleType


def load_solution(test_file: str, module_name: str | None = None) -> ModuleType:
    test_path = Path(test_file).resolve()
    solution_path = test_path.with_name("solution.py")

    if module_name is None:
        module_name = f"solution_{solution_path.parent.name}"

    spec = importlib.util.spec_from_file_location(module_name, solution_path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Could not load solution module from {solution_path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
