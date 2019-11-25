#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#
# https://leetcode.com/problems/find-pivot-index/description/
#
# algorithms
# Easy (41.26%)
# Total Accepted:    75.3K
# Total Submissions: 181.7K
# Testcase Example:  '[1,7,3,6,5,6]'
#
# Given an array of integers nums, write a method that returns the "pivot"
# index of this array.
# 
# We define the pivot index as the index where the sum of the numbers to the
# left of the index is equal to the sum of the numbers to the right of the
# index.
# 
# If no such index exists, we should return -1. If there are multiple pivot
# indexes, you should return the left-most pivot index.
# 
# Example 1:
# 
# 
# Input: 
# nums = [1, 7, 3, 6, 5, 6]
# Output: 3
# Explanation: 
# The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the
# sum of numbers to the right of index 3.
# Also, 3 is the first index where this occurs.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# nums = [1, 2, 3]
# Output: -1
# Explanation: 
# There is no index that satisfies the conditions in the problem
# statement.
# 
# 
# 
# 
# Note:
# 
# 
# The length of nums will be in the range [0, 10000].
# Each element nums[i] will be an integer in the range [-1000, 1000].
# 
# 
# 
# 
#
class Solution:
    # def pivotIndex(self, nums: List[int]) -> int:
    def pivotIndex(self, nums):
        n = len(nums)
        if n < 3:
            return -1
        pivot = 0
        s1 = sum(nums[:pivot])
        s2 = sum(nums[pivot+1:])
        # print(s1, s2)
        # for p in range(n):
        while pivot < n and s1 != s2:
            s1 += nums[pivot]
            pivot += 1
            # print(pivot)
            if pivot == n:
                return -1
            s2 -= nums[pivot]
        # print(pivot)
        return pivot

# s = Solution()
# nums = [1, 7, 3, 6, 5, 6]
# print(s.pivotIndex(nums))

# nums = [1, 2, 3]
# print(s.pivotIndex(nums))

# nums = [-1,-1,-1,0,1,1]
# print(s.pivotIndex(nums))