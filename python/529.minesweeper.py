#
# @lc app=leetcode id=529 lang=python3
#
# [529] Minesweeper
#
# https://leetcode.com/problems/minesweeper/description/
#
# algorithms
# Medium (54.13%)
# Total Accepted:    38.5K
# Total Submissions: 71.1K
# Testcase Example:  '[["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]]\n[3,0]'
#
# Let's play the minesweeper game (Wikipedia, online game)!
# 
# You are given a 2D char matrix representing the game board. 'M' represents an
# unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a
# revealed blank square that has no adjacent (above, below, left, right, and
# all 4 diagonals) mines, digit ('1' to '8') represents how many mines are
# adjacent to this revealed square, and finally 'X' represents a revealed
# mine.
# 
# Now given the next click position (row and column indices) among all the
# unrevealed squares ('M' or 'E'), return the board after revealing this
# position according to the following rules:
# 
# 
# If a mine ('M') is revealed, then the game is over - change it to 'X'.
# If an empty square ('E') with no adjacent mines is revealed, then change it
# to revealed blank ('B') and all of its adjacent unrevealed squares should be
# revealed recursively.
# If an empty square ('E') with at least one adjacent mine is revealed, then
# change it to a digit ('1' to '8') representing the number of adjacent
# mines.
# Return the board when no more squares will be revealed.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: 
# 
# [['E', 'E', 'E', 'E', 'E'],
# ⁠['E', 'E', 'M', 'E', 'E'],
# ⁠['E', 'E', 'E', 'E', 'E'],
# ⁠['E', 'E', 'E', 'E', 'E']]
# 
# Click : [3,0]
# 
# Output: 
# 
# [['B', '1', 'E', '1', 'B'],
# ⁠['B', '1', 'M', '1', 'B'],
# ⁠['B', '1', '1', '1', 'B'],
# ⁠['B', 'B', 'B', 'B', 'B']]
# 
# Explanation:
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# 
# [['B', '1', 'E', '1', 'B'],
# ⁠['B', '1', 'M', '1', 'B'],
# ⁠['B', '1', '1', '1', 'B'],
# ⁠['B', 'B', 'B', 'B', 'B']]
# 
# Click : [1,2]
# 
# Output: 
# 
# [['B', '1', 'E', '1', 'B'],
# ⁠['B', '1', 'X', '1', 'B'],
# ⁠['B', '1', '1', '1', 'B'],
# ⁠['B', 'B', 'B', 'B', 'B']]
# 
# Explanation:
# 
# 
# 
# 
# 
# Note:
# 
# 
# The range of the input matrix's height and width is [1,50].
# The click position will only be an unrevealed square ('M' or 'E'), which also
# means the input board contains at least one clickable square.
# The input board won't be a stage when game is over (some mines have been
# revealed).
# For simplicity, not mentioned rules should be ignored in this problem. For
# example, you don't need to reveal all the unrevealed mines when the game is
# over, consider any cases that you will win the game or flag any squares.
# 
# 
#
from collections import defaultdict
from pprint import pprint
class Solution:
    # def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
    def updateBoard(self, board, click):
        class Node:
            def __init__(self, r,c):
                self.r = r
                self.c = c
                mine = self.count_mine_around()
                if not mine:
                    board[self.r][self.c] = 'B'
                else:
                    board[self.r][self.c] = str(mine)

            def mine(self, r,c):
                if board[r][c] == 'M':
                    return 1
                else:
                    return 0

            def border_valid(self, r,c):
                return r >= 0 and r < n_rows and c >= 0 and c < n_cols

            def check(self, r,c, func):
                if not self.border_valid(r,c):
                    return 0
                return func(r,c)

            def count_mine_around(self):
                res = 0
                res += self.check(*self.up_left(),self.mine)
                res += self.check(*self.up(),self.mine)
                res += self.check(*self.up_right(),self.mine)
                res += self.check(*self.left(),self.mine)
                res += self.check(*self.right(),self.mine)
                res += self.check(*self.down_left(),self.mine)
                res += self.check(*self.down(),self.mine)
                res += self.check(*self.down_right(),self.mine)
                return res

            def valid(self, r,c):
                if not explored[(r,c)] and board[r][c] == 'E':
                    return Node(r,c)
                else:
                    return None
            
            def up_left(self):
                return self.r - 1, self.c - 1
            def up_right(self):
                return self.r - 1, self.c + 1
            def up(self):
                return self.r - 1, self.c
            def left(self):
                return self.r, self.c - 1
            def right(self):
                return self.r, self.c + 1
            def down_left(self):
                return self.r + 1, self.c -1
            def down(self):
                return self.r + 1, self.c
            def down_right(self):
                return self.r + 1, self.c + 1

            def explore(self, r,c):
                node = self.check(r,c, self.valid)
                if node:
                    node.dfs()
            def dfs(self):
                if board[self.r][self.c] == 'B':


                    # up_left = self.check(*self.up_left(), self.valid)
                    # if up_left:
                    #     up_left.dfs()
                    self.explore(*self.up_left())
                    self.explore(*self.up())
                    self.explore(*self.up_right())
                    self.explore(*self.left())
                    self.explore(*self.right())
                    self.explore(*self.down())
                    self.explore(*self.down_left())
                    self.explore(*self.down_right())

        n_rows = len(board)
        n_cols = len(board[0])
        r, c = tuple(click)
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        else:
            explored = defaultdict(lambda: False)
            explored[(r,c)] = True
            node = Node(r,c)

            node.dfs()

        # pprint(board)
        return board
        # return board

# s = Solution()
# board = [['E', 'E', 'E', 'E', 'E'],
# ['E', 'E', 'M', 'E', 'E'],
# ['E', 'E', 'E', 'E', 'E'],
# ['E', 'E', 'E', 'E', 'E']]

# click = [3,0]
# print(s.updateBoard(board, click))

# board = [["E"]]
# click = [0,0]
# print(s.updateBoard(board, click))

# board = [["E","E","E","E","E","E","E","E"],
#          ["E","E","E","E","E","E","E","M"],
#          ["E","E","M","E","E","E","E","E"],
#          ["M","E","E","E","E","E","E","E"],
#          ["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","E","E","E","E","E","E"],["E","E","M","M","E","E","E","E"]]
# click = [0,0]
# print(s.updateBoard(board, click) == [["B","B","B","B","B","B","1","E"],
#  ["B","1","1","1","B","B","1","M"],
#  ["1","2","M","1","B","B","1","1"],
#  ["M","2","1","1","B","B","B","B"],
#  ["1","1","B","B","B","B","B","B"],
#  ["B","B","B","B","B","B","B","B"],
#  ["B","1","2","2","1","B","B","B"],
#  ["B","1","M","M","1","B","B","B"]])