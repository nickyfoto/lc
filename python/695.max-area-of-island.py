#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#
# https://leetcode.com/problems/max-area-of-island/description/
#
# algorithms
# Medium (58.49%)
# Total Accepted:    95.2K
# Total Submissions: 162.7K
# Testcase Example:  '[[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]'
#
# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.) You
# may assume all four edges of the grid are surrounded by water.
# 
# Find the maximum area of an island in the given 2D array. (If there is no
# island, the maximum area is 0.)
# 
# Example 1:
# 
# 
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
# ⁠ [0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠ [0,1,1,0,1,0,0,0,0,0,0,0,0],
# ⁠ [0,1,0,0,1,1,0,0,1,0,1,0,0],
# ⁠ [0,1,0,0,1,1,0,0,1,1,1,0,0],
# ⁠ [0,0,0,0,0,0,0,0,0,0,1,0,0],
# ⁠ [0,0,0,0,0,0,0,1,1,1,0,0,0],
# ⁠ [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# 
# Given the above grid, return 6. Note the answer is not 11, because the island
# must be connected 4-directionally.
# 
# Example 2:
# 
# 
# [[0,0,0,0,0,0,0,0]]
# Given the above grid, return 0.
# 
# Note: The length of each dimension in the given grid does not exceed 50.
# 
#


from collections import defaultdict

class Solution:
    # def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    def maxAreaOfIsland(self, grid):

        class ISLAND:
            def __init__(self, row, col):
                self.row = row
                self.col = col
                self.area = 1
                self.root = [self.row, self.col]
                # print(self.root, self.area)

            def explore(self, r, c):
                if grid[r][c] and not explored.get((r,c)):
                    island = ISLAND(r, c)
                    explored[(r,c)] = island
                    area = island.dfs()
                    return 1+area
                else:
                    return 0
            
            def dfs(self):
                # up
                area = 0
                if self.row > 0:
                    r, c = self.row-1, self.col
                    area += self.explore(r,c)
                # down
                if self.row < n_row - 1:
                    r, c = self.row+1, self.col
                    area += self.explore(r,c)
                # left
                if self.col > 0:
                    r, c = self.row, self.col - 1
                    area += self.explore(r,c)
                # right
                if self.col < n_col - 1:
                    r, c = self.row, self.col + 1
                    area += self.explore(r,c)
                self.area += area
                return area
        


        explored = {}

        n_row = len(grid)
        n_col = len(grid[0])
        for r in range(n_row):
            for c in range(n_col):
                if grid[r][c] and not explored.get((r,c)):
                    island = ISLAND(r, c)
                    explored[(r,c)] = island
                    island.dfs()
                    # print(island.area, island.root)
        res = [v.area for k,v in explored.items()]
        # print(res)
        if res:
            return max(res)
        else:
            return 0
        # print(explored)





# s = Solution()
# grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#         [0,0,0,0,0,0,0,1,1,1,0,0,0],
#         [0,1,1,0,1,0,0,0,0,0,0,0,0],
#         [0,1,0,0,1,1,0,0,1,0,1,0,0],
#         [0,1,0,0,1,1,0,0,1,1,1,0,0],
#         [0,0,0,0,0,0,0,0,0,0,1,0,0],
#         [0,0,0,0,0,0,0,1,1,1,0,0,0],
#         [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# print(s.maxAreaOfIsland(grid))

# # grid = [[0,0,0,0,0,0,0,0]]
# # print(s.maxAreaOfIsland(grid))

# grid = [[0,1,1],
#         [1,1,0]]
# print(s.maxAreaOfIsland(grid)) # 4












