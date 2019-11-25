#
# @lc app=leetcode id=463 lang=python3
#
# [463] Island Perimeter
#
# https://leetcode.com/problems/island-perimeter/description/
#
# algorithms
# Easy (61.07%)
# Total Accepted:    137.3K
# Total Submissions: 224.5K
# Testcase Example:  '[[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]'
#
# You are given a map in form of a two-dimensional integer grid where 1
# represents land and 0 represents water.
# 
# Grid cells are connected horizontally/vertically (not diagonally). The grid
# is completely surrounded by water, and there is exactly one island (i.e., one
# or more connected land cells).
# 
# The island doesn't have "lakes" (water inside that isn't connected to the
# water around the island). One cell is a square with side length 1. The grid
# is rectangular, width and height don't exceed 100. Determine the perimeter of
# the island.
# 
# 
# 
# Example:
# 
# 
# Input:
# [[0,1,0,0],
# ⁠ [1,1,1,0],
# ⁠ [0,1,0,0],
# ⁠ [1,1,0,0]]
# 
# Output: 16
# 
# Explanation: The perimeter is the 16 yellow stripes in the image below:
# 
# 
# 
# 
#
class Solution:
    # def islandPerimeter(self, grid: List[List[int]]) -> int:
    def islandPerimeter(self, grid):

        n_rows = len(grid)
        n_cols = len(grid[0])
        res = 0
        def getPeri(r,c):
            def getUp(r,c):
                if r < 0:
                    return 1
                else:
                    if grid[r][c] == 0:
                        return 1
                    else:
                        return 0
            def getDown(r,c):
                if r == n_rows:
                    return 1
                else:
                    if grid[r][c] == 0:
                        return 1
                    else:
                        return 0
            def getLeft(r,c):
                if c < 0:
                    return 1
                else:
                    if grid[r][c] == 0:
                        return 1
                    else:
                        return 0
            def getRight(r,c):
                if c == n_cols:
                    return 1
                else:
                    if grid[r][c] == 0:
                        return 1
                    else:
                        return 0
            up = getUp(r-1,c)
            down = getDown(r+1,c)
            left = getLeft(r,c-1)
            right = getRight(r,c+1)
            return up+down+left+right

        for r in range(n_rows):
            for c in range(n_cols):
                if grid[r][c] == 1:
                    res += getPeri(r,c)
        return res
# s = Solution()
# grid = [ [0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# print(s.islandPerimeter(grid))

