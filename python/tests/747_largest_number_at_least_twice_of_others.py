#
# @lc app=leetcode id=747 lang=python3
#
# [747] Largest Number At Least Twice of Others
#
# https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/
#
# algorithms
# Easy (40.63%)
# Total Accepted:    54.6K
# Total Submissions: 134.2K
# Testcase Example:  '[0,0,0,1]'
#
# In a given integer array nums, there is always exactly one largest element.
# 
# Find whether the largest element in the array is at least twice as much as
# every other number in the array.
# 
# If it is, return the index of the largest element, otherwise return -1.
# 
# Example 1:
# 
# 
# Input: nums = [3, 6, 1, 0]
# Output: 1
# Explanation: 6 is the largest integer, and for every other number in the
# array x,
# 6 is more than twice as big as x.  The index of value 6 is 1, so we return
# 1.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1, 2, 3, 4]
# Output: -1
# Explanation: 4 isn't at least as big as twice the value of 3, so we return
# -1.
# 
# 
# 
# 
# Note:
# 
# 
# nums will have a length in the range [1, 50].
# Every nums[i] will be an integer in the range [0, 99].
# 
# 
# 
# 
#
class Solution:
    # def dominantIndex(self, nums: List[int]) -> int:
    def dominantIndex(self, nums):
        m = max(nums)
        m_idx = nums.index(m)
        if m > 0:
            if not [x for x in nums if x != m and 2*x > m]:
                return m_idx
            else:
                return -1
        elif m == 0:
            return m_idx
        else:
            if len([x for x in nums if x != m and m*2-x >= 0]) == len(nums) - 1:
                return m_idx
            else:
                return -1
        
    def dominantIndex(self, nums):
        mx = max(nums)
        if all(mx >= 2 * num for num in nums if num != mx):
            return nums.index(mx)
        return -1