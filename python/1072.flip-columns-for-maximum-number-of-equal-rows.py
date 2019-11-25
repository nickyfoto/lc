#
# @lc app=leetcode id=1072 lang=python3
#
# [1072] Flip Columns For Maximum Number of Equal Rows
#
# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/description/
#
# algorithms
# Medium (58.11%)
# Total Accepted:    5.6K
# Total Submissions: 9.6K
# Testcase Example:  '[[0,1],[1,1]]'
#
# Given a matrix consisting of 0s and 1s, we may choose any number of columns
# in the matrix and flip every cell in that column.  Flipping a cell changes
# the value of that cell from 0 to 1 or from 1 to 0.
# 
# Return the maximum number of rows that have all values equal after some
# number of flips.
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
# Input: [[0,1],[1,1]]
# Output: 1
# Explanation: After flipping no values, 1 row has all values equal.
# 
# 
# 
# Example 2:
# 
# 
# Input: [[0,1],[1,0]]
# Output: 2
# Explanation: After flipping values in the first column, both rows have equal
# values.
# 
# 
# 
# Example 3:
# 
# 
# Input: [[0,0,0],[0,0,1],[1,1,0]]
# Output: 2
# Explanation: After flipping values in the first two columns, the last two
# rows have equal values.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= matrix.length <= 300
# 1 <= matrix[i].length <= 300
# All matrix[i].length's are equal
# matrix[i][j] is 0 or 1
# 
# 
# 
# 
#
from collections import Counter
class Solution:
    # def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
    def maxEqualRowsAfterFlips2(self, matrix) -> int:
        
        def flip(c):
            for r in range(n_row):
                matrix[r][c] = 1 - matrix[r][c]
        def worth_flip(c):
            score = 0
            for r in range(n_row):
                number_of_ones = sum(matrix[r])
                number_of_zeros = n_col - number_of_ones
                if matrix[r][c] == 0:    
                    if number_of_ones >= number_of_zeros:
                        score += 1
                else:
                    if number_of_zeros >= number_of_ones:
                        score += 1
            if score > n_row - score:
                return True
            return False
                
        n_row = len(matrix)
        n_col = len(matrix[0])
        
        for c in range(n_col):
            w = worth_flip(c)
            print(c, w)
            if w:
                flip(c)
            # r: (number of 0s, number of 1s )
            # table[r] = (n_col - sum(matrix[r], sum(matrix[r])))
        res = 0
        for r in range(n_row):
            row_sum = sum(matrix[r])
            if row_sum == n_col or row_sum == 0:
                res += 1
        return res

    def maxEqualRowsAfterFlips1(self, matrix) -> int:

        n_rows = len(matrix)
        n_cols = len(matrix[0])
        num_of_natural_equal = 0
        
        for r in range(n_rows):
            if sum(matrix[r]) == n_cols or sum(matrix[r]) == 0:
                num_of_natural_equal += 1

        number_of_equal_or_flip_equal = [1] * n_rows
        for r in range(n_rows):
            for i in range(r+1, n_rows):
                if matrix[i] == matrix[r] or [1-x for x in matrix[i]] == matrix[r]:
                    number_of_equal_or_flip_equal[r] += 1
        print(num_of_natural_equal)
        print(number_of_equal_or_flip_equal)
        return max(num_of_natural_equal, max(number_of_equal_or_flip_equal))

    def maxEqualRowsAfterFlips(self, matrix) -> int:

        n_rows = len(matrix)
        n_cols = len(matrix[0])
        num_of_natural_equal = 0
        
        for r in range(n_rows):
            if sum(matrix[r]) == n_cols or sum(matrix[r]) == 0:
                num_of_natural_equal += 1

        c = Counter([tuple(t) for t in matrix])
        c_flip = {}
        for k in c:
            complement = tuple([1-x for x in k])
            if complement in c:
                c_flip[complement] = c[complement]

        # print(num_of_natural_equal)
        # print([v for k,v in c_flip.items()])
        # print(c)
        # print(c_flip)
        for k in c:
            complement = tuple([1-x for x in k])
            if complement in c_flip:
                c[k] += c_flip[complement]

        # print([v for k,v in c.items()])
        # print
        return max(num_of_natural_equal, max(c.values()))


# s = Solution()
# matrix = [[0,0,0],[0,0,1],[1,1,0]]
# print(s.maxEqualRowsAfterFlips(matrix) == 2)


# matrix = [[0,1],[1,1]]
# print(s.maxEqualRowsAfterFlips(matrix) == 1)



# matrix = [[0,1],[1,0]]
# print(s.maxEqualRowsAfterFlips(matrix) == 2) 

# # #           #T       T       T
# # #           #F F F T F F F T F F F
# matrix = [[1,0,0,0,1,1,1,0,1,1,1],
#           [1,0,0,0,1,0,0,0,1,0,0],
#           [1,0,0,0,1,1,1,0,1,1,1],
#           [1,0,0,0,1,0,0,0,1,0,0],
#           [1,1,1,0,1,1,1,0,1,1,1]]
# print(s.maxEqualRowsAfterFlips(matrix) == 2) # expect 2
# print(sorted(matrix))

        
  # ✘ Time Limit Exceeded
  # ✘ 73/84 cases passed (N/A)

# matrix = [[1,1],
#  [0,1],
#  [1,0],
#  [0,0],
#  [1,0],
#  [1,0],
#  [0,1],
#  [1,0],
#  [0,0],
#  [1,0]]
# print(s.maxEqualRowsAfterFlips(matrix) == 7) # 7
