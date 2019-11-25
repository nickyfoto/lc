#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#
# https://leetcode.com/problems/minimum-falling-path-sum/description/
#
# algorithms
# Medium (59.27%)
# Total Accepted:    23.4K
# Total Submissions: 39.5K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a square array of integers A, we want the minimum sum of a falling path
# through A.
# 
# A falling path starts at any element in the first row, and chooses one
# element from each row.  The next row's choice must be in a column that is
# different from the previous row's column by at most one.
# 
# 
# 
# Example 1:
# 
# 
# Input: [[1,2,3],[4,5,6],[7,8,9]]
# Output: 12
# Explanation: 
# The possible falling paths are:
# 
# 
# 
# [1,4,7], [1,4,8], [1,5,7], [1,5,8], [1,5,9]
# [2,4,7], [2,4,8], [2,5,7], [2,5,8], [2,5,9], [2,6,8], [2,6,9]
# [3,5,7], [3,5,8], [3,5,9], [3,6,8], [3,6,9]
# 
# 
# The falling path with the smallest sum is [1,4,7], so the answer is 12.
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length == A[0].length <= 100
# -100 <= A[i][j] <= 100
# 
#
class Solution:
    # def minFallingPathSum(self, A: List[List[int]]) -> int:
    def minFallingPathSum(self, A) -> int:
        n = len(A)
        # first_row = A[0]


        def getMin(r,c):
            if r == n-1:
                return A[r][c]
            else:
                if c == 0:
                    # print(A[r+1])
                    return A[r][c] + min(A[r+1][0:c+2])
                elif c == n - 1:
                    return A[r][c] + min(A[r+1][c-1:n])
                else:
                    return A[r][c] + min(A[r+1][c-1:c+2])

        for r in range(n-1, -1, -1):
            # print(A[r])
            for c in range(n):
                A[r][c] = getMin(r,c)

        # print(A)
        return min(A[0])





# s = Solution()
# A = [[1,2,3],[4,5,6],[7,8,9]]
# print(s.minFallingPathSum(A))






















