#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (28.86%)
# Total Accepted:    1.1M
# Total Submissions: 3.8M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 
# 
# 
# 
# Example 2:
# 
# 
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# 
# Example 3:
# 
# 
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3. 
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
# 
# 
# 
# 
# 
#

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        old
        """
        if not s:
            return 0
        n = len(s)
        L = [1] * n #longest no repeating substring starting from i
        d = {s[0]:0}
        for i, c in enumerate(s):
            if i != 0:
                if c not in d:
                    L[i] = L[i-1] + 1
                    d[c] = i
                else:
                    # print(d, i, s[i], d[c])
                    L[i] = i - d[c]
                    if len(d) > i - d[c]:
                        # print('i-d[c]=', i-d[c])
                        dc = d.copy()
                        for k,v in d.items():
                            if v <= d[c]:
                                del dc[k]
                        d = dc
                    d[c] = i
                    # print(d, L)

        # print(L)
        return max(L)

    def lengthOfLongestSubstring(self, s):
        n = len(s)
        dp = [1] * n
        pos = {}
        lst = []
        res = 0
        for i, c in enumerate(s):
            if i > 0:
                if c in lst:
                    dp[i] = i - pos[c]
                    if dp[i] == 1: lst = []
                    else: lst = lst[-(dp[i] - 1):]
                else:
                    dp[i] += dp[i - 1]
            lst.append(c)  
            pos[c] = i
            res = max(dp[i], res)
        return res

    def lengthOfLongestSubstring(self, s):
        """
        start represent the starting idx
        satisfy the constrain
        """
        d = {}
        res = start = 0
        for i, c in enumerate(s):
            if c in d:
                start = max(start, d[c] + 1)
            res = max(res, i - start + 1)
            d[c] = i
        return res
