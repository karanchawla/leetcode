"""
# 523. Continuous Subarray Sum
Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k.
"""


class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        # P[l..r] = (A[r+1] - A[l]) % k == 0; (r + 1 - l) >=2
        # A[r + 1] % k == A[l] % k where (r + 1 - l) >= 2
        seen = {0: -1}
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            r = prefix % k
            if r in seen and i - seen[r] >= 2:
                return True
            # IMPORTANT: Maximize length so we want to add the earliest seen remainder here
            if r not in seen:
                seen[r] = i
        return False
