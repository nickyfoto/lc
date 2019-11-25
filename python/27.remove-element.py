#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
# https://leetcode.com/problems/remove-element/description/
#
# algorithms
# Easy (44.71%)
# Total Accepted:    423.6K
# Total Submissions: 945.7K
# Testcase Example:  '[3,2,2,3]\n3'
#
# Given an array nums and a value val, remove all instances of that value
# in-place and return the new length.
# 
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
# 
# The order of elements can be changed. It doesn't matter what you leave beyond
# the new length.
# 
# Example 1:
# 
# 
# Given nums = [3,2,2,3], val = 3,
# 
# Your function should return length = 2, with the first two elements of nums
# being 2.
# 
# It doesn't matter what you leave beyond the returned length.
# 
# 
# Example 2:
# 
# 
# Given nums = [0,1,2,2,3,0,4,2], val = 2,
# 
# Your function should return length = 5, with the first five elements of nums
# containing 0, 1, 3, 0, and 4.
# 
# Note that the order of those five elements can be arbitrary.
# 
# It doesn't matter what values are set beyond the returned length.
# 
# Clarification:
# 
# Confused why the returned value is an integer but your answer is an array?
# 
# Note that the input array is passed in by reference, which means modification
# to the input array will be known to the caller as well.
# 
# Internally you can think of this:
# 
# 
# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeElement(nums, val);
# 
# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len
# elements.
# for (int i = 0; i < len; i++) {
# print(nums[i]);
# }
# 
#
class Solution:
    # def removeElement(self, nums: List[int], val: int) -> int:
    def removeElement(self, nums, val):
        num_swap = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == val:
                j = i+1
                while j < n and nums[j] == val:
                    j += 1
                if j < n:
                    nums[i], nums[j] = nums[j], nums[i]
                    num_swap += 1
                    # print('i=', i, 'j=', j, nums, num_swap)
            else:
                num_swap += 1
        nums = nums[:num_swap]
        # print('final', nums)
        return num_swap

# s = Solution()
# nums = [3,2,2,3]
# val = 3
# print(s.removeElement(nums, val))
        
# nums = [0,1,2,2,3,0,4,2]
# val = 2
# print(s.removeElement(nums, val))
