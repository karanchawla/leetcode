"""
3: Longest Substring Without Repeating Characters

Given a string s, find the length of the longest substring without duplicate characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        left = 0
        right = 0
        chars = Counter()
        for right in range(len(s)):
            chars[s[right]] += 1
            while chars[s[right]] > 1:
                chars[s[left]] -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
