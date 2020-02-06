#
# @lc app=leetcode id=329 lang=python3
#
# [329] Longest Increasing Path in a Matrix
#
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
#
# algorithms
# Hard (42.02%)
# Likes:    1457
# Dislikes: 24
# Total Accepted:    119.8K
# Total Submissions: 285.2K
# Testcase Example:  '[[9,9,4],[6,6,8],[2,1,1]]'
#
# Given an integer matrix, find the length of the longest increasing path.
# 
# From each cell, you can either move to four directions: left, right, up or
# down. You may NOT move diagonally or move outside of the boundary (i.e.
# wrap-around is not allowed).
# 
# Example 1:
# 
# 
# Input: nums = 
# [
# ⁠ [9,9,4],
# ⁠ [6,6,8],
# ⁠ [2,1,1]
# ] 
# Output: 4 
# Explanation: The longest increasing path is [1, 2, 6, 9].
# 
# 
# Example 2:
# 
# 
# Input: nums = 
# [
# ⁠ [3,4,5],
# ⁠ [3,2,6],
# ⁠ [2,2,1]
# ] 
# Output: 4 
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally
# is not allowed.
# 
# 
#

# @lc code=start
class Solution:
    # def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    def longestIncreasingPath(self, matrix):
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for i in range(m)]

        def dfs(r, c):
            if dp[r][c] != 0: return dp[r][c]
            val = matrix[r][c]
            res = 0
            if r > 0 and matrix[r - 1][c] > val:
                res = max(res, dfs(r - 1, c)) # up
            if r < m - 1 and matrix[r + 1][c] > val:
                res = max(res, dfs(r + 1, c)) # down
            if c > 0 and matrix[r][c - 1] > val:
                res = max(res, dfs(r, c - 1)) # left
            if c < n - 1 and matrix[r][c + 1] > val:
                res = max(res, dfs(r, c + 1)) # right
            dp[r][c] = res + 1
            return dp[r][c]

        res = 1
        for r in range(m):
            for c in range(n):
                res = max(res, dfs(r, c))

        return res
# @lc code=end
