#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (43.33%)
# Total Accepted:    521.1K
# Total Submissions: 1.2M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
# 
# Example:
# 
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
# 
#
class Solution:
    # def maxSubArray(self, nums: List[int]) -> int:
    def maxSubArray(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        L = [nums[0]]
        for i in range(1, n):
            if L[i-1] <= 0:
                L.append(nums[i])
            else:
                # print(nums[i])
                # print(L)
                L.append(L[i-1] + nums[i])
                # print(L)
        # print(L)
        return max(L)


# s = Solution()
# a = [-2,1,-3,4,-1,2,1,-5,4]
# print(s.maxSubArray(a))
