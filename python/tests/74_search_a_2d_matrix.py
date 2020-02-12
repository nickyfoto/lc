#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (35.81%)
# Likes:    1285
# Dislikes: 138
# Total Accepted:    282.9K
# Total Submissions: 789.6K
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,50]]\n3'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
# 
# 
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the
# previous row.
# 
# 
# Example 1:
# 
# 
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 3
# Output: true
# 
# 
# Example 2:
# 
# 
# Input:
# matrix = [
# ⁠ [1,   3,  5,  7],
# ⁠ [10, 11, 16, 20],
# ⁠ [23, 30, 34, 50]
# ]
# target = 13
# Output: false
# 
#

# @lc code=start
from bisect import bisect_left
class Solution:
    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        i = bisect_left(matrix, [target])
        print(i)
        if i < len(matrix) and target == matrix[i][0]:
            return True
        if i > 0:
            i -= 1
        idx = bisect_left(matrix[i], target)
        if idx == len(matrix[i]):
            return False
        return target == matrix[i][idx]
# @lc code=end
