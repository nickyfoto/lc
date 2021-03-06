#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#
# https://leetcode.com/problems/first-missing-positive/description/
#
# algorithms
# Hard (30.62%)
# Likes:    2535
# Dislikes: 698
# Total Accepted:    279K
# Total Submissions: 910.4K
# Testcase Example:  '[1,2,0]'
#
# Given an unsorted integer array, find the smallest missing positive integer.
# 
# Example 1:
# 
# 
# Input: [1,2,0]
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: [3,4,-1,1]
# Output: 2
# 
# 
# Example 3:
# 
# 
# Input: [7,8,9,11,12]
# Output: 1
# 
# 
# Note:
# 
# Your algorithm should run in O(n) time and uses constant extra space.
# 
#

# @lc code=start
class Solution:
    # def firstMissingPositive(self, nums: List[int]) -> int:
    def firstMissingPositive_me(self, nums):
        n = len(nums)
        d = {i: False for i in range(1, n+2)}
        for i in nums:
            if i in d:
                d[i] = True
        for i in d:
            if not d[i]:
                return i

    def firstMissingPositive(self, nums):
        """
        each value - 1 as index
        if it is a valid index and nums[idx] != nums[i]
        swap nums[i] nums[idx]
        """
        n = len(nums)
        for i in range(n):
            elem, idx = nums[i], nums[i] - 1
            while idx >= 0 and idx < n and nums[idx] != elem:
                nextElem = nums[idx]
                nums[idx] = elem
                elem, idx = nextElem, nextElem - 1
                # print('here')

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
# @lc code=end
