---
name: exercise-patterns
description: Use when scaffolding a new exercise or briefing the scaffolder on exercise format. Contains the exact file templates for prompt.md, theory.md, solution.py, and test_solution.py.
---

# Exercise Patterns

## Naming convention
exercises: ex<nn>_<snake_case_description>
lessons:   <nn>_<topic_name>
nn is zero-padded: ex01, ex02, ... ex12

## prompt.md structure
# <ExerciseName>

## Task
<1-2 sentence description of what to implement>

## Function signature
```python
def function_name(param: type) -> return_type:
```

## Complexity requirement
Must be O(<complexity>). Example: O(n), O(log n), O(n log n).

## Disallowed
The following are not allowed:
- <builtin or module> — example of disallowed: `bisect.bisect_left(arr, x)`
- Allowed alternative: implement the binary search loop manually

## Constraints
- <constraint 1 with A/B example>
- <constraint 2 with A/B example>

## Hints (only read if stuck)
- Hint 1: <directional, not a solution>
- Hint 2: <more specific if hint 1 not enough>

## theory.md structure
# Theory: <TopicName>

## Mental model
<2-3 sentences explaining the core idea>

## Why this matters
<1-2 sentences on real-world relevance>

## Common pitfalls
- <pitfall 1>
- <pitfall 2>

## solution.py structure
```python
"""
<ExerciseName>

<one-line description of what to implement>
"""


def function_name(param: type) -> return_type:
    """
    <Docstring repeating the task and return value>
    """
    raise NotImplementedError
```

## test_solution.py structure
Tests must include:
1. Constraint enforcement tests (AST check or monkeypatch for disallowed builtins)
2. Basic functional test (happy path)
3. Edge case: empty input
4. Edge case: single element
5. Edge case specific to the algorithm (e.g. all duplicates, negative numbers)
6. At least one test with the exact complexity requirement in mind
