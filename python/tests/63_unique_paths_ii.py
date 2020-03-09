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
        from official answer
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        obstacleGrid[0][0] = 1
        for i in range(1, m):
            # for the first column
            # if curr == 0 and up == 1
            # set curr = 1
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i - 1][0] == 1)
        for j in range(1, n):
            # for the first row
            # if curr == 0 left == 1
            # set curr = 1
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j - 1] == 1)
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                else:
                    obstacleGrid[i][j] = 0
        return obstacleGrid[-1][-1]
        
# @lc code=end
