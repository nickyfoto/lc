#
# @lc app=leetcode id=410 lang=python3
#
# [410] Split Array Largest Sum
#
# https://leetcode.com/problems/split-array-largest-sum/description/
#
# algorithms
# Hard (43.62%)
# Likes:    1452
# Dislikes: 76
# Total Accepted:    78.3K
# Total Submissions: 179.1K
# Testcase Example:  '[7,2,5,10,8]\n2'
#
# Given an array which consists of non-negative integers and an integer m, you
# can split the array into m non-empty continuous subarrays. Write an algorithm
# to minimize the largest sum among these m subarrays.
# 
# 
# Note:
# If n is the length of array, assume the following constraints are satisfied:
# 
# 1 ≤ n ≤ 1000
# 1 ≤ m ≤ min(50, n)
# 
# 
# 
# Examples: 
# 
# Input:
# nums = [7,2,5,10,8]
# m = 2
# 
# Output:
# 18
# 
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
# 
# 
#

# @lc code=start
from itertools import accumulate
import math
from pprint import pprint
class Solution:
    # def splitArray(self, nums: List[int], m: int) -> int:
    def splitArray(self, nums, m):
        """
        set l be the max value of nums
        set r be the sum of nums
        for every iteration
            set mid = l + (r - l) // 2

            iterate every num in nums:
                if acc + num > mid:
                    set acc = that num
                    increment cnt
                else:
                    add num to acc
                if cnt <= m:
                    update res with mid
                    set r = mid - 1
                else:
                    set l = mid + 1
        """
        r = sum(nums)
        l = max(nums)
        n = len(nums)
        res = r

        def can_fit(mid):
            """
            mid as threshhold to see whether we can 
            split array into m partition
            
            sm: sum of values for each partition
            slots: number of slots we needed
            """
            slot_sum = 0
            slots = 1
            for i in range(n):
                if slot_sum + nums[i] <= mid:
                    slot_sum += nums[i]
                else:
                    slots += 1
                    slot_sum = nums[i]
            return slots <= m
            

        while l <= r:
            mid = l + (r - l) // 2
            fit = can_fit(mid)
            if fit:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res


    # def splitArray(self, nums, m):
    #     n = len(nums)
    #     dp = [[math.inf] * (m + 1) for _ in range(n + 1)]
    #     acc = [0] + list(accumulate(nums))
    #     dp[0][0] = 0
    #     for i in range(1, n + 1):
    #         for j in range(1, m + 1):
    #             for k in range(i):
    #                 dp[i][j] = min(dp[i][j], max(dp[k][j - 1], acc[i] - acc[k]))
    #     # pprint(dp)
    #     return dp[n][m]

# @lc code=end
