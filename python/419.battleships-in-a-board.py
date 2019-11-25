#
# @lc app=leetcode id=419 lang=python3
#
# [419] Battleships in a Board
#
# https://leetcode.com/problems/battleships-in-a-board/description/
#
# algorithms
# Medium (66.83%)
# Total Accepted:    70.4K
# Total Submissions: 105.4K
# Testcase Example:  '[["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]'
#
# Given an 2D board, count how many battleships are in it. The battleships are
# represented with 'X's, empty slots are represented with '.'s. You may assume
# the following rules:
# 
# 
# You receive a valid board, made of only battleships or empty slots.
# Battleships can only be placed horizontally or vertically. In other words,
# they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1
# column), where N can be of any size.
# At least one horizontal or vertical cell separates between two battleships -
# there are no adjacent battleships.
# 
# 
# Example:
# X..X
# ...X
# ...X
# 
# In the above board there are 2 battleships.
# 
# Invalid Example:
# ...X
# XXXX
# ...X
# 
# This is an invalid board that you will not receive - as battleships will
# always have a cell separating between them.
# 
# Follow up:Could you do it in one-pass, using only O(1) extra memory and
# without modifying the value of the board?
#
class Solution:
    # def countBattleships(self, board: List[List[str]]) -> int:
    def countBattleships(self, board) -> int:
        n_rows = len(board)
        n_cols = len(board[0])

        # print(n_rows, n_cols)

        def valid(p):
            r,c = p
            return n_rows > r >=0 and n_cols > c >= 0

        def get_around(r,c):
            up    = r-1,c
            down  = r+1,c
            left  = r,c-1
            right = r,c+1
            # print(up, down, left, right)
            return filter(valid, [up, down, left, right])

        def one_one_battle(r,c):
            around = get_around(r,c)
            return all([board[r][c] == '.' for r,c in around])

        def h_battle(r,c):
            if n_cols == 1:
                return False
            if c == 0:
                return board[r][c+1] == 'X'
            elif c == n_cols - 1:
                return board[r][c-1] == 'X'
            else:
                return board[r][c-1] == 'X' or board[r][c+1] == 'X'


        def v_battle(r,c):
            if n_rows == 1:
                return False
            if r == 0:
                return board[r+1][c] == 'X'
            elif r == n_rows - 1:
                return board[r-1][c] == 'X'
            else:
                return board[r-1][c] == 'X' or board[r+1][c] == 'X'

        def v_battle_start(r,c):
            if r == 0:
                return True
            else:
                return board[r-1][c] == '.'

        def h_battle_start(r,c):
            if c == 0:
                return True
            else:
                return board[r][c-1] == '.'

        nb = 0
        for r in range(n_rows):
            for c in range(n_cols):
                if board[r][c] == 'X':
                    if one_one_battle(r,c):
                        nb += 1
                    elif h_battle(r,c) and h_battle_start(r,c):
                        nb += 1
                    elif v_battle(r,c) and v_battle_start(r,c):
                        nb += 1

        # print('here', r,c, v_battle(3,0), h_battle(3,0), one_one_battle(3,0), v_battle_start(3,0))
        # print(nb)
        return nb


s = Solution()
board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
# print(s.countBattleships(board))


board = [["X","X","X"]]
# print(s.countBattleships(board))



board = [[".","X",".",".","X"],
         [".","X",".",".","X"],
         [".",".",".",".","X"],
         ["X",".","X","X","."],
         ["X",".",".",".","X"]]
print(s.countBattleships(board))





















        
