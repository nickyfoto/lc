#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#
# https://leetcode.com/problems/maximum-average-subarray-i/description/
#
# algorithms
# Easy (39.62%)
# Total Accepted:    54.2K
# Total Submissions: 136.2K
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
# Given an array consisting of n integers, find the contiguous subarray of
# given length k that has the maximum average value. And you need to output the
# maximum average value.
# 
# Example 1:
# 
# 
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= k <= n <= 30,000.
# Elements of the given array will be in the range [-10,000, 10,000].
# 
# 
# 
# 
#
class Solution:
    # def findMaxAverage(self, nums: List[int], k: int) -> float:
    def findMaxAverage(self, nums, k):
        n = len(nums)
        l = nums[:k]
        m = sum(l)
        s = m
        # print(l, m)
        for i in range(k, n):
            # s += nums[i] - l[0]
            s += nums[i] - nums[i-k]
            # print(l[0], nums[i-k])
            # l = nums[i+1-k:i+1]
            # print(l)
            if s > m:
                # print('here', i)
                m = s
        return m / k



# s = Solution()
# nums = [1,12,-5,-6,50,3]
# k = 4
# print(s.findMaxAverage(nums, k))
# nums = [4,2,1,3,3]
# k = 2
# print(s.findMaxAverage(nums, k))


