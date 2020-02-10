#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (50.97%)
# Likes:    756
# Dislikes: 98
# Total Accepted:    171K
# Total Submissions: 335.3K
# Testcase Example:  '3'
#
# Given a positive integer n, generate a square matrix filled with elements
# from 1 to n^2 in spiral order.
# 
# Example:
# 
# 
# Input: 3
# Output:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
# 
# 
#

# @lc code=start
from itertools import cycle
from pprint import pprint
class Solution:
    # def generateMatrix(self, n: int) -> List[List[int]]:
    def generateMatrix(self, n):
        total = n * n
        i = 1
        res = [[0] * n for _ in range(n)]
        cmd = cycle(['left', 'down', 'right', 'up'])
        command = next(cmd)
        r, c = 0, 0
        def blocked(r, c):
            # print(r,c, visited[(r, c)] or r < 0 or r == m or c < 0 or c == n)
            return r < 0 or r == n or c < 0 or c == n or res[r][c] > 0
        while i <= total:
            # print(command, i, r, c)
            while command == 'left' and not blocked(r, c):
                res[r][c] = i
                c += 1
                i += 1
            while command == 'down' and not blocked(r, c):
                res[r][c] = i
                r += 1
                i += 1
            while command == 'right' and not blocked(r, c):
                res[r][c] = i
                c -= 1
                i += 1
            while command == 'up' and not blocked(r, c):
                res[r][c] = i
                r -= 1
                i += 1
            if command == 'left':
                c -= 1
                r += 1
            elif command == 'down':
                r -= 1
                c -= 1
            elif command == 'right':
                c += 1
                r -= 1
            elif command == 'up':
                r += 1
                c += 1
            # if i == total:
                # break
            # i -= 1
            # print('here', r, c, command, res)
            command = next(cmd)
        # pprint(res, width=40)
        return res
# @lc code=end
