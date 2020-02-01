#
# @lc app=leetcode id=1220 lang=python3
#
# [1220] Count Vowels Permutation
#
# https://leetcode.com/problems/count-vowels-permutation/description/
#
# algorithms
# Hard (51.88%)
# Likes:    91
# Dislikes: 29
# Total Accepted:    6.6K
# Total Submissions: 12.8K
# Testcase Example:  '1'
#
# Given an integer n, your task is to count how many strings of length n can be
# formed under the following rules:
# 
# 
# Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
# Each vowel 'a' may only be followed by an 'e'.
# Each vowel 'e' may only be followed by an 'a' or an 'i'.
# Each vowel 'i' may not be followed by another 'i'.
# Each vowel 'o' may only be followed by an 'i' or a 'u'.
# Each vowel 'u' may only be followed by an 'a'.
# 
# 
# Since the answer may be too large, return it modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: n = 1
# Output: 5
# Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
# 
# 
# Example 2:
# 
# 
# Input: n = 2
# Output: 10
# Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io",
# "iu", "oi", "ou" and "ua".
# 
# 
# Example 3: 
# 
# 
# Input: n = 5
# Output: 68
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 2 * 10^4
# 
# 
#

# @lc code=start

class Solution:
    # def countVowelPermutation(self, n: int) -> int:
    def countVowelPermutation(self, n):
        dp = [[0] * 5 for i in range(n + 1)]
        MOD = 10**9 + 7
        for i in range(5):
            dp[1][i] = 1
        for i in range(1, n):
            dp[i+1][0] = (dp[i][4] + dp[i][1] + dp[i][2]) % MOD
            dp[i+1][1] = (dp[i][0] + dp[i][2]) % MOD
            dp[i+1][2] = (dp[i][3] + dp[i][1]) % MOD
            dp[i+1][3] = (dp[i][2]) % MOD
            dp[i+1][4] = (dp[i][2] + dp[i][3]) % MOD
        
        ans = sum(dp[n][i] % MOD for i in range(5)) % MOD
            
        return ans
# @lc code=end
