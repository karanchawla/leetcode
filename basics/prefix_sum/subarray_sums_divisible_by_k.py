"""
Given an integer array `nums` and an integer `k`, return the number of contiguous subarrays whose sum is divisible by k.
Example 1
Input: nums = [4, 5, 0, -2, -3, 1], k = 5
Output: 7

Input: nums = [5], k = 5
Output: 1

A[l..r] % k == 0 <==> (P[r + 1] - P[l]) % k == 0 <==> P[r+1] % k == P[l] % k

"""


def subarray_sum_divisible_by_k(nums: list[int], k: int) -> int:
    count = 0
    seen = {0: 1}
    prefix = 0
    for x in nums:
        prefix += x
        # remainder = ((prefix % k) + k) % k in C++/Java for handling negative numbers
        count += seen.get(prefix % k, 0)
        seen[prefix % k] = seen.get(prefix % k, 0) + 1

    return count
