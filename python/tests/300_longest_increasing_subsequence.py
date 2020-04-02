#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#
# https://leetcode.com/problems/longest-increasing-subsequence/description/
#
# algorithms
# Medium (41.91%)
# Likes:    3770
# Dislikes: 85
# Total Accepted:    320K
# Total Submissions: 763K
# Testcase Example:  '[10,9,2,5,3,7,101,18]'
#
# Given an unsorted array of integers, find the length of longest increasing
# subsequence.
# 
# Example:
# 
# 
# Input: [10,9,2,5,3,7,101,18]
# Output: 4 
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the
# length is 4. 
# 
# Note: 
# 
# 
# There may be more than one LIS combination, it is only necessary for you to
# return the length.
# Your algorithm should run in O(n^2) complexity.
# 
# 
# Follow up: Could you improve it to O(n log n) time complexity?
# 
#

# @lc code=start
from bisect import bisect_left
class Solution:
    # def lengthOfLIS(self, nums: List[int]) -> int:
    def lengthOfLIS_bs(self, nums):
        """
        dp with binary search
        """
        if not nums: return 0
        n = len(nums)
        dp = [0] * n
        res = 0
        for num in nums:
            i = bisect_left(dp[:res], num)
            dp[i] = num
            if i == res:
                res += 1
        return res

    def lengthOfLIS(self, nums):
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            dp[i] = max(dp[i], max([dp[j] for j in range(i) if nums[j] < nums[i]] or [0]) + 1)
        # print(dp)
        return max(dp) if dp else 0
# @lc code=end
