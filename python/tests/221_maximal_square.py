#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
# https://leetcode.com/problems/maximal-square/description/
#
# algorithms
# Medium (35.20%)
# Likes:    2129
# Dislikes: 54
# Total Accepted:    184.5K
# Total Submissions: 522.9K
# Testcase Example:  '[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]'
#
# Given a 2D binary matrix filled with 0's and 1's, find the largest square
# containing only 1's and return its area.
# 
# Example:
# 
# 
# Input: 
# 
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# 
# Output: 4
# 
#

# @lc code=start
class Solution:
    # def maximalSquare(self, matrix: List[List[str]]) -> int:
    def maximalSquare(self, matrix):
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        mx = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    mx = max(dp[i][j], mx)
        return mx * mx
# @lc code=end
