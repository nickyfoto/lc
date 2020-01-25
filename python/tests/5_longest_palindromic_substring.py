#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (28.62%)
# Likes:    5282
# Dislikes: 454
# Total Accepted:    775.1K
# Total Submissions: 2.7M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#

# @lc code=start
from pprint import pprint
class Solution:
    def longestPalindrome2(self, s: str) -> str:
        def helper(s,l,r):
            while 0<=l and r < len(s) and s[l]==s[r]:
                    l-=1; r+=1
            return s[l+1:r]

        res = ""
        for i in range(len(s)):
            res = max(helper(s,i,i), helper(s,i,i+1), res, key=len)
        return res
       
    def longestPalindrome1(self, s: str) -> str:
        n = len(s)
        res = ""
        dp = [[False] * n for i in range(n)]
        print(dp)
        for i in range(n - 1, -1, -1):
            print(i)
            for j in range(i, n):
                print("i=", i, "j=", j)
                dp[i][j] = (s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1]))
                if dp[i][j] and (res == "" or j - i + 1 > len(res)):
                    res = s[i:j + 1]
        return res
      
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        # if n == 1:
            # return s
        if not s:
            return s
        res = s[0]
        dp = [[False] * n for i in range(n)]
        for l in range(n-1, -1, -1):
            for r in range(l, n):
                if l == r:
                    dp[l][r] = True
                elif r - l <= 2:
                    dp[l][r] = s[l] == s[r]
                if r - l > 2:
                    # print(l, r, dp[l+1][r-1], l+1,r-1)
                    dp[l][r] = (dp[l+1][r-1] and s[l] == s[r])
                if dp[l][r]:
                    # print(l, r, res, dp[l][r])
                    if r - l >= len(res):
                        res = s[l:r+1]
        # pprint(dp)
        return res
# @lc code=end
