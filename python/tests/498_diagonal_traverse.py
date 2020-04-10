#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#
# https://leetcode.com/problems/diagonal-traverse/description/
#
# algorithms
# Medium (46.69%)
# Likes:    608
# Dislikes: 293
# Total Accepted:    69.6K
# Total Submissions: 148.6K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of M x N elements (M rows, N columns), return all elements of
# the matrix in diagonal order as shown in the below image.
# 
# 
# 
# Example:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 
# Output:  [1,2,4,7,5,3,6,8,9]
# 
# Explanation:
# 
# 
# 
# 
# 
# Note:
# 
# The total number of elements of the given matrix will not exceed 10,000.
# 
#

# @lc code=start
class Solution:
    # def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
    def findDiagonalOrder(self, matrix):
        if not matrix or not matrix[0]: return []
        m, n = len(matrix), len(matrix[0])
        arr = [0] * (m * n)
        r = c = 0
        for i in range(m * n):
            arr[i] = matrix[r][c]
            if (r + c) % 2 == 0: #moving up
                # condition 'c == n - 1' must before 'r == 0'
                if c == n - 1: 
                    r += 1
                elif r == 0:
                    c += 1
                else:
                    r -= 1
                    c += 1
            else:
                if r == m - 1:
                    c += 1
                elif c == 0:
                    r += 1
                else:
                    r += 1
                    c -= 1
        return arr
# @lc code=end
