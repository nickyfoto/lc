#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#
# https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
#
# algorithms
# Medium (62.06%)
# Total Accepted:    109.6K
# Total Submissions: 176.6K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements
# appear twice and others appear once.
# 
# Find all the elements that appear twice in this array.
# 
# Could you do it without extra space and in O(n) runtime?
# 
# Example:
# 
# Input:
# [4,3,2,7,8,2,3,1]
# 
# Output:
# [2,3]
# 
#
class Solution:
    # def findDuplicates(self, nums: List[int]) -> List[int]:
    # def findDuplicates(self, nums):
        # n = len(nums)
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for x in nums:
            # print(abs(x)-1)
            if nums[abs(x)-1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x)-1] *= -1
            # print(nums, res)
        return res
# s = Solution()
# nums = [4,3,2,7,8,2,3,1]
# # nums = [4,3,6,7,8,2,5,1]
# print(s.findDuplicates(nums))