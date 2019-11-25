#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#
# https://leetcode.com/problems/single-number/description/
#
# algorithms
# Easy (60.36%)
# Total Accepted:    476.1K
# Total Submissions: 787.7K
# Testcase Example:  '[2,2,1]'
#
# Given a non-empty array of integers, every element appears twice except for
# one. Find that single one.
# 
# Note:
# 
# Your algorithm should have a linear runtime complexity. Could you implement
# it without using extra memory?
# 
# Example 1:
# 
# 
# Input: [2,2,1]
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: [4,1,2,1,2]
# Output: 4
# 
# 
#
class Solution:
    # def singleNumber(self, nums: List[int]) -> int:
    def singleNumber(self, nums):
        d = {}
        for num in nums:
            if num in d:
                del d[num]
            else:
                d[num] = None
        return list(d.keys())[0]


# s = Solution()
# nums = [2,2,1]
# print(s.singleNumber(nums))

# nums = [4,1,2,1,2]
# print(s.singleNumber(nums))
