#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
# https://leetcode.com/problems/sort-colors/description/
#
# algorithms
# Medium (43.08%)
# Total Accepted:    353.7K
# Total Submissions: 819K
# Testcase Example:  '[2,0,2,1,1,0]'
#
# Given an array with n objects colored red, white or blue, sort them in-place
# so that objects of the same color are adjacent, with the colors in the order
# red, white and blue.
# 
# Here, we will use the integers 0, 1, and 2 to represent the color red, white,
# and blue respectively.
# 
# Note: You are not suppose to use the library's sort function for this
# problem.
# 
# Example:
# 
# 
# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# 
# Follow up:
# 
# 
# A rather straight forward solution is a two-pass algorithm using counting
# sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite
# array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?
# 
# 
#
class Solution:
    # def sortColors(self, nums: List[int]) -> None:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = 1
        n = len(nums)
        left, right = 0, n - 1
        while nums[left] < pivot:
            left += 1
            if left > right:
                break
        while nums[right] > pivot:
            right -= 1
            if left > right:
                break
        # print(left, right)
        i = left
        while left <= right:
            if nums[i] < pivot:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
            elif nums[i] > pivot:
                if i < right:
                    nums[i], nums[right] = nums[right], nums[i]
                    right -= 1
                    while nums[right] > pivot:
                        right -= 1
            # print('i=', i, nums)
            if nums[i] >= 1:
                i += 1
            if i == left:
                i += 1
            if i == len(nums):
                break
#         print(nums)
#         # return nums

# s = Solution()
# nums = [2,0,2,1,1,0]
# print(s.sortColors(nums))
# nums = [0]
# print(s.sortColors(nums))

# nums = [2,0,1]
# print(s.sortColors(nums))
# nums = [0,1]
# print(s.sortColors(nums))

# nums = [1,2,0]
# print(s.sortColors(nums))





