#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# https://leetcode.com/problems/search-insert-position/description/
#
# algorithms
# Easy (40.71%)
# Total Accepted:    396.4K
# Total Submissions: 971.6K
# Testcase Example:  '[1,3,5,6]\n5'
#
# Given a sorted array and a target value, return the index if the target is
# found. If not, return the index where it would be if it were inserted in
# order.
# 
# You may assume no duplicates in the array.
# 
# Example 1:
# 
# 
# Input: [1,3,5,6], 5
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [1,3,5,6], 2
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: [1,3,5,6], 7
# Output: 4
# 
# 
# Example 4:
# 
# 
# Input: [1,3,5,6], 0
# Output: 0
# 
# 
#
class Solution:
    # def searchInsert(self, nums: List[int], target: int) -> int:
    def searchInsert(self, nums, target):
        n = len(nums)
        if n < 1:
            return 0
        if n == 1:
            if target <= nums[0]:
                return 0
            else:
                return 1
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return n
        mid = n // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.searchInsert(nums[:mid], target)
        else:
            return mid + self.searchInsert(nums[mid:], target)


# # 
# s = Solution()
# nums = [1,3,5,6]
# t = 5
# # Output: 2
# print(s.searchInsert(nums, t)==2)
# # 
# # 
# # Example 2:
# # 
# # 
# nums = [1,3,5,6]
# t = 2
# # Output: 1
# print(s.searchInsert(nums, t)==1)
# # 
# # Example 3:
# # 
# # 
# nums = [1,3,5,6]
# t = 7
# # Output: 4
# print(s.searchInsert(nums, t)==4)
# # 
# # Example 4:
# # 
# # 
# nums = [1,3,5,6]
# t = 0
# # Output: 0
# print(s.searchInsert(nums, t)==0)













