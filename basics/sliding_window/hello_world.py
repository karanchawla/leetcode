"""
Given an array of integers and a number k, find the maximum sum of any contiguous subarray of length exactly k.
"""


def solution(nums: list[int], k: int) -> int:
    left = 0
    right = 1
    curr_sum = nums[left]
    while right < k:
        curr_sum += nums[right]
        right += 1

    # left = 0
    # right = k
    max_sum = curr_sum
    while right < len(nums):
        # maintain window size of k
        curr_sum = curr_sum - nums[left] + nums[right]
        max_sum = max(max_sum, curr_sum)
        left += 1
        right += 1

    return int(max_sum)
