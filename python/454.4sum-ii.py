#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#
# https://leetcode.com/problems/4sum-ii/description/
#
# algorithms
# Medium (51.45%)
# Total Accepted:    76.9K
# Total Submissions: 149.5K
# Testcase Example:  '[1,2]\n[-2,-1]\n[-1,2]\n[0,2]'
#
# Given four lists A, B, C, D of integer values, compute how many tuples (i, j,
# k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
# 
# To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤
# N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is
# guaranteed to be at most 231 - 1.
# 
# Example:
# 
# 
# Input:
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
# 
# Output:
# 2
# 
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
# 
# 
# 
# 
#
from collections import Counter
class Solution:
    # def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    def fourSumCount(self, A, B, C, D):

        
        # print(D)          
        # print(count)
        AB = Counter(a+b for a in A for b in B)
        return sum(AB[-c-d] for c in C for d in D)


# s = Solution()
# A = [ 1, 2]
# B = [-2,-1]
# C = [-1, 2]
# D = [ 0, 2]
# print(s.fourSumCount(A, B, C, D))
















        
