"""
1004. Max Consecutive Ones III
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array
if you can flip at most k 0's.

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""


class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        max_ones = 0
        left = 0
        num_zeros = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                num_zeros += 1

            while num_zeros > k:
                if nums[left] == 0:
                    num_zeros -= 1
                left += 1

            max_ones = max(max_ones, right - left + 1)

        return max_ones
