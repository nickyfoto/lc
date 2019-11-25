#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
# https://leetcode.com/problems/missing-number/description/
#
# algorithms
# Easy (48.06%)
# Total Accepted:    273.8K
# Total Submissions: 566.5K
# Testcase Example:  '[3,0,1]'
#
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
# the one that is missing from the array.
# 
# Example 1:
# 
# 
# Input: [3,0,1]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [9,6,4,2,3,5,7,0,1]
# Output: 8
# 
# 
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement
# it using only constant extra space complexity?
#
class Solution:
    # def missingNumber(self, nums: List[int]) -> int:

    def missingNumber(self, nums):
        # if nums == [0]:
            # return 1
        nums.sort()
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return nums[-1]+1


# s = Solution()
# nums = [3,0,1]
# print(s.missingNumber(nums))

# nums = [1,2,3]
# print(s.missingNumber(nums))

# nums = [9,6,4,2,3,5,7,0,1]
# print(s.missingNumber(nums))

# nums = [1,2]
# print(s.missingNumber(nums))

# nums = [0,2,3]
# print(s.missingNumber(nums))


# nums = [1,8,4,6,2,0,9,7,5]
# print(s.missingNumber(nums))
