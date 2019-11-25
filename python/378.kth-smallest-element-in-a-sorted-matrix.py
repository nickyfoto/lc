#
# @lc app=leetcode id=378 lang=python3
#
# [378] Kth Smallest Element in a Sorted Matrix
#
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
#
# algorithms
# Medium (50.48%)
# Total Accepted:    126.3K
# Total Submissions: 249.8K
# Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
#
# Given a n x n matrix where each of the rows and columns are sorted in
# ascending order, find the kth smallest element in the matrix.
# 
# 
# Note that it is the kth smallest element in the sorted order, not the kth
# distinct element.
# 
# 
# Example:
# 
# matrix = [
# ⁠  [ 1,  5,  9],
# ⁠  [10, 11, 13],
# ⁠  [12, 13, 15]
# ],
# k = 8,
# 
# return 13.
# 
# 
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ n2.
#
import bisect
class Solution:
    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    def kthSmallest(self, matrix, k: int) -> int:
        # print(matrix)
        n = len(matrix[0])
        k -= 1
        # q, r = divmod(k, col_length)
        # print(q, r)
        # return matrix[q][r]
        l = matrix[0]
        for r in range(1,n):
            for i in matrix[r]:
                bisect.insort(l, i)
        # print(l)
        # print(k)
        return l[k]



# s = Solution()
# matrix = [
# [ 1,  5,  9],
# [10, 11, 13],
# [12, 13, 15]]
# k = 8
# print(s.kthSmallest(matrix, k)) 


# matrix = [[1,2],[1,3]]
# k = 2        
# print(s.kthSmallest(matrix, k)) # 1
# k = 1       
# print(s.kthSmallest(matrix, k)) # 1












