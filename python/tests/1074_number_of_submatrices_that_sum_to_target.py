#
# @lc app=leetcode id=1074 lang=python3
#
# [1074] Number of Submatrices That Sum to Target
#
# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/description/
#
# algorithms
# Hard (59.32%)
# Likes:    435
# Dislikes: 23
# Total Accepted:    14.1K
# Total Submissions: 23.7K
# Testcase Example:  '[[0,1,0],[1,1,1],[0,1,0]]\n0'
#
# Given a matrix, and a target, return the number of non-empty submatrices that
# sum to target.
# 
# A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x
# <= x2 and y1 <= y <= y2.
# 
# Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if
# they have some coordinate that is different: for example, if x1 != x1'.
# 
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
# Output: 4
# Explanation: The four 1x1 submatrices that only contain 0.
# 
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[1,-1],[-1,1]], target = 0
# Output: 5
# Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the
# 2x2 submatrix.
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= matrix.length <= 300
# 1 <= matrix[0].length <= 300
# -1000 <= matrix[i] <= 1000
# -10^8 <= target <= 10^8
# 
# 
#

# @lc code=start
from pprint import pprint
from collections import defaultdict
class Solution:
    def numSubmatrixSumTarget(self, matrix, target):
        m, n = len(matrix) + 1, len(matrix[0]) + 1
        prefix_sum = [[0] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                prefix_sum[i][j] = matrix[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]
        # pprint(prefix_sum, width=40)

        cnt = 0
        for r1 in range(1, m):
            for r2 in range(r1, m):
                h = defaultdict(int)
                h[0] = 1
                for col in range(1, n):
                    curr_sum = prefix_sum[r2][col] - prefix_sum[r1 - 1][col]
                    cnt += h[curr_sum - target]
                    # print(cnt, curr_sum - target, 'h[curr_sum - target]=', h[curr_sum - target], 'r1=', r1, 'r2=', r2)
                    # print(h)
                    h[curr_sum] += 1
            #print(r1, cnt)
        return cnt
# @lc code=end
