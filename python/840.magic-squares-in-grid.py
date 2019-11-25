#
# @lc app=leetcode id=840 lang=python3
#
# [840] Magic Squares In Grid
#
# https://leetcode.com/problems/magic-squares-in-grid/description/
#
# algorithms
# Easy (35.58%)
# Total Accepted:    13.6K
# Total Submissions: 38.2K
# Testcase Example:  '[[4,3,8,4],[9,5,1,9],[2,7,6,2]]'
#
# A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9
# such that each row, column, and both diagonals all have the same sum.
# 
# Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?
# (Each subgrid is contiguous).
# 
# 
# 
# Example 1:
# 
# 
# Input: [[4,3,8,4],
# ⁠        [9,5,1,9],
# ⁠        [2,7,6,2]]
# Output: 1
# Explanation: 
# The following subgrid is a 3 x 3 magic square:
# 438
# 951
# 276
# 
# while this one is not:
# 384
# 519
# 762
# 
# In total, there is only one magic square inside the given grid.
# 
# 
# Note:
# 
# 
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# 0 <= grid[i][j] <= 15
# 
# 
#
class Solution:
    # def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
    def numMagicSquaresInside(self, grid):
        n_rows = len(grid)
        n_cols = len(grid[0])
        res = 0

        def isMagic(r,c):
            res = []
            for row in range(r,r+3):
                rr = grid[row][c:c+3]
                if sum(rr) != 15:
                    return False
                else:
                    res.extend(rr)
            for col in range(c,c+3):
                total = 0
                for row in range(r,r+3):
                    total += grid[row][col]
                if total != 15:
                    return False
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != 15:
                return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != 15:
                return False
            if set(res) != set(range(1,10)):
                return False
            return True

        for r in range(n_rows-2):
            for c in range(n_cols-2):
                # print(r,c)
                if isMagic(r,c):
                    res += 1
        return res


# s = Solution()
# grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
# print(s.numMagicSquaresInside(grid))

# grid = [[5,5,5],[5,5,5],[5,5,5]]
# print(s.numMagicSquaresInside(grid))