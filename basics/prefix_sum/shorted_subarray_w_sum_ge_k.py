"""
862. Shortest Subarray with Sum at Least K

Given an integer array nums and an integer k, return the length of the shortest non-empty
subarray of nums with a sum of at least k. If there is no such subarray, return -1.

A subarray is a contiguous part of an array.
Example 1:

Input: nums = [1], k = 1
Output: 1
Example 2:

Input: nums = [1,2], k = 4
Output: -1
Example 3:

Input: nums = [2,-1,2], k = 3
Output: 3


Thought process:

BACK: among all future left boundaries, keep only
      candidates that could improve the answer
      → discard l1 when P[l2] <= P[l1] (l2 is shorter AND larger sum)

FRONT: for each right boundary r, extract the best
       left boundary it can pair with
       → once l satisfies the condition, its best match is found, discard it
"""

from collections import deque


class Solution:
    def shortestSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        prefix_sums = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sums[i] = prefix_sums[i - 1] + nums[i - 1]

        candidate_indices = deque()
        result = float("inf")

        for i in range(n + 1):
            while (
                candidate_indices
                and prefix_sums[i] - prefix_sums[candidate_indices[0]] >= k
            ):
                result = min(result, i - candidate_indices.popleft())

            while (
                candidate_indices
                and prefix_sums[i] <= prefix_sums[candidate_indices[-1]]
            ):
                candidate_indices.pop()

            candidate_indices.append(i)

        return result if result != float("inf") else -1
