#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#
# https://leetcode.com/problems/intersection-of-two-arrays/description/
#
# algorithms
# Easy (54.07%)
# Total Accepted:    216.7K
# Total Submissions: 398.2K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# Given two arrays, write a function to compute their intersection.
# 
# Example 1:
# 
# 
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# 
# 
# Note:
# 
# 
# Each element in the result must be unique.
# The result can be in any order.
# 
# 
# 
# 
#
class Solution:
    # def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    def intersection(self, nums1, nums2):
        d1 = {}
        d2 = {}
        for i in nums1:
            if i not in d1:
                d1[i] = 0
        for i in nums2:
            if i not in d2:
                d2[i] = 0
        l1, l2 = len(d1), len(d2)
        if l1 < l2:
            for k in d1:
                if k in d2:
                    d1[k] = 1
            return [k for (k, v) in d1.items() if d1[k]]
        else:
            for k in d2:
                if k in d1:
                    d2[k] = 1
            return [k for (k, v) in d2.items() if d2[k]]

# s = Solution()

# nums1 = [1,2,2,1]
# nums2 = [2,2]

# print(s.intersection(nums1, nums2))

# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]

# print(s.intersection(nums1, nums2))



















