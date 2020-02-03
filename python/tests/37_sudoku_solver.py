#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#
# https://leetcode.com/problems/sudoku-solver/description/
#
# algorithms
# Hard (40.51%)
# Likes:    1328
# Dislikes: 81
# Total Accepted:    161.2K
# Total Submissions: 397.7K
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# 
# A sudoku solution must satisfy all of the following rules:
# 
# 
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the the digits 1-9 must occur exactly once in each of the 9 3x3
# sub-boxes of the grid.
# 
# 
# Empty cells are indicated by the character '.'.
# 
# 
# A sudoku puzzle...
# 
# 
# ...and its solution numbers marked in red.
# 
# Note:
# 
# 
# The given board contain only digits 1-9 and the character '.'.
# You may assume that the given Sudoku puzzle will have a single unique
# solution.
# The given board size is always 9x9.
# 
# 
#

# @lc code=start
from pprint import pprint
class Solution:
    # def solveSudoku(self, board: List[List[str]]) -> None:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """

        def valid(d, r, c):
            blkrow = (r // 3) * 3
            blkcol = (c // 3) * 3
            for i in range(9):
                if  board[i][c] == str(d) or board[r][i] == str(d) or \
                    board[blkrow + i // 3][blkcol + i % 3] == str(d):
                    return False
            return True

        def solve(board):
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        for d in range(1,10):
                            if valid(d, r, c):
                                board[r][c] = str(d)
                                if solve(board):
                                    return True
                                else:
                                    board[r][c] = '.'
                        return False
            return True

        solve(board)
        # print()
        # pprint(board)
        return board
# @lc code=end
