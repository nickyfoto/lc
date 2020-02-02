#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#
# https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (32.91%)
# Likes:    947
# Dislikes: 398
# Total Accepted:    208K
# Total Submissions: 632.2K
# Testcase Example:  '[2,5,6,0,0,1,2]\n0'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
# 
# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
# 
# You are given a target value to search. If found in the array return true,
# otherwise return false.
# 
# Example 1:
# 
# 
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
# 
# Follow up:
# 
# 
# This is a follow up problem to Search in Rotated Sorted Array, where nums may
# contain duplicates.
# Would this affect the run-time complexity? How and why?
# 
# 
#

# @lc code=start
from bisect import bisect_left
class Solution:
    # def search(self, nums: List[int], target: int) -> bool:

    def search(self, nums, target):
        
    
        def findMinIndex(nums):
            n = len(nums)
            if n == 1 or len(set(nums)) == 1:
                return 0
            if nums[0] < nums[-1]:
                return 0
            lo, hi = 0, n
            while lo < hi:
                # print('lo=', lo, 'hi=', hi)
                mid = (lo + hi) // 2
                m = nums[mid]
                if nums[mid - 1] > m:
                    # print('check mid=', mid)
                    return mid
                else:
                    # normally nums[0] must > nums[-1]
                    # if we allow duplicates, then nums[0] == nums[-1]
                    if nums[0] > nums[-1]:
                        if nums[-1] < m:
                            lo = mid + 1
                        else:
                            hi = mid
                    else: # nums[0] == nums[-1] 
                        # print('mid=', mid, nums[:mid])
                        left_min_index = findMinIndex(nums[:mid])
                        # print('left_min_index=', left_min_index, 'nums[left_min_index]=', nums[left_min_index],'nums[0]=', nums[0])
                        # if nums[left_min_index] < nums[0]:
                        if left_min_index > 0:
                            return left_min_index
                        else:
                            # print('here mid=', mid, nums[mid:])
                            return mid + findMinIndex(nums[mid:])    

        # print(findMinIndex(nums))

        def bs(nums, target):
            b = bisect_left(nums, target)
            # print(nums, b)
            if b == len(nums):
                return False
            if nums[b] == target:
                return True
            return False

        if not nums:
            return False
        if len(nums) == 1:
            return target == nums[0]
        
        min_index = findMinIndex(nums)
        # print('min_index=', min_index, 'nums[min_index - 1]=', nums[min_index - 1], nums.index(2) == min_index - 1, len(nums))

        if min_index == 0:
            return bs(nums, target)
        elif min_index == len(nums) - 1:
            if target == nums[min_index]:
                return True
            return bs(nums[:-1], target)
        else:
            return bs(nums[:min_index], target) or bs(nums[min_index:], target)

# @lc code=end
