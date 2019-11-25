#
# @lc app=leetcode id=448 lang=python3
#
# [448] Find All Numbers Disappeared in an Array
#
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
#
# algorithms
# Easy (53.52%)
# Total Accepted:    161.3K
# Total Submissions: 300.3K
# Testcase Example:  '[4,3,2,7,8,2,3,1]'
#
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some
# elements appear twice and others appear once.
# 
# Find all the elements of [1, n] inclusive that do not appear in this array.
# 
# Could you do it without extra space and in O(n) runtime? You may assume the
# returned list does not count as extra space.
# 
# Example:
# 
# Input:
# [4,3,2,7,8,2,3,1]
#  1 2 2 3 3 4 7 8
# Output:
# [5,6]
# 
# 
#
class Solution:
    # def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        miss = []
        # nums.sort()
        d = {}
        for i in nums:
            if i not in d:
                d[i] = None
        for i in range(1, n+1):
            if i not in d:
                miss.append(i)
        return miss
        # i = 0
        # while i < n:

