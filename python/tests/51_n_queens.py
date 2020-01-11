#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
# https://leetcode.com/problems/n-queens/description/
#
# algorithms
# Hard (43.08%)
# Likes:    1358
# Dislikes: 61
# Total Accepted:    173.3K
# Total Submissions: 402.3K
# Testcase Example:  '4'
#
# The n-queens puzzle is the problem of placing n queens on an n×n chessboard
# such that no two queens attack each other.
# 
# 
# 
# Given an integer n, return all distinct solutions to the n-queens puzzle.
# 
# Each solution contains a distinct board configuration of the n-queens'
# placement, where 'Q' and '.' both indicate a queen and an empty space
# respectively.
# 
# Example:
# 
# 
# Input: 4
# Output: [
# ⁠[".Q..",  // Solution 1
# ⁠ "...Q",
# ⁠ "Q...",
# ⁠ "..Q."],
# 
# ⁠["..Q.",  // Solution 2
# ⁠ "Q...",
# ⁠ "...Q",
# ⁠ ".Q.."]
# ]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as
# shown above.
# 
# 
#

# @lc code=start
from collections import defaultdict
from pprint import pprint
class Solution:
    def solveNQueens(self, n: int):
        self.res = []
        def backtrack(n, v, l, r, row, s):
            if row == n:
                self.res.append(s.copy())
                return

            for col in range(n):
                if v[col] or l[row - col + n] or r[row + col]:
                    continue
                v[col] = True
                l[row - col + n] = True
                r[row + col] = True
                
                s.append(col)    
                
                backtrack(n, v, l, r, row + 1, s)
                v[col] = False
                l[row - col + n] = False
                r[row + col] = False
                s.pop()

        v = defaultdict(lambda: False)
        l = defaultdict(lambda: False)
        r = defaultdict(lambda: False)
        
        backtrack(n, v, l, r, 0, [])

        def translate(res):
            answers = []
            for r in res:
                ans = [["."] * n for i in range(n)]
                for i in range(len(r)):
                    ans[i][r[i]] = 'Q'
                answers.append(["".join(a) for a in ans])
            return answers
        res = translate(self.res)
        return res
# @lc code=end
