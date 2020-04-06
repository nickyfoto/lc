#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
# https://leetcode.com/problems/target-sum/description/
#
# algorithms
# Medium (46.35%)
# Likes:    2077
# Dislikes: 95
# Total Accepted:    141.2K
# Total Submissions: 303.8K
# Testcase Example:  '[1,1,1,1,1]\n3'
#
# 
# You are given a list of non-negative integers, a1, a2, ..., an, and a target,
# S. Now you have 2 symbols + and -. For each integer, you should choose one
# from + and - as its new symbol.
# ⁠
# 
# Find out how many ways to assign symbols to make sum of integers equal to
# target S.  
# 
# 
# Example 1:
# 
# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 
# 
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 
# There are 5 ways to assign symbols to make the sum of nums be target 3.
# 
# 
# 
# Note:
# 
# The length of the given array is positive and will not exceed 20. 
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.
# 
# 
#

# @lc code=start
from functools import lru_cache
class Solution:
    # def findTargetSumWays(self, nums: List[int], S: int) -> int:
    def findTargetSumWays(self, nums, S):
        n = len(nums)
        @lru_cache(None)
        def dfs(i, sm):
            if i == n:
                if sm == S:
                    return 1
                return 0
            else:
                a = dfs(i + 1, sm + nums[i])
                b = dfs(i + 1, sm - nums[i])
                return a + b
        return dfs(0, 0)
# @lc code=end
