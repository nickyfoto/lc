#
# @lc app=leetcode id=598 lang=python3
#
# [598] Range Addition II
#
# https://leetcode.com/problems/range-addition-ii/description/
#
# algorithms
# Easy (48.62%)
# Total Accepted:    30.7K
# Total Submissions: 63.1K
# Testcase Example:  '3\n3\n[[2,2],[3,3]]'
#
# Given an m * n matrix M initialized with all 0's and several update
# operations.
# Operations are represented by a 2D array, and each operation is represented
# by an array with two positive integers a and b, which means M[i][j] should be
# added by one for all 0  and 0 . 
# You need to count and return the number of maximum integers in the matrix
# after performing all the operations.
# 
# Example 1:
# 
# Input: 
# m = 3, n = 3
# operations = [[2,2],[3,3]]
# Output: 4
# Explanation: 
# Initially, M = 
# [[0, 0, 0],
# ⁠[0, 0, 0],
# ⁠[0, 0, 0]]
# 
# After performing [2,2], M = 
# [[1, 1, 0],
# ⁠[1, 1, 0],
# ⁠[0, 0, 0]]
# 
# After performing [3,3], M = 
# [[2, 2, 1],
# ⁠[2, 2, 1],
# ⁠[1, 1, 1]]
# 
# So the maximum integer in M is 2, and there are four of it in M. So return
# 4.
# 
# 
# 
# Note:
# 
# The range of m and n is [1,40000].
# The range of a is [1,m], and the range of b is [1,n].
# The range of operations size won't exceed 10,000.
# 
# 
#
class Solution:
    # def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
    def maxCount(self, m, n, ops):
        if not ops:
            return m * n
        # print(len(ops))
        # if len(ops) == 1:
        #     return ops[0][0] * ops[0][1]
        return min([op[0] for op in ops]) * min([op[1] for op in ops])
        # matrix = [[0 for i in range(n)] for j in range(m)]
        # max_val = 0
        # count = 0
        # for op in ops:
        #     for row in range(op[0]):
        #         for col in range(op[1]):
        #             matrix[row][col] += 1
        #             if matrix[row][col] > max_val:
        #                 max_val = matrix[row][col]
        #                 count = 1
        #             elif matrix[row][col] == max_val:
        #                 count += 1
        # return count

# s = Solution()

# print(s.maxCount(3, 3, [[2,2],[3,3]]))
# print(s.maxCount(39999,
#                  39999,
#                  [[19999,19999]]))

# print(s.maxCount(26797,
#                  12287,
#                  [[18717,11856],[3154,2135],[561,10977],[14679,3527],[17166,1028],[20980,3893],[13125,7906],[23463,6555],[8173,2966],[18316,12040],[22715,6802],[13774,6466],[22370,4428],[23389,8396],[1436,8292],[26525,8913],[19736,9021],[6483,4026]]
#                 ))











