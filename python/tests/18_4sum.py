#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#
# https://leetcode.com/problems/4sum/description/
#
# algorithms
# Medium (32.32%)
# Likes:    1475
# Dislikes: 279
# Total Accepted:    290.5K
# Total Submissions: 898.7K
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# Given an array nums of n integers and an integer target, are there elements
# a, b, c, and d in nums such that a + b + c + d = target? Find all unique
# quadruplets in the array which gives the sum of target.
# 
# Note:
# 
# The solution set must not contain duplicate quadruplets.
# 
# Example:
# 
# 
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
# 
# A solution set is:
# [
# ⁠ [-1,  0, 0, 1],
# ⁠ [-2, -1, 1, 2],
# ⁠ [-2,  0, 0, 2]
# ]
# 
# 
#

# @lc code=start
class Solution:
    # def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    def fourSum(self, nums, target):
        def findNSum(l, r, target, N, result, results):
            if r - l + 1 < N or N < 2 or target < nums[l] * N or target > nums[r] * N:
                return
            if N == 2:
                while l < r:
                    s = nums[l] + nums[r]
                    if s == target:
                        results.append(result + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l - 1] == nums[l]:
                            l += 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
            else:
                for i in range(l, r + 1):
                    if i == l or (i > l and nums[i - 1] != nums[i]):
                        findNSum(i + 1, r, target - nums[i], N - 1, result + [nums[i]], results)
        nums.sort()
        results = []
        findNSum(0, len(nums) - 1, target, 4, [], results)
        return results
# @lc code=end
