#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (35.89%)
# Total Accepted:    378.2K
# Total Submissions: 1M
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
# 
# Note:
# 
# 
# The number of elements initialized in nums1 and nums2 are m and n
# respectively.
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2.
# 
# 
# Example:
# 
# 
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# Output: [1,2,2,3,5,6]
# 
# 
#
class Solution:
    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        total = m + n
        while nums2:
            p = nums2.pop(0)
            while i < total and nums1[i] <= p:
                i += 1
            if i < m:
                # print(i)
                # temp = nums1[i]
                nums1[i+1:m+1] = nums1[i:m]
                nums1[i] = p
                # print(nums1)
                m += 1
            else:
                # print('i=', i, m)
                nums1[m] = p
                m += 1
        # print(nums1)
                # print(m)


# s = Solution()
# nums1 = [1,2,3,0,0,0]
# m = 3
# nums2 = [2,5,6]
# n = 3
# s.merge(nums1, m, nums2, n)
