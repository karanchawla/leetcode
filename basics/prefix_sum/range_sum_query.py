"""
LC 303: Range sum query
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right
inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]
"""


class NumArray:
    def __init__(self, nums: list[int]):
        self.hash = {0: 0}  # sentinel
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            self.hash[i + 1] = prefix

    def sumRange(self, left: int, right: int) -> int:
        return self.hash[right + 1] - self.hash[left]
