#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
# https://leetcode.com/problems/house-robber-ii/description/
#
# algorithms
# Medium (35.93%)
# Likes:    1349
# Dislikes: 43
# Total Accepted:    151.1K
# Total Submissions: 420.3K
# Testcase Example:  '[2,3,2]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed. All houses at this place are
# arranged in a circle. That means the first house is the neighbor of the last
# one. Meanwhile, adjacent houses have security system connected and it will
# automatically contact the police if two adjacent houses were broken into on
# the same night.
# 
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
# 
# Example 1:
# 
# 
# Input: [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money =
# 2),
# because they are adjacent houses.
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
# 
#

# @lc code=start
class Solution:
    # def rob(self, nums: List[int]) -> int:
    def rob(self, nums):
        """
        recur nums[1:]
        recur nums[:-1]
        return max of these two
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        def recur(nums):
            res = prev = 0
            for n in nums:
                res, prev = max(res, prev + n), res
                print(res, prev)
            return res
        return max(recur(nums[1:]), recur(nums[:-1]))
# @lc code=end
