#
# @lc app=leetcode id=883 lang=python3
#
# [883] Projection Area of 3D Shapes
#
# https://leetcode.com/problems/projection-area-of-3d-shapes/description/
#
# algorithms
# Easy (65.60%)
# Total Accepted:    17.6K
# Total Submissions: 26.7K
# Testcase Example:  '[[2]]'
#
# On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the
# x, y, and z axes.
# 
# Each value v = grid[i][j] represents a tower of v cubes placed on top of grid
# cell (i, j).
# 
# Now we view the projection of these cubes onto the xy, yz, and zx planes.
# 
# A projection is like a shadow, that maps our 3 dimensional figure to a 2
# dimensional plane. 
# 
# Here, we are viewing the "shadow" when looking at the cubes from the top, the
# front, and the side.
# 
# Return the total area of all three
# projections.
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
# Output: 5
# 
# 
# 
# Example 2:
# 
# 
# Input: [[1,2],[3,4]]
# Output: 17
# Explanation: 
# Here are the three projections ("shadows") of the shape made with each
# axis-aligned plane.
# 
# 
# 
# 
# Example 3:
# 
# 
# Input: [[1,0],[0,2]]
# Output: 8
# 
# 
# 
# Example 4:
# 
# 
# Input: [[1,1,1],[1,0,1],[1,1,1]]
# Output: 14
# 
# 
# 
# Example 5:
# 
# 
# Input: [[2,2,2],[2,1,2],[2,2,2]]
# Output: 21
# 
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= grid.length = grid[0].length <= 50
# 0 <= grid[i][j] <= 50
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
class Solution:
    # def projectionArea(self, grid: List[List[int]]) -> int:
    def top_down(self, grid):
        res = 0
        for row in grid:
            for ele in row:
                if ele != 0:
                    res += 1
        return res
    def bottom_up(self, grid):
        res = grid[0]
        
        for r in range(1, len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] > res[c]:
                    res[c] = grid[r][c]
        return sum(res)
    def left_right(self, grid):
        res = [r[0] for r in grid]
        for r in range(len(grid)):
            for c in range(1, len(grid[0])):
                if grid[r][c] > res[r]:
                    res[r] = grid[r][c]
        return sum(res)
    def projectionArea(self, grid):
        top_down = self.top_down(grid)
        # print(top_down)
        left_right = self.left_right(grid)
        # print(left_right)
        bottom_up = self.bottom_up(grid)
        # print(bottom_up)
        # print(top_down+left_right+bottom_up)

        return (top_down+left_right+bottom_up)



# s = Solution()

# grid = [[2]]
# print(s.projectionArea(grid) == 5)


# grid = [[1,2],[3,4]]
# print(s.projectionArea(grid) == 17)


# grid = [[1,0],[0,2]]
# print(s.projectionArea(grid) == 8)
# grid = [[1,1,1],[1,0,1],[1,1,1]]
# print(s.projectionArea(grid) == 14)
# grid = [[2,2,2],[2,1,2],[2,2,2]]
# print(s.projectionArea(grid) == 21)

