#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#
# https://leetcode.com/problems/next-greater-element-i/description/
#
# algorithms
# Easy (59.67%)
# Total Accepted:    98.7K
# Total Submissions: 165.2K
# Testcase Example:  '[4,1,2]\n[1,3,4,2]'
#
# 
# You are given two arrays (without duplicates) nums1 and nums2 where nums1’s
# elements are subset of nums2. Find all the next greater numbers for nums1's
# elements in the corresponding places of nums2. 
# 
# 
# 
# The Next Greater Number of a number x in nums1 is the first greater number to
# its right in nums2. If it does not exist, output -1 for this number.
# 
# 
# Example 1:
# 
# Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
# Output: [-1,3,-1]
# Explanation:
# ⁠   For number 4 in the first array, you cannot find the next greater number
# for it in the second array, so output -1.
# ⁠   For number 1 in the first array, the next greater number for it in the
# second array is 3.
# ⁠   For number 2 in the first array, there is no next greater number for it
# in the second array, so output -1.
# 
# 
# 
# Example 2:
# 
# Input: nums1 = [2,4], nums2 = [1,2,3,4].
# Output: [3,-1]
# Explanation:
# ⁠   For number 2 in the first array, the next greater number for it in the
# second array is 3.
# ⁠   For number 4 in the first array, there is no next greater number for it
# in the second array, so output -1.
# 
# 
# 
# 
# Note:
# 
# All elements in nums1 and nums2 are unique.
# The length of both nums1 and nums2 would not exceed 1000.
# 
# 
#
class Solution:
    # def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    def nextGreaterElement(self, nums1, nums2):
        res = []
        for n1 in nums1:
            idx = nums2.index(n1)
            if idx == len(nums2) -1:
                res.append(-1)
            else:
                for i in range(idx+1, len(nums2)):
                    if nums2[i] > n1:
                        res.append(nums2[i])
                        break
                if i == len(nums2) - 1 and not nums2[i] > n1:
                    res.append(-1)
        return res

   
# s = Solution()
# nums1 = [4,1,2]
# nums2 = [1,3,4,2]


# print(s.nextGreaterElement(nums1, nums2))

# nums1 = [2,4]
# nums2 = [1,2,3,4]
# print(s.nextGreaterElement(nums1, nums2))