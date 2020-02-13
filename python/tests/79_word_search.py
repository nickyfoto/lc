#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (33.54%)
# Likes:    2757
# Dislikes: 138
# Total Accepted:    388.8K
# Total Submissions: 1.2M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given a 2D board and a word, find if the word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cell, where
# "adjacent" cells are those horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# Example:
# 
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# Given word = "ABCCED", return true.
# Given word = "SEE", return true.
# Given word = "ABCB", return false.
# 
# 
#

# @lc code=start
from collections import defaultdict
class Solution:
    # def exist(self, board: List[List[str]], word: str) -> bool:
    def exist(self, board, word):
        if not board:
            return False
        m = len(board)
        n = len(board[0])

        def backtrack(board, r, c, idx):
            if idx == len(word): return True
            if r > m - 1 or r < 0 or c < 0 or c > n - 1 or board[r][c] != word[idx]:
                return False
            board[r][c] = '*'
            res = backtrack(board, r - 1, c, idx + 1) or \
                  backtrack(board, r + 1, c, idx + 1) or \
                  backtrack(board, r, c - 1, idx + 1) or \
                  backtrack(board, r, c + 1, idx + 1)
            board[r][c] = word[idx]
            return res

        for r in range(m):
            for c in range(n):
                if backtrack(board, r, c, 0):
                    return True
        return False
    def exist_me(self, board, word):
        if not board:
            return False
        m = len(board)
        n = len(board[0])

        def get_adj(r, c, word, used):
            res = []
            # print('r=', r, 'c=', c, 'm=', m)
            if r - 1 >= 0 and not used[(r - 1, c)] and board[r - 1][c] == word[0]:
                res.append((r - 1, c))
            if r + 1 < m and not used[(r + 1, c)] and board[r + 1][c] == word[0]:
                # print('here')
                res.append((r + 1, c))
            if c - 1 >= 0 and not used[(r, c - 1)] and board[r][c - 1] == word[0]:
                res.append((r, c - 1))
            if c + 1 < n and not used[(r, c + 1)] and board[r][c + 1] == word[0]:
                res.append((r, c + 1))
            return res

        def bfs(r, c, word, used):
            if not word:
                return True
            adj = get_adj(r, c, word, used)
            # print(adj)
            if adj:
                for i, j in adj:
                    used[(i,j)] = True
                    if bfs(i, j, word[1:], used):
                        return True
                    used[(i,j)] = False
            return False

        for r in range(m):
            for c in range(n):
                d = defaultdict(lambda:False)
                d[(r,c)] = True
                if board[r][c] == word[0] and bfs(r, c, word[1:], d):
                    return True
        return False
# @lc code=end
