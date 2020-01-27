#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# https://leetcode.com/problems/3sum/description/
#
# algorithms
# Medium (25.58%)
# Likes:    5399
# Dislikes: 658
# Total Accepted:    756.2K
# Total Submissions: 3M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
# 
# Note:
# 
# The solution set must not contain duplicate triplets.
# 
# Example:
# 
# 
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
# ⁠ [-1, 0, 1],
# ⁠ [-1, -1, 2]
# ]
# 
#

# @lc code=start
class Solution:
    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    def threeSum(self, nums):
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n - 2):
            if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                left = i + 1
                right = n - 1
                sm = 0 - nums[i]
                while left < right:
                    if nums[left] + nums[right] == sm:
                        res.append([nums[i], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right - 1] == nums[right]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif nums[left] + nums[right] < sm:
                            left += 1
                    else:
                        right -= 1
        return res 
# @lc code=end
