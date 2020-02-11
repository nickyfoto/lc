#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
# https://leetcode.com/problems/minimum-path-sum/description/
#
# algorithms
# Medium (50.69%)
# Likes:    2087
# Dislikes: 48
# Total Accepted:    306.5K
# Total Submissions: 604.5K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# Given a m x n grid filled with non-negative numbers, find a path from top
# left to bottom right which minimizes the sum of all numbers along its path.
# 
# Note: You can only move either down or right at any point in time.
# 
# Example:
# 
# 
# Input:
# [
#  [1,3,1],
# ⁠ [1,5,1],
# ⁠ [4,2,1]
# ]
# Output: 7
# Explanation: Because the path 1→3→1→1→1 minimizes the sum.
# 
# 
#

# @lc code=start
from heapq import heappop, heappush
class Solution:
    # def minPathSum(self, grid: List[List[int]]) -> int:
    def minPathSum(self, grid):
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        res = [[0] * n for _ in range(m)]
        res[0][0] = grid[0][0]
        for r in range(m):
            for c in range(n):
                if r == 0 and c > 0:
                    res[r][c] = grid[r][c] + res[r][c - 1]
                elif c == 0 and r > 0:
                    res[r][c] = grid[r][c] + res[r - 1][c]
                else:
                    res[r][c] = grid[r][c] + min(res[r - 1][c], res[r][c - 1])
        return res[-1][-1]

    def minPathSum_me(self, grid):
        """
        wrong method
        """
        if not grid:
            return 0
        m = len(grid)
        n = len(grid[0])
        q = []
        heappush(q, (grid[0][0], (0, 0)))
        while q:
            dist, (r, c) = heappop(q)
            if (r, c) == (m - 1, n - 1):
                return dist
            for rr, cc in [[r + 1, c], [r, c + 1]]:
                if rr < m and cc < n:
                    heappush(q, (dist + grid[rr][cc], (rr, cc)))
# @lc code=end
