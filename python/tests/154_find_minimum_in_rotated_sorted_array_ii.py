#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/
#
# algorithms
# Hard (40.17%)
# Likes:    648
# Dislikes: 183
# Total Accepted:    156.9K
# Total Submissions: 390.6K
# Testcase Example:  '[1,3,5]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
# 
# Find the minimum element.
# 
# The array may contain duplicates.
# 
# Example 1:
# 
# 
# Input: [1,3,5]
# Output: 1
# 
# Example 2:
# 
# 
# Input: [2,2,2,0,1]
# Output: 0
# 
# Note:
# 
# 
# This is a follow up problem to Find Minimum in Rotated Sorted Array.
# Would allow duplicates affect the run-time complexity? How and why?
# 
# 
#

# @lc code=start
class Solution:
    # def findMin(self, nums: List[int]) -> int:
    def findMin(self, nums):
        n = len(nums)
        if n == 1 or len(set(nums)) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        lo, hi = 0, n
        while lo < hi:
            # print('lo=', lo, 'hi=', hi)
            mid = (lo + hi) // 2
            m = nums[mid]
            if nums[mid - 1] > m:
                return m
            else:
                # normally nums[0] must > nums[-1]
                # if we allow duplicates, then nums[0] == nums[-1]
                if nums[0] > nums[-1]:
                    if nums[-1] < m:
                        lo = mid + 1
                    else:
                        hi = mid
                else: # nums[0] == nums[-1] 
                    left_min = self.findMin(nums[:mid])
                    # print('left_min=', left_min)
                    if left_min < nums[0]:
                        return left_min
                    else:
                        return self.findMin(nums[mid:])                    
# @lc code=end
