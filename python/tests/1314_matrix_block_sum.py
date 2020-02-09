#
# @lc app=leetcode id=1314 lang=python3
#
# [1314] Matrix Block Sum
#
# https://leetcode.com/problems/matrix-block-sum/description/
#
# algorithms
# Medium (71.72%)
# Likes:    93
# Dislikes: 16
# Total Accepted:    5.1K
# Total Submissions: 7.2K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]\n1'
#
# Given a m * n matrix mat and an integer K, return a matrix answer where each
# answer[i][j] is the sum of all elements mat[r][c] for i - K <= r <= i + K, j
# - K <= c <= j + K, and (r, c) is a valid position in the matrix.
# 
# Example 1:
# 
# 
# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]], K = 1
# Output: [[12,21,16],[27,45,33],[24,39,28]]
# 
# 
# Example 2:
# 
# 
# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
# Output: [[45,45,45],[45,45,45],[45,45,45]]
# 
# 
# 
# Constraints:
# 
# 
# m == mat.length
# n == mat[i].length
# 1 <= m, n, K <= 100
# 1 <= mat[i][j] <= 100
# 
#

# @lc code=start
from pprint import pprint
class Solution:
    # def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
    def matrixBlockSum(self, mat, K):
        m, n = len(mat), len(mat[0])
        rangeSum = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                rangeSum[i + 1][j + 1] = rangeSum[i + 1][j] + rangeSum[i][j + 1] - rangeSum[i][j] + mat[i][j]
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1, c1, r2, c2 = max(0, i - K), max(0, j - K), min(m, i + K + 1), min(n, j + K + 1)
                res[i][j] = rangeSum[r2][c2] - rangeSum[r1][c2] - rangeSum[r2][c1] + rangeSum[r1][c1]
        return res


    def matrixBlockSum_me(self, mat, K):
        m = len(mat)
        n = len(mat[0])
        res = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                rows = range(max(0, i - K), min(m, i + K + 1))
                cols = range(max(0, j - K), min(n, j + K + 1))
                res[i][j] = sum(mat[r][c] for c in cols for r in rows)
        return res

# @lc code=end
