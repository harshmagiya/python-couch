# ex02_word_frequencies

Implement a word-frequency counter.

## Task

In `solution.py`, implement:

```python
def word_frequencies(text: str) -> dict[str, int]:
    ...
```

Behavior:

- Return a dictionary mapping each word to its count.
- Words are case-insensitive (treat "Python" and "python" as the same word).
- Treat any whitespace (spaces/tabs/newlines) as separators.
- Ignore the punctuation characters: `.,;:!?"'()[]` (remove them).

Notes:

- If `text` has no words, return `{}`.
- Do not use third-party libraries.

## Examples

- `word_frequencies("Hi hi")` -> `{"hi": 2}`
- `word_frequencies("Python, python! PYTHON?")` -> `{"python": 3}`
- `word_frequencies("\t a\nA  b  ")` -> `{"a": 2, "b": 1}`

## Constraints (for practice)

- Do not use `collections.Counter` in this exercise.
