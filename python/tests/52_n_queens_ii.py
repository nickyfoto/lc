#
# @lc app=leetcode id=52 lang=python3
#
# [52] N-Queens II
#
# https://leetcode.com/problems/n-queens-ii/description/
#
# algorithms
# Hard (55.03%)
# Likes:    376
# Dislikes: 132
# Total Accepted:    117.1K
# Total Submissions: 212.8K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard
# such that no two queens attack each other.
# 
# 
# 
# Given an integer n, return the number of distinct solutions to the n-queens
# puzzle.
# 
# Example:
# 
# 
# Input: 4
# Output: 2
# Explanation: There are two distinct solutions to the 4-queens puzzle as shown
# below.
# [
# [".Q..",  // Solution 1
# "...Q",
# "Q...",
# "..Q."],
# 
# ["..Q.",  // Solution 2
# "Q...",
# "...Q",
# ".Q.."]
# ]
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    def totalNQueens2(self, n: int) -> int:
        """
        for row 0 there are n possible positions
        """
        if n == 1:
            return 1
        self.res = 0

        def update_board(row, col, board):
            for r in range(row+1, n):
                diff = r - row
                mark = col - diff
                # print('diff=', diff, 'mark=', mark)
                if mark >= 0:
                    board[r][mark] = True
                mark = col + diff
                # print('diff=', diff, 'mark=', mark)
                if mark < n:
                    board[r][mark] = True
                board[r][col] = True

        def assign(board):
            row = board['next']
                
            # print('before', board)
            for col in range(n):
                if col not in board[row]:
                    board_copy = deepcopy(board)
                    board_copy[row][col] = True
                    # board_copy[row]['col'] = col
                    update_board(row, col, board=board_copy)
                    if row == n - 1:
                        # print('succ', board_copy)
                        self.res += 1
                    else:
                        board_copy['next'] += 1
                        # print('after', board_copy)
                        boards.append(board_copy)
            # print()

        boards = []
        for col in range(n): # for row 0
            board = {row: {} for row in range(n)}
            board[0][col] = True
            board[0]['col'] = col
            update_board(row=0, col=col, board=board)
            board['next'] = 1
            # assign(board) 
            # print('col=', col, board)
            boards.append(board)

        while boards:
            board = boards.pop(0)
            assign(board)
        return self.res
    
    def totalNQueens(self, n):
        """
        https://leetcode.wang/leetCode-52-N-QueensII.html
        use one array to check whether there's diagnoal conflict
        """
        self.res = 0
        def recur(n, v, l, r, row):
            if row == n:
                self.res += 1
                return
            for col in range(n):
                print('col=', col, 'row=', row)
                print('row - col + n=', row - col + n, 'row + col=', row + col)
                if v[col] or l[row - col + n] or r[row + col]:
                    continue
                v[col] = True
                l[row - col + n] = True
                r[row + col] = True
                recur(n, v, l, r, row + 1)
                v[col] = False
                l[row - col + n] = False
                r[row + col] = False
        recur(n, defaultdict(lambda: False), defaultdict(lambda: False), defaultdict(lambda: False), 0)
        return self.res
# @lc code=end
