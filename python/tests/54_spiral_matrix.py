#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#
# https://leetcode.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (32.60%)
# Likes:    1744
# Dislikes: 493
# Total Accepted:    310.9K
# Total Submissions: 953.6K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of m x n elements (m rows, n columns), return all elements of
# the matrix in spiral order.
# 
# Example 1:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
# 
# 
# Example 2:
# 
# Input:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
# 
#

# @lc code=start
from itertools import cycle
from collections import defaultdict
class Solution:
    # def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    def spiralOrder(self, matrix):
        m = len(matrix)
        if m > 0:
            n = len(matrix[0])
        else:
            return []

        total = m * n

        i = 0
        res = []
        r, c = 0, 0
        cmd = cycle(['left', 'down', 'right', 'up'])
        command = next(cmd)
        visited = defaultdict(lambda: False)
        def blocked(r, c):
            # print(r,c, visited[(r, c)] or r < 0 or r == m or c < 0 or c == n)
            return visited[(r, c)] or r < 0 or r == m or c < 0 or c == n

        while i < total:
            # print(command, i, r, c)
            while command == 'left' and not blocked(r, c):
                res.append(matrix[r][c])
                visited[(r, c)] = True
                c += 1
                i += 1
            while command == 'down' and not blocked(r, c):
                res.append(matrix[r][c])
                visited[(r, c)] = True
                r += 1
                i += 1
            while command == 'right' and not blocked(r, c):
                res.append(matrix[r][c])
                visited[(r, c)] = True
                c -= 1
                i += 1
            while command == 'up' and not blocked(r, c):
                res.append(matrix[r][c])
                visited[(r, c)] = True
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
            # print('here', r, c, command)
            command = next(cmd)
            # print(res)
        return res

    def spiralOrder(self, matrix):
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]: return []
        m, n = len(matrix), len(matrix[0])
        res = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = i = 0
        seen = defaultdict(lambda: False)
        for _ in range(m * n):
            res.append(matrix[r][c])
            seen[r,c] = True
            rr, cc = r + dr[i], c + dc[i]
            if 0 <= rr < m and 0 <= cc < n and not seen[rr,cc]:
                r, c = rr, cc
            else:
                i = (i + 1) % 4
                r, c = r + dr[i], c + dc[i]
        return res

# @lc code=end
