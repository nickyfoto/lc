#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
# https://leetcode.com/problems/word-search-ii/description/
#
# algorithms
# Hard (31.84%)
# Likes:    1776
# Dislikes: 89
# Total Accepted:    161.5K
# Total Submissions: 506.6K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
#  '["oath","pea","eat","rain"]'
#
# Given a 2D board and a list of words from the dictionary, find all words in
# the board.
# 
# Each word must be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring. The
# same letter cell may not be used more than once in a word.
# 
# 
# 
# Example:
# 
# 
# Input: 
# board = [
# ⁠ ['o','a','a','n'],
# ⁠ ['e','t','a','e'],
# ⁠ ['i','h','k','r'],
# ⁠ ['i','f','l','v']
# ]
# words = ["oath","pea","eat","rain"]
# 
# Output: ["eat","oath"]
# 
# 
# 
# 
# Note:
# 
# 
# All inputs are consist of lowercase letters a-z.
# The values of words are distinct.
# 
# 
#

# @lc code=start
class Solution:
    # def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    def findWords(self, board, words):
        if not board or not words:
            return []
        max_length = max(map(len, words))
        words = {word:None for word in words}
        d = {}
        for i in range(1, max_length+1):
            d[i] = {word[:i]:None for word in words if len(word) >= i}
        # print(d)
        m = len(board)
        n = len(board[0])
        res = {}

        def backtrack(r, c, word):
            if r < 0 or c < 0 or r > m - 1 or c > n - 1 or len(res) == len(words):
                return
            word += board[r][c]
            if len(word) > max_length:
                return
            if word in words:
                if word not in res:
                    res[word] = None
            if word in d[len(word)]:
                board[r][c] = '*'
                backtrack(r + 1, c, word)
                backtrack(r - 1, c, word)
                backtrack(r, c + 1, word)
                backtrack(r, c - 1, word)
                board[r][c] = word[-1]


        for r in range(m):
            for c in range(n):
                if board[r][c] in d[1]:
                    backtrack(r, c, "")
        return res.keys()
# @lc code=end
