#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#
# https://leetcode.com/problems/distinct-subsequences/description/
#
# algorithms
# Hard (36.81%)
# Likes:    971
# Dislikes: 49
# Total Accepted:    124.6K
# Total Submissions: 338K
# Testcase Example:  '"rabbbit"\n"rabbit"'
#
# Given a string S and a string T, count the number of distinct subsequences of
# S which equals T.
# 
# A subsequence of a string is a new string which is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (ie, "ACE" is a
# subsequence of "ABCDE" while "AEC" is not).
# 
# Example 1:
# 
# 
# Input: S = "rabbbit", T = "rabbit"
# Output: 3
# Explanation:
# 
# As shown below, there are 3 ways you can generate "rabbit" from S.
# (The caret symbol ^ means the chosen letters)
# 
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
# 
# 
# Example 2:
# 
# 
# Input: S = "babgbag", T = "bag"
# Output: 5
# Explanation:
# 
# As shown below, there are 5 ways you can generate "bag" from S.
# (The caret symbol ^ means the chosen letters)
# 
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
# ⁠ ^  ^^
# babgbag
# ⁠   ^^^
# 
# 
#

# @lc code=start
from pprint import pprint
class Solution:
    # def numDistinct(self, s: str, t: str) -> int:
    def numDistinct(self, s, t):
        """
        backtrack TLE, use dp



        if t[i] == s[j]:
            dp[i+1][j+1] = dp[upper_left] + dp[left]
        else:
            dp[i+1][j+1] = dp[left]

             r a b b b i t
          [1,1,1,1,1,1,1,1]
        r [0,1,1,1,1,1,1,1]
        a [0,0,1,1,1,1,1,1]
        b [0,0,0,1,2,3,3,3]
        b [0,0,0,0,1,3,3,3]
        i [0,0,0,0,0,0,3,3]
        t [0,0,0,0,0,0,0,3]

        """
        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
        dp[0] = [1] * (len(s) + 1)
        for i in range(len(t)):
            for j in range(len(s)):
                if t[i] == s[j]:
                    dp[i+1][j+1] = dp[i][j] + dp[i+1][j]
                else:
                    dp[i+1][j+1] = dp[i+1][j]
        # pprint(dp)
        return dp[-1][-1]

# @lc code=end
