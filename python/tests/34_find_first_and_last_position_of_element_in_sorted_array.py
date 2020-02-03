#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (34.95%)
# Likes:    2483
# Dislikes: 114
# Total Accepted:    410.1K
# Total Submissions: 1.2M
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# Given an array of integers nums sorted in ascending order, find the starting
# and ending position of a given target value.
# 
# Your algorithm's runtime complexity must be in the order of O(log n).
# 
# If the target is not found in the array, return [-1, -1].
# 
# Example 1:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# 
# Example 2:
# 
# 
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# 
#

# @lc code=start
class Solution:
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    def searchRange_me(self, nums, target):

        def find(mid, target):
            lo, hi = mid, mid
            while lo > 0 and nums[lo - 1] == target:
                lo -= 1
            while hi < len(nums) - 1 and nums[hi + 1] == target:
                hi += 1
            return [lo, hi]


        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if target == nums[mid]:
                return find(mid, target)
            elif target < nums[mid]:
                hi = mid
            else:
                lo = mid + 1
        return [-1, -1]

    def searchRange(self, nums, target):
        
        def firstGreaterEqual(nums, target):
            """
            if target in nums return the index of first target
            if target not in nums, return the first index that are larget 
            than target
            if target larger than nums[-1], return len(nums)
            """
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                m = nums[mid]
                if m < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo
        
        
        start = firstGreaterEqual(nums, target)
        print(start, firstGreaterEqual(nums, 11))
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        return [start, firstGreaterEqual(nums, target + 1) - 1]

# @lc code=end
