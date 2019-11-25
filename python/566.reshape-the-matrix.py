#
# @lc app=leetcode id=566 lang=python3
#
# [566] Reshape the Matrix
#
# https://leetcode.com/problems/reshape-the-matrix/description/
#
# algorithms
# Easy (58.96%)
# Total Accepted:    79.8K
# Total Submissions: 135K
# Testcase Example:  '[[1,2],[3,4]]\n1\n4'
#
# In MATLAB, there is a very useful function called 'reshape', which can
# reshape a matrix into a new one with different size but keep its original
# data.
# 
# 
# 
# You're given a matrix represented by a two-dimensional array, and two
# positive integers r and c representing the row number and column number of
# the wanted reshaped matrix, respectively.
# 
# ⁠The reshaped matrix need to be filled with all the elements of the original
# matrix in the same row-traversing order as they were.
# 
# 
# 
# If the 'reshape' operation with given parameters is possible and legal,
# output the new reshaped matrix; Otherwise, output the original matrix.
# 
# 
# Example 1:
# 
# Input: 
# nums = 
# [[1,2],
# ⁠[3,4]]
# r = 1, c = 4
# Output: 
# [[1,2,3,4]]
# Explanation:The row-traversing of nums is [1,2,3,4]. The new reshaped matrix
# is a 1 * 4 matrix, fill it row by row by using the previous list.
# 
# 
# 
# Example 2:
# 
# Input: 
# nums = 
# [[1,2],
# ⁠[3,4]]
# r = 2, c = 4
# Output: 
# [[1,2],
# ⁠[3,4]]
# Explanation:There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So
# output the original matrix.
# 
# 
# 
# Note:
# 
# The height and width of the given matrix is in range [1, 100].
# The given r and c are all positive.
# 
# 
#
from functools import reduce
class Solution:
    # def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
    def matrixReshape(self, nums, r, c):
        n_rows = len(nums)
        n_cols = len(nums[0])
        if r * c != n_rows * n_cols:
            return nums
        elif r == n_rows and c == n_cols:
            return nums
        else:
            res = [[] for i in range(r)]
            nums = reduce(lambda x, y: x+y, nums)
            # print(list(nums))
            for i in range(r):
                # print(i*c,i*c+c)
                res[i] = nums[i*c:i*c+c]

                                                                        # 0 0:2
                                                                        # 1 2:4
                                                                        # 2 0:2
                                                                        # 3 2:4
        return res

# s = Solution()
# nums = [[1,2],[3,4]]
# r = 1
# c = 4
# print(s.matrixReshape(nums, r, c))

# nums = [[1,2],[3,4],[5,6],[7,8]]
# r = 2
# c = 4
# print(s.matrixReshape(nums, r, c))

# nums = [[1,2,3,4], [5,6,7,8]]
# r = 4
# c = 2
# print(s.matrixReshape(nums, r, c))


# nums = [[0,1,2,3],
#         [4,5,6,7],
#         [8,9,10,11]]
# r = 4
# c = 3
# print(s.matrixReshape(nums, r, c))

# nums = [[0,1,2],
#         [3,4,5],
#         [6,7,8],
#         [9,10,11]]
# r = 3
# c = 4
# print(s.matrixReshape(nums, r, c))

