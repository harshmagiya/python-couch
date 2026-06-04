# ex07_longest_substring_no_repeat

Read: `theory.md` (2-3 minutes) before coding.

## Task

In `solution.py`, implement:

```python
def longest_substring_no_repeat(s: str) -> int:
    ...
```

Behavior:

- Return the length of the longest contiguous substring of `s` that
  contains no repeated character.
- "Repeated" means the same character appearing twice anywhere in the
  substring. Position does not matter — even `'a'` at index 1 and
  `'a'` at index 5 count as a repeat.
- Comparison must be character-based, not byte-based. Unicode characters
  above the BMP (e.g. emoji or CJK extensions) count as a single character.

## Examples

- `longest_substring_no_repeat("abcabcbb") == 3`   (e.g. "abc", "bca", "cab")
- `longest_substring_no_repeat("bbbbb") == 1`      (any single 'b')
- `longest_substring_no_repeat("pwwkew") == 3`     (e.g. "wke")
- `longest_substring_no_repeat("") == 0`
- `longest_substring_no_repeat("abcdef") == 6`     (all unique)
- `longest_substring_no_repeat("abba") == 2`       (e.g. "ab" or "ba")
- `longest_substring_no_repeat("dvdf") == 3`       (e.g. "vdf")
- `longest_substring_no_repeat("αβγαβγ") == 3`     (e.g. "αβγ")
- `longest_substring_no_repeat("🎉🎊🎉") == 2`     (two distinct emoji)

## Complexity requirement

- O(n) time.
- O(min(n, alphabet_size)) extra space (a dict tracking the last index
  of each character we have seen is fine).

## Constraints (for practice)

- No nested loop that, for each `left`, scans forward to find the first
  repeat (that would be O(n^2)).
- The window's `left` pointer must only ever move *right* (forward),
  never backward.

## Disallowed examples

```python
best = 0
for i in range(len(s)):                          # WRONG: O(n^2) outer / inner scan
    seen = set()
    for j in range(i, len(s)):
        if s[j] in seen:
            break
        seen.add(s[j])
    best = max(best, j - i)
return best
```

```python
return max(len(set(s[i:j])) for i in range(len(s)) for j in range(i + 1, len(s) + 1))  # WRONG
```
