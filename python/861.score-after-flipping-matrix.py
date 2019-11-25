#
# @lc app=leetcode id=861 lang=python3
#
# [861] Score After Flipping Matrix
#
# https://leetcode.com/problems/score-after-flipping-matrix/description/
#
# algorithms
# Medium (70.37%)
# Total Accepted:    14.2K
# Total Submissions: 20.2K
# Testcase Example:  '[[0,0,1,1],[1,0,1,0],[1,1,0,0]]'
#
# We have a two dimensional matrix A where each value is 0 or 1.
# 
# A move consists of choosing any row or column, and toggling each value in
# that row or column: changing all 0s to 1s, and all 1s to 0s.
# 
# After making any number of moves, every row of this matrix is interpreted as
# a binary number, and the score of the matrix is the sum of these numbers.
# 
# Return the highest possible score.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# Output: 39
# Explanation:
# Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
# 0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 20
# 1 <= A[0].length <= 20
# A[i][j] is 0 or 1.
# 
# 
# 
#
# from math import ceil
class Solution:
    # def matrixScore(self, A: List[List[int]]) -> int:
    def matrixScore(self, A):
        
        n_row = len(A)
        n_col = len(A[0])

        for r in range(n_row):
            if A[r][0] == 0:
                A[r] = list(map(lambda x: 1 - x, A[r]))
        def sum_col(c):
            return sum(A[r][c] for r in range(n_row))
        def flip_col(c):
            for r in range(n_row):
                A[r][c] = 1 - A[r][c]
        for c in range(n_col):
            if sum_col(c) <= int(n_row / 2):
                flip_col(c)
        # print(A)
        def getSum(l):
            return sum([2**(n_col-i-1) for i in range(n_col) if l[i]])
        # print(sum(map(getSum, A)))
        return sum(map(getSum, A))


# s = Solution()
# A = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
# print(s.matrixScore(A))




















