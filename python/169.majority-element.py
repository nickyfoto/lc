#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#
# https://leetcode.com/problems/majority-element/description/
#
# algorithms
# Easy (52.22%)
# Total Accepted:    378.2K
# Total Submissions: 720.6K
# Testcase Example:  '[3,2,3]'
#
# Given an array of size n, find the majority element. The majority element is
# the element that appears more than ⌊ n/2 ⌋ times.
# 
# You may assume that the array is non-empty and the majority element always
# exist in the array.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: 3
# 
# Example 2:
# 
# 
# Input: [2,2,1,1,1,2,2]
# Output: 2
# 
# 
#
class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    def majorityElement(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]
        mid = n // 2
        first = nums[:mid]
        second = nums[mid:]
        fm = self.majorityElement(first)
        sm = self.majorityElement(second)    
        if fm == sm:
            return fm
        else:
            fmc = nums.count(fm)
            smc = nums.count(sm)
            if fmc > mid:
                return fm
            if smc > mid:
                return sm
            return None


# s = Solution()
# a = [3,2,3]
# print(s.majorityElement(a))
# a = [2,2,1,1,1,2,2]
# print(s.majorityElement(a))
# a = [1,1,2,2,2]
# print(s.majorityElement(a))
# a = [2,1,1,2,2]
# print(s.majorityElement(a))
# a = [1,2,1,1,2,2]
# print(s.majorityElement(a))
