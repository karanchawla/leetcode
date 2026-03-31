"""
560. Subarray Sum Equals K

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""


def subarraySum(nums: list[int], k: int) -> int:
    count = 0
    seen = {0: 1}
    prefix = 0

    for x in nums:
        prefix += x
        count += seen.get(prefix - k, 0)
        seen[prefix] = seen.get(prefix, 0) + 1

    return count
