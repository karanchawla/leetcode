"""
LC 340: Longest Substring with At Most K Distinct Characters

Given a string s and an integer k, return the length of the longest substring of s that
contains at most k distinct characters.

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.

"""

from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        longest = float("-inf")
        left = 0
        window = defaultdict(int)

        for right in range(len(s)):
            window[s[right]] += 1
            while len(window) > k:
                window[s[left]] -= 1
                if not window[s[left]]:
                    del window[s[left]]
                left += 1
            longest = max(longest, right - left + 1)
        return longest
