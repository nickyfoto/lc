#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
# https://leetcode.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (50.83%)
# Total Accepted:    214.9K
# Total Submissions: 422.7K
# Testcase Example:  '[1,3,4,2,2]'
#
# Given an array nums containing n + 1 integers where each integer is between 1
# and n (inclusive), prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
# 
# Example 1:
# 
# 
# Input: [1,3,4,2,2]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [3,1,3,4,2]
# Output: 3
# 
# Note:
# 
# 
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated
# more than once.
# 
# 
#
class Solution:
    # def findDuplicate(self, nums: List[int]) -> int:
    def findDuplicate(self, nums) -> int:
        # n = len(nums) - 1
        # res = sum(nums) - (1+n)*n // 2
        # return res
        for i in range(len(nums)):
            if nums[abs(nums[i])-1] > 0:
                nums[abs(nums[i])-1] = 0 - nums[abs(nums[i])-1]
            else:
                # print(nums[nums[i] - 1])
                # print('i=', i, nums[i])
                return abs(nums[i])
        # print(nums)

# s = Solution()
# nums = [1,3,4,2,2]
# print(s.findDuplicate(nums))
# nums = [3,1,3,4,2]
# print(s.findDuplicate(nums))

# nums = [2,2,2,2,2]
# print(s.findDuplicate(nums))
