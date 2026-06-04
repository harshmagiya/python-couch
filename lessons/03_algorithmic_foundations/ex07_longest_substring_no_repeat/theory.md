# Variable Sliding Window: Longest Substring Without Repeats

## What problem this solves

Find the longest contiguous substring of `s` that contains no repeated character. The "no repeat" rule makes the window well-behaved: the moment you add a character that is already in the window, you must drop everything up to and including its previous occurrence from the *left* side.

## Mental model

A **variable-size sliding window** `[left, right]` that always contains a substring with no repeats. The right pointer scans the string one character at a time; the left pointer may jump forward when a repeat is found.

You also keep a `last_seen` dict: `last_seen[c]` is the most recent index where `c` appeared.

For each `right` from `0` to `len(s) - 1`:

1. If `s[right]` is in `last_seen` AND `last_seen[s[right]] >= left`, you have a repeat inside the current window. Jump `left` to `last_seen[s[right]] + 1`.
2. Record `last_seen[s[right]] = right`.
3. Update `best = max(best, right - left + 1)`.

After the loop, `best` is the answer.

## Why "jump `left` past the previous occurrence"

When a character `c` is about to enter the window at index `right` and we have seen `c` before at index `prev`, the new window cannot include `prev` (else the substring `[left, right]` has two `c`s). The shortest valid window starts at `max(left, prev + 1)`. Since `left` only moves forward, we can simply do `left = prev + 1` (we know `prev + 1 > left` whenever the condition `last_seen[c] >= left` holds; otherwise we don't move `left` at all).

## Why it matters in real projects

- The "longest substring with property P" pattern generalises to: longest substring with at most K distinct, longest substring with all vowels, longest palindromic substring (with a hashmap twist), and many log-anomaly detections.
- The O(n) total work — even though `left` can jump by more than one per step — is a key insight: the right pointer makes `n` steps, the left pointer also makes at most `n` steps, so the inner work is amortised O(1) per outer step.

## Common pitfalls

### Forgetting the `>= left` check

- You must only jump `left` if the previous occurrence is *inside* the current window. If it's *before* `left`, it doesn't conflict with the new character.

### Using a set instead of a last-seen dict

- A set tells you "is the character anywhere in `last_seen`" but not *where*. The whole point is to know the previous index, so you can jump `left` precisely.

### Resetting `left` to `right` on a repeat

- That's wrong; the window must start *after* the previous occurrence (`prev + 1`), not at the new character. A reset loses the characters between the previous occurrence and the new one.

### Counting characters that don't repeat in the BMP correctly

- A Python `str` is a sequence of code points, so a normal loop already counts Unicode characters correctly. But using `bytes(s, "utf-8")` would break this — don't.

## Edge cases

- Empty string.
- Single character.
- All same.
- All unique.
- Two adjacent repeats (`"abba"`): the second `'a'` jumps `left` past the first; the second `'b'` jumps `left` past the first `'b'`. Trace it on paper to convince yourself.
- Unicode (e.g. Greek, CJK, emoji).

## Quick check

`s = "abcabcbb"`.

- r=0 ('a'): last_seen empty. left=0, best=1. last_seen['a']=0.
- r=1 ('b'): not in window. left=0, best=2. last_seen['b']=1.
- r=2 ('c'): not in window. left=0, best=3. last_seen['c']=2.
- r=3 ('a'): 'a' at 0, 0 >= 0 -> left=1. best=3. last_seen['a']=3.
- r=4 ('b'): 'b' at 1, 1 >= 1 -> left=2. best=3. last_seen['b']=4.
- r=5 ('c'): 'c' at 2, 2 >= 2 -> left=3. best=3. last_seen['c']=5.
- r=6 ('b'): 'b' at 4, 4 >= 3 -> left=5. best=2. last_seen['b']=6.
- r=7 ('b'): 'b' at 6, 6 >= 5 -> left=7. best=1. last_seen['b']=7.

Return `3`. ✓

## ML/research connection

The variable-window + last-seen-index pattern is exactly how attention masks are constructed in transformers: for each query position, the valid key range is a window that depends on the previous key that "conflicts" with the current one, and the same jump-left-past-previous-occurrence rule applies. This is the foundational mental model for understanding sliding-window attention variants.
