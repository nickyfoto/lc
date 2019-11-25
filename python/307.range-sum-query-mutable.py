#
# @lc app=leetcode id=307 lang=python3
#
# [307] Range Sum Query - Mutable
#
# https://leetcode.com/problems/range-sum-query-mutable/description/
#
# algorithms
# Medium (29.73%)
# Total Accepted:    78.5K
# Total Submissions: 262.4K
# Testcase Example:  '["NumArray","sumRange","update","sumRange"]\n[[[1,3,5]],[0,2],[1,2],[0,2]]'
#
# Given an integer array nums, find the sum of the elements between indices i
# and j (i ≤ j), inclusive.
# 
# The update(i, val) function modifies nums by updating the element at index i
# to val.
# 
# Example:
# 
# 
# Given nums = [1, 3, 5]
# 
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8
# 
# 
# Note:
# 
# 
# The array is only modifiable by the update function.
# You may assume the number of calls to update and sumRange function is
# distributed evenly.
# 
# 
#
class NumArray:

    # def __init__(self, nums: List[int]):
    def __init__(self, nums):
        self.arr = nums

    def update(self, i: int, val: int) -> None:
        self.arr[i] = val

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.arr[i:j+1])


# Your NumArray object will be instantiated and called as such:
# nums = [1, 3, 5]
# obj = NumArray(nums)
# print(obj.sumRange(0,2))
# obj.update(1,2)
# print(obj.sumRange(0,2))
# param_2 = obj.sumRange(i,j)
