#
# @lc app=leetcode id=892 lang=python3
#
# [892] Surface Area of 3D Shapes
#
# https://leetcode.com/problems/surface-area-of-3d-shapes/description/
#
# algorithms
# Easy (55.73%)
# Total Accepted:    10.6K
# Total Submissions: 19.1K
# Testcase Example:  '[[2]]'
#
# On a N * N grid, we place some 1 * 1 * 1 cubes.
# 
# Each value v = grid[i][j] represents a tower of v cubes placed on top of grid
# cell (i, j).
# 
# Return the total surface area of the resulting shapes.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [[2]]
# Output: 10
# 
# 
# 
# Example 2:
# 
# 
# Input: [[1,2],[3,4]]
# Output: 34
# 
# 
# 
# Example 3:
# 
# 
# Input: [[1,0],[0,2]]
# Output: 16
# 
# 
# 
# Example 4:
# 
# 
# Input: [[1,1,1],[1,0,1],[1,1,1]]
# Output: 32
# 
# 
# 
# Example 5:
# 
# 
# Input: [[2,2,2],[2,1,2],[2,2,2]]
# Output: 46
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 50
# 0 <= grid[i][j] <= 50
# 
# 
# 
# 
# 
# 
# 
#
class Solution:
    # def surfaceArea(self, grid: List[List[int]]) -> int:
    def top_down(self, grid):
        res = 0
        for row in grid:
            for ele in row:
                if ele != 0:
                    res += 1
        return res
    def left_right(self, grid):
        res = [r[0] for r in grid]
        for r in range(len(grid)):
            for c in range(1, len(grid[0])):
                if grid[r][c] > grid[r][c-1]:
                    res[r] += grid[r][c] - grid[r][c-1]
        return sum(res)
    def right_left(self,grid):
        res = [r[-1] for r in grid]
        for r in range(len(grid)):
            for c in range(len(grid[0])-2, -1, -1):
                if grid[r][c] > grid[r][c+1]:
                    res[r] += grid[r][c] - grid[r][c+1]
        return sum(res)

    def up_bottum(self, grid):
        res = grid[0].copy()
        for r in range(1, len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] > grid[r-1][c]:
                    res[c] += grid[r][c] - grid[r-1][c]
        return sum(res)
    def bottum_up(self, grid):
        res = grid[-1].copy()
        # print(grid)
        for r in range(len(grid)-2, -1, -1):
            # print('r', r)
            for c in range(len(grid[0])):
                if grid[r][c] > grid[r+1][c]:
                    # print('r=', r, grid[r])
                    # print('r+1=', r+1, grid[r+1])
                    res[c] += grid[r][c] - grid[r+1][c]
                    # print(res)
        return sum(res)
    def surfaceArea(self, grid):
        td = self.top_down(grid)
        lr = self.left_right(grid)
        rl = self.right_left(grid)
        # print(grid)
        ub = self.up_bottum(grid)
        bu = self.bottum_up(grid)
        # print(td)
        # print(lr)
        # print(rl)
        # print(ub)
        # print(bu)
        res = td*2+lr+rl+ub+bu
        # print(res)
        return res




# s = Solution()

# grid = [[2]]
# print(s.surfaceArea(grid) == 10)


# grid = [[1,2],[3,4]]
# print(s.surfaceArea(grid) == 34)


# grid = [[1,0],[0,2]]
# print(s.surfaceArea(grid) == 16)

# grid = [[1,1,1],[1,0,1],[1,1,1]]
# print(s.surfaceArea(grid) == 32)

# grid = [[2,2,2],[2,1,2],[2,2,2]]
# print(s.surfaceArea(grid) == 46)





























