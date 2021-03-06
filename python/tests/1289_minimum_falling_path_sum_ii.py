#
# @lc app=leetcode id=1289 lang=python3
#
# [1289] Minimum Falling Path Sum II
#
# https://leetcode.com/problems/minimum-falling-path-sum-ii/description/
#
# algorithms
# Hard (57.67%)
# Likes:    77
# Dislikes: 10
# Total Accepted:    4.4K
# Total Submissions: 7.7K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a square grid of integers arr, a falling path with non-zero shifts is a
# choice of exactly one element from each row of arr, such that no two elements
# chosen in adjacent rows are in the same column.
# 
# Return the minimum sum of a falling path with non-zero shifts.
# 
# 
# Example 1:
# 
# 
# Input: arr = [[1,2,3],[4,5,6],[7,8,9]]
# Output: 13
# Explanation: 
# The possible falling paths are:
# [1,5,9], [1,5,7], [1,6,7], [1,6,8],
# [2,4,8], [2,4,9], [2,6,7], [2,6,8],
# [3,4,8], [3,4,9], [3,5,7], [3,5,9]
# The falling path with the smallest sum is [1,5,7], so the answer is 13.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length == arr[i].length <= 200
# -99 <= arr[i][j] <= 99
# 
# 
#

# @lc code=start
import heapq
class Solution:
    # def minFallingPathSum(self, arr: List[List[int]]) -> int:
    def minFallingPathSum(self, arr):
        n = len(arr)
        for r in range(1, n):
            sm2 = heapq.nsmallest(2, arr[r - 1])
            for c in range(n):
                arr[r][c] += sm2[1] if arr[r-1][c] == sm2[0] else sm2[0]
        return min(arr[-1])
# @lc code=end
