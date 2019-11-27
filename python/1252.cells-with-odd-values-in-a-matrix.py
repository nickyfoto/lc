#
# @lc app=leetcode id=1252 lang=python3
#
# [1252] Cells with Odd Values in a Matrix
#
# https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/description/
#
# algorithms
# Easy (78.56%)
# Likes:    70
# Dislikes: 53
# Total Accepted:    10.9K
# Total Submissions: 14K
# Testcase Example:  '2\n3\n[[0,1],[1,1]]'
#
# Given n and m which are the dimensions of a matrix initialized by zeros and
# given an array indices where indices[i] = [ri, ci]. For each pair of [ri, ci]
# you have to increment all cells in row ri and column ci by 1.
# 
# Return the number of cells with odd values in the matrix after applying the
# increment to all indices.
# 
# 
# Example 1:
# 
# 
# Input: n = 2, m = 3, indices = [[0,1],[1,1]]
# Output: 6
# Explanation: Initial matrix = [[0,0,0],[0,0,0]].
# After applying first increment it becomes [[1,2,1],[0,1,0]].
# The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.
# 
# 
# Example 2:
# 
# 
# Input: n = 2, m = 2, indices = [[1,1],[0,0]]
# Output: 0
# Explanation: Final matrix = [[2,2],[2,2]]. There is no odd number in the
# final matrix.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 50
# 1 <= m <= 50
# 1 <= indices.length <= 100
# 0 <= indices[i][0] < n
# 0 <= indices[i][1] < m
# 
# 
#

# @lc code=start
class Solution:
    # def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
    def oddCells(self, n: int, m: int, indices) -> int:
        # print('ok')
        matrix = [[0] * m for i in range(n)]
        # print(matrix)
        for r, c in indices:
            # print(r, c)
            # update row
            matrix[r] = [x+1 for x in matrix[r]]
            for r in matrix:
                r[c] += 1
        # print(matrix)
        res = 0
        for r in range(n):
            for c in range(m):
                if matrix[r][c] % 2 != 0:
                    res += 1
        return res
# @lc code=end


# n = 2
# m = 3
# indices = [[0,1],[1,1]]
# s = Solution()
# print(s.oddCells(n, m, indices))

# n = 2
# m = 2
# indices = [[1,1],[0,0]]
# print(s.oddCells(n, m, indices))