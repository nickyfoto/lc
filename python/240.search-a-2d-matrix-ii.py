#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#
# https://leetcode.com/problems/search-a-2d-matrix-ii/description/
#
# algorithms
# Medium (41.31%)
# Total Accepted:    204.9K
# Total Submissions: 495.2K
# Testcase Example:  '[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]\n5'
#
# Write an efficient algorithm that searches for a value in an m x n matrix.
# This matrix has the following properties:
# 
# 
# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# 
# 
# Example:
# 
# Consider the following matrix:
# 
# 
# [
# ⁠ [1,   4,  7, 11, 15],
# ⁠ [2,   5,  8, 12, 19],
# ⁠ [3,   6,  9, 16, 22],
# ⁠ [10, 13, 14, 17, 24],
# ⁠ [18, 21, 23, 26, 30]
# ]
# 
# 
# Given target = 5, return true.
# 
# Given target = 20, return false.
# 
#
import bisect
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        m = len(matrix)
        n = len(matrix[0])
        if n == 0:
            return False
        last_col = [matrix[r][-1] for r in range(m)]
        # print(last_col)
        starting_row = bisect.bisect_left(last_col, target)

        first_col = [matrix[r][0] for r in range(m)]
        
        end_row = bisect.bisect_right(first_col, target)
        for r in range(starting_row, end_row):
            # print(target, matrix[r])
            right_idx = bisect.bisect_right(matrix[r], target)

            if matrix[r][right_idx-1] == target:
                return True
        return False

# s = Solution()

# matrix = [
# [1,   4,  7, 11, 15],
# [2,   5,  8, 12, 19],
# [3,   6,  9, 16, 22],
# [10, 13, 14, 17, 24],
# [18, 21, 23, 26, 30]
# ]

# target = 5

# print(s.searchMatrix(matrix, target))

# target = 20
# print(s.searchMatrix(matrix, target))

