#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
# https://leetcode.com/problems/unique-paths-ii/description/
#
# algorithms
# Medium (33.91%)
# Likes:    1267
# Dislikes: 209
# Total Accepted:    255.2K
# Total Submissions: 752.5K
# Testcase Example:  '[[0,0,0],[0,1,0],[0,0,0]]'
#
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
# the diagram below).
# 
# The robot can only move either down or right at any point in time. The robot
# is trying to reach the bottom-right corner of the grid (marked 'Finish' in
# the diagram below).
# 
# Now consider if some obstacles are added to the grids. How many unique paths
# would there be?
# 
# 
# 
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
# 
# Note: m and n will be at most 100.
# 
# Example 1:
# 
# 
# Input:
# [
# [0,0,0],
# [0,1,0],
# [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
# 
# 
#

# @lc code=start
class Solution:
    # def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        if ob col == n - 1, all above will be ob
        if ob row == m -1, all left will be ob
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        def update_obs():
            for r in range(m):
                for c in range(n):
                    if obstacleGrid[r][c] == 1:
                        if r == 0:
                            update('up')
                        elif r == m - 1:
                            update('down')
                        elif c == 0:
                            update('left')
                        elif c == n - 1:
                            update('right')

        update_obs()
        
# @lc code=end
