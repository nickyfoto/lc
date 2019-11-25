#
# @lc app=leetcode id=561 lang=python3
#
# [561] Array Partition I
#
# https://leetcode.com/problems/array-partition-i/description/
#
# algorithms
# Easy (69.19%)
# Total Accepted:    148.4K
# Total Submissions: 214.2K
# Testcase Example:  '[1,4,3,2]'
#
# 
# Given an array of 2n integers, your task is to group these integers into n
# pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of
# min(ai, bi) for all i from 1 to n as large as possible.
# 
# 
# Example 1:
# 
# Input: [1,4,3,2]
# 
# Output: 4
# Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3,
# 4).
# 
# 
# 
# Note:
# 
# n is a positive integer, which is in the range of [1, 10000].
# All the integers in the array will be in the range of [-10000, 10000].
# 
# 
#
class Solution:
    # def arrayPairSum(self, nums: List[int]) -> int:
    def arrayPairSum(self, nums):
        nums.sort()
        n = len(nums)
        # print([nums[i] for i in range(n) if n % 2 == 0])
        return sum([nums[i] for i in range(n) if i % 2 == 0])

# s = Solution()
# nums = [1,4,3,2]
# print(s.arrayPairSum(nums))
        
