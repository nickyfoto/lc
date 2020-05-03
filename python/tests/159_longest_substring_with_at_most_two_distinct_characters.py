#
# @lc app=leetcode id=159 lang=python3
#
# [159] Longest Substring with At Most Two Distinct Characters
#
# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/description/
#
# algorithms
# Medium (48.73%)
# Likes:    826
# Dislikes: 16
# Total Accepted:    100.5K
# Total Submissions: 206.3K
# Testcase Example:  '"eceba"'
#
# Given a string s , find the length of the longest substring t  that contains
# at most 2 distinct characters.
# 
# Example 1:
# 
# 
# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.
# 
# 
# Example 2:
# 
# 
# Input: "ccaabbb"
# Output: 5
# Explanation: t is "aabbb" which its length is 5.
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    # def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        my solution
        """
        start = 0
        d = defaultdict(int)
        res = 0
        for i, c in enumerate(s):
            d[c] += 1
            if len(d) <= 2:
                res = max(res, i - start + 1)
            else:
                j = start
                for j in range(start, i + 1):
                    d[s[j]] -= 1
                    if d[s[j]] == 0:
                        del d[s[j]]
                        break
                start = j + 1
        return res
                
# @lc code=end
