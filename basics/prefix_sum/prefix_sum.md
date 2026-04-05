# Prefix Sum: Complete Pattern Reference

## The Foundation

```
P[0] = 0
P[i] = A[0] + A[1] + ... + A[i-1]
sum(A[l..r]) = P[r+1] - P[l]
```

**Always use 1-indexed P.** `P[-1]` doesn't exist — the +1 offset eliminates the entire class of boundary bugs. The sentinel is just `P[0] = 0` made explicit in the hash map before the loop.

---

## The Two Independent Operations

Every single prefix sum hash map problem has these as **separate, independent if statements**:

```python
# 1. Lookup
if condition on seen:
    update answer

# 2. Insert
if/always:
    update seen
```

Coupling them with `if/else` is the single most common bug across all problems in this pattern. Never do it.

---

## Update Rule By Goal

| Goal | Update rule | Reason |
|---|---|---|
| Count subarrays | Always increment frequency | Every occurrence is a valid left boundary |
| Longest / min-length subarray | Only insert if absent | Earliest index maximizes the gap |
| Max/min sum subarray | Always update with running min/max | Optimal value may appear at any index |

---

## Hash Map Semantics By Problem Type

| Problem Type | Key | Value | Sentinel |
|---|---|---|---|
| Exact sum = k | `prefix` | frequency | `{0: 1}` |
| Sum divisible by k | `prefix % k` | frequency | `{0: 1}` |
| Longest subarray, sum = k | `prefix` | first index | `{0: -1}` |
| Longest balanced binary | `prefix` (0→-1 transform) | first index | `{0: -1}` |
| Min length, sum ≥ k (pos. only) | — | — | sliding window |
| Max sum, length div. by k | `prefix % k` | running minimum prefix | `{0: 0}` |
| Count subarrays, k odds | `prefix` (odd→1, even→0) | frequency | `{0: 1}` |
| Good subarray, sum div. k, len ≥ 2 | `prefix % k` | first index | `{0: -1}` |

---

## Transformations

Several problems are disguised versions of simpler ones:

```
0s and 1s, equal count     → replace 0 with -1, target sum = 0
k odd numbers              → replace odd with 1, even with 0, target sum = k
non-zero digit concat      → prefix concatenation with alignment shift
```

When you see a binary array or a property that partitions elements into two classes, immediately ask: *what transformation reduces this to a sum problem?*

---

## When Prefix Sum vs Sliding Window

| Condition | Approach |
|---|---|
| Negative numbers, exact sum | Prefix sum + hash map |
| All positive, sum ≥ k, minimize length | Sliding window O(n) |
| All positive, sum ≥ k (general) | Prefix sum + binary search O(n log n) |
| Negative numbers, sum ≥ k, minimize length | Prefix sum + monotonic deque O(n) |

**Key signal:** if the problem says "positive integers" and asks for a length condition, sliding window is likely optimal. If negatives are possible, you're forced into prefix sum territory.

---

## Modular Arithmetic Gotcha

Python's `%` always returns non-negative. C++/Java don't guarantee this.

```python
# Safe in any language:
remainder = ((prefix % k) + k) % k
```

---

## 2D Prefix Sums

```python
# Build (1-indexed)
P[i][j] = M[i-1][j-1] + P[i-1][j] + P[i][j-1] - P[i-1][j-1]

# Query (r1,c1) to (r2,c2) — 0-indexed input
P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]
```

Don't memorize the query formula. Re-derive it every time from inclusion-exclusion:

```
start with full rectangle → subtract top strip → subtract left strip → add back top-left corner (subtracted twice)
```

The anchor rule: `M[r][c]` lives at `P[r+1][c+1]`. Everything else follows.

---

## Problem Pattern Map

```
Count subarrays, sum = k, any integers
    → prefix + hash map, lookup (prefix - k)

Count subarrays, sum divisible by k
    → prefix % k as key, lookup current remainder

Longest subarray, sum = k
    → prefix + hash map, first occurrence, sentinel {0:-1}

Longest balanced binary array
    → 0→-1 transform, longest subarray sum = 0

Count subarrays, exactly k odds
    → odd→1 even→0 transform, count subarrays sum = k

Good subarray, sum divisible by k, length ≥ 2
    → prefix % k as key, first occurrence, check gap ≥ 2

Max subarray sum, length divisible by k
    → prefix % k as key, store running minimum prefix

Non-zero digit concatenation queries
    → prefix concatenation, alignment shift: concat_r - concat_l * 10^count

Minimum length subarray, sum ≥ k, positive integers
    → sliding window O(n) or prefix + binary search O(n log n)
```

---

## The One Paragraph To Remember

Prefix sum converts range queries into subtractions. The hash map lets you find valid left boundaries in O(1). The sentinel seeds `P[0] = 0` before the loop so subarrays starting at index 0 are visible. Lookup before insert so length-0 subarrays don't self-match. First-occurrence-only when maximizing a gap. Modular arithmetic when divisibility is involved. Sliding window only when all elements are positive and the problem has monotonicity. Everything else is a transformation to reduce to one of these cases.
