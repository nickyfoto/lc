#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (44.77%)
# Likes:    12553
# Dislikes: 439
# Total Accepted:    2.3M
# Total Submissions: 5.2M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# Example:
# 
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
# 
#

# @lc code=start
class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    def twoSum(self, nums, target):
        """
        use a dictionary to save the value we've seen and its index
        if we see a new number that can match with a previous seen number
        we return the index of these two
        """
        d = {nums[0]: 0}
        for i in range(len(nums)):
            other = target - nums[i+1]
            if other in d:
                return [d[other], i+1]
            else:
                d[nums[i+1]]= i+1
# @lc code=end
