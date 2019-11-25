#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
#
# algorithms
# Easy (40.89%)
# Total Accepted:    616.7K
# Total Submissions: 1.5M
# Testcase Example:  '[1,1,2]'
#
# Given a sorted array nums, remove the duplicates in-place such that each
# element appear only once and return the new length.
# 
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
# 
# Example 1:
# 
# 
# Given nums = [1,1,2],
# 
# Your function should return length = 2, with the first two elements of nums
# being 1 and 2 respectively.
# 
# It doesn't matter what you leave beyond the returned length.
# 
# Example 2:
# 
# 
# Given nums = [0,0,1,1,1,2,2,3,3,4],
# 
# Your function should return length = 5, with the first five elements of nums
# being modified to 0, 1, 2, 3, and 4 respectively.
# 
# It doesn't matter what values are set beyond the returned length.
# 
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
# int len = removeDuplicates(nums);
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
    # def removeDuplicates(self, nums: List[int]) -> int:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        n = len(nums)
        p1 = 0
        target = nums[p1]
        num_unique = 0
        while p1 < n:
            p2 = 1
            while p1+p2 < len(nums) and nums[p1+p2] == target:
                p2 += 1
            p1 += p2
            num_unique += 1
            if p1 < n:
                nums[num_unique], nums[p1] = nums[p1], nums[num_unique]
                target = nums[num_unique]
            # print(num_unique, p1, 'target=', target)
        # print(nums)
        nums = nums[:num_unique]
        # print(nums)
        return num_unique
        # p1 = 0
        # while p1 < n:
        #     p2 = 1
        #     while p1 + p2 < len(nums) and nums[p1+p2] == nums[p1]:
        #         p2 += 1
        #     p1 += p2
        #     num_unique += 1
        #     print(p1, p2)

        # print(nums)
        # return num_unique



# s = Solution()
# nums = [1,1,2]
# print(s.removeDuplicates(nums))

# nums = [0,0,1,1,1,2,2,3,3,4]
# print(s.removeDuplicates(nums))
