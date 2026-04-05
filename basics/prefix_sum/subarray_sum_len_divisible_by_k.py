"""
3381: Maximum Subarray Sum With Length Divisible by K

You are given an array of integers nums and an integer k.
Return the maximum sum of a subarray of nums, such that the size of the subarray is divisible by k.

Example 1:
Input: nums = [1,2], k = 1
Output: 3
Explanation:
The subarray [1, 2] with sum 3 has length equal to 2 which is divisible by 1.

Example 2:
Input: nums = [-1,-2,-3,-4,-5], k = 4
Output: -10
Explanation:
The maximum sum subarray is [-1, -2, -3, -4] which has length equal to 4 which is divisible by 4.
"""


def maxSubArraySum(nums: list[int], k: int) -> int:
    max_sum = float("-inf")
    table = {0: 0}
    prefix = 0
    for i in range(len(nums)):
        prefix += nums[i]
        if (i + 1) % k in table:
            max_sum = max(max_sum, prefix - table[(i + 1) % k])
            table[(i + 1) % k] = min(table[(i + 1) % k], prefix)
        else:
            table[(i + 1) % k] = prefix
    return int(max_sum)
