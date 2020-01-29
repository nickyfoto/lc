#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (39.90%)
# Likes:    954
# Dislikes: 51
# Total Accepted:    72.8K
# Total Submissions: 182.5K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# Given two strings s1 and s2, write a function to return true if s2 contains
# the permutation of s1. In other words, one of the first string's permutations
# is the substring of the second string.
# 
# 
# 
# Example 1:
# 
# 
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
# 
# 
# Example 2:
# 
# 
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
# 
# 
# 
# 
# Note:
# 
# 
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].
# 
# 
#

# @lc code=start
from collections import Counter
from string import ascii_lowercase
class Solution:
    def checkInclusion_me(self, s1: str, s2: str) -> bool:
        c = Counter(s1)
        r = len(s1)
        d = Counter(s2[:r])
        l = 0
        while r <= len(s2):
            if d == c:
                return True
            d[s2[l]] -= 1
            if d[s2[l]] == 0:
                del d[s2[l]]
            if r < len(s2):
                if s2[r] in d:
                    d[s2[r]] += 1
                else:
                    d[s2[r]] = 1
            l += 1
            r += 1
        return False

    def checkInclusion(self, s1: str, s2: str) -> bool:
        c = {l: 0 for l in ascii_lowercase}
        c.update(Counter(s1))
        # print(c)
        r = len(s1)
        d = {l: 0 for l in ascii_lowercase}
        d.update(Counter(s2[:r]))
        cnt = sum(c[k] == d[k] for k in c)
        # print(cnt)
        l = 0
        while r <= len(s2):
            if cnt == 26:
                return True
            if d[s2[l]] == c[s2[l]]:
                cnt -= 1
            d[s2[l]] -= 1
            if d[s2[l]] == c[s2[l]]:
                cnt += 1
            
            if r < len(s2):
                if d[s2[r]] == c[s2[r]]:
                    cnt -= 1
                d[s2[r]] += 1
                if d[s2[r]] == c[s2[r]]:
                    cnt += 1
            l += 1
            r += 1
        return False
# @lc code=end
