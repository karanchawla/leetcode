"""
LC 1248
Given an array of integers nums and an integer k, return the number of contiguous subarrays that contain exactly k
odd numbers.

Input:  nums = [1, 1, 2, 1, 1], k = 3
Output: 2

Input:  nums = [2, 4, 6], k = 1
Output: 0

Input:  nums = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k = 2
Output: 16
"""


def nice_subarrays(nums: list[int], k: int) -> int:
    count = 0
    seen = {0: 1}
    prefix = 0
    nums = [0 if x % 2 == 0 else 1 for x in nums]
    for x in nums:
        prefix += x
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1
    return count


print(nice_subarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2))
