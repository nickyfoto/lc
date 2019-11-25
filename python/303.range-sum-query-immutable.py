#
# @lc app=leetcode id=303 lang=python3
#
# [303] Range Sum Query - Immutable
#
# https://leetcode.com/problems/range-sum-query-immutable/description/
#
# algorithms
# Easy (37.48%)
# Total Accepted:    136.8K
# Total Submissions: 362.2K
# Testcase Example:  '["NumArray","sumRange","sumRange","sumRange"]\n[[[-2,0,3,-5,2,-1]],[0,2],[2,5],[0,5]]'
#
# Given an integer array nums, find the sum of the elements between indices i
# and j (i ≤ j), inclusive.
# 
# Example:
# 
# Given nums = [-2, 0, 3, -5, 2, -1]
# 
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# 
# 
# 
# Note:
# 
# You may assume that the array does not change.
# There are many calls to sumRange function.
# 
# 
#
class NumArray:

    # def __init__(self, nums: List[int]):
    def __init__(self, nums):
        self.nums = nums
        self.L = self.sumArray(nums)
    # def sumRange(self, i: int, j: int) -> int:
    def sumArray(self, nums):
        n = len(nums)
        if n < 1:
            return []
        L = [0] * n
        L[0] = nums[0]
        for i in range(1, n):
            L[i] = L[i-1] + nums[i]
        # print(L)
        return L
    def sumRange(self, i, j):
        if i == 0:
            return self.L[j]
        else:
            return self.L[j] - self.L[i-1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

# a = [-2, 0, 3, -5, 2, -1]
# s = NumArray(a)
# print(s.sumRange(0, 2))
# print(s.sumRange(2, 5))
# print(s.sumRange(0, 5))
# a = []
# s =NumArray(a)

