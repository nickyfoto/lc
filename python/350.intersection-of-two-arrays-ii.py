#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#
# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
#
# algorithms
# Easy (47.44%)
# Total Accepted:    199K
# Total Submissions: 417.4K
# Testcase Example:  '[1,2,2,1]\n[2,2]'
#
# Given two arrays, write a function to compute their intersection.
# 
# Example 1:
# 
# 
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# 
# 
# Note:
# 
# 
# Each element in the result should appear as many times as it shows in both
# arrays.
# The result can be in any order.
# 
# 
# Follow up:
# 
# 
# What if the given array is already sorted? How would you optimize your
# algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is
# better?
# What if elements of nums2 are stored on disk, and the memory is limited such
# that you cannot load all elements into the memory at once?
# 
# 
#
class Solution:
    # def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    def intersect(self, nums1, nums2):
        def getDict(nums):
            d = {}
            for i in nums:
                if i not in d:
                    d[i] = 1
                else:
                    d[i] += 1
            return d
        d1 = getDict(nums1)
        d2 = getDict(nums2)
        if len(d1) > len(d2):
            res = []
            for k in d2:
                if k in d1:
                    res.extend([k] * min([d2[k], d1[k]]))
            return res
        else:
            res = []
            for k in d1:
                if k in d2:
                    res.extend([k] * min([d2[k], d1[k]]))
            return res


# s = Solution()
# nums1 = [1,2,2,1]
# nums2 = [2,2]
# print(s.intersect(nums1, nums2))
# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
# print(s.intersect(nums1, nums2))



























