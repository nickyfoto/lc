#
# @lc app=leetcode id=1277 lang=python3
#
# [1277] Count Square Submatrices with All Ones
#
# https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/
#
# algorithms
# Medium (67.25%)
# Likes:    135
# Dislikes: 5
# Total Accepted:    5.3K
# Total Submissions: 7.8K
# Testcase Example:  '[[0,1,1,1],[1,1,1,1],[0,1,1,1]]'
#
# Given a m * n matrix of ones and zeros, return how many square submatrices
# have all ones.
# 
# 
# Example 1:
# 
# 
# Input: matrix =
# [
# [0,1,1,1],
# [1,1,1,1],
# [0,1,1,1]
# ]
# Output: 15
# Explanation: 
# There are 10 squares of side 1.
# There are 4 squares of side 2.
# There is  1 square of side 3.
# Total number of squares = 10 + 4 + 1 = 15.
# 
# 
# Example 2:
# 
# 
# Input: matrix = 
# [
# ⁠ [1,0,1],
# ⁠ [1,1,0],
# ⁠ [1,1,0]
# ]
# Output: 7
# Explanation: 
# There are 6 squares of side 1.  
# There is 1 square of side 2. 
# Total number of squares = 6 + 1 = 7.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 300
# 1 <= arr[0].length <= 300
# 0 <= arr[i][j] <= 1
# 
# 
#

# @lc code=start
# from lcpy import List
# from pprint import pprint
class Solution:

    def get_sum(self, matrix):
        """
        return sum of binary matrices
        """
        # pprint(matrix)
        return sum(sum(r) for r in matrix)

    def countSquares(self, matrix):
        """
        starting square size
        s = min(m, n)
        print(self.get_sum(matrix))
        count square of 2 and also output a matrix if 
        there's a sqaure matrix with length 2
        """
        total = 0
        ones = self.get_sum(matrix)
        n_rows = len(matrix)
        n_cols = len(matrix[0])
        def recur(matrix, n_rows, n_cols):
            # n_rows = len(matrix)
            # n_cols = len(matrix[0])
            # print(n_rows, n_cols)
            n = 0
            output_m = [[0] * (n_cols - 1) for i in range(n_rows - 1)]
            for r in range(n_rows - 1):
                for c in range(n_cols - 1):
                    if matrix[r][c] == 1 and matrix[r][c+1] == 1 and \
                       matrix[r+1][c] == 1 and matrix[r+1][c+1] == 1:
                        n += 1
                        output_m[r][c] = 1
            return n, output_m, n_rows-1, n_cols-1
        
        for i in range(min(n_rows, n_cols)-1):
            n, matrix, n_rows, n_cols = recur(matrix, n_rows=n_rows, n_cols=n_cols)
            total += n
        # print(total)
        # print(recur(matrix))
        return total + ones
# @lc code=end
