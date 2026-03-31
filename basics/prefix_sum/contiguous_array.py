"""
LC 525
Given a binary array `nums` containing only `0s` and `1s`, return the length of the longest contiguous subarray with an
equal number of 0s and 1s.

Input:  nums = [0, 0, 1, 0, 0, 0, 1, 1]
Output: 6

A[l..r] = P[r+1] - P[l] == 0 <==> P[r+1] == P[l]
"""
# nums = [0, 0, 1, 0, 0, 0, 1, 1]
# pref = [0, -1, -2, -1, -2, -3, -4, -3, -2]


def contiguous_array(nums: list[int]) -> int:
    longest = -1
    prefix = 0
    hash = {0: -1}
    nums = [-1 if x == 0 else x for x in nums]
    for i in range(len(nums)):
        prefix += nums[i]
        if prefix in hash:
            longest = max(longest, i - hash[prefix])
        if prefix not in hash:
            hash[prefix] = i

    return longest


print(contiguous_array([0, 0, 1, 0, 0, 0, 1, 1]))
