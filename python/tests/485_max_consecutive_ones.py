#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#
# https://leetcode.com/problems/max-consecutive-ones/description/
#
# algorithms
# Easy (55.09%)
# Total Accepted:    142.5K
# Total Submissions: 258.3K
# Testcase Example:  '[1,0,1,1,0,1]'
#
# Given a binary array, find the maximum number of consecutive 1s in this
# array.
# 
# Example 1:
# 
# Input: [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive
# 1s.
# ⁠   The maximum number of consecutive 1s is 3.
# 
# 
# 
# Note:
# 
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000
# 
# 
#
class Solution:
    # def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    def findMaxConsecutiveOnes(self, nums):
        m = 0
        i = 0
        n = len(nums)
        count1 = 0
        # count_not_1 = 0
        while i < n:
            while i < n and nums[i] != 1:
                # count_not_1 += 1
                i += 1
            # print('count_not_1=', count_not_1)
            # print('i=', i)
            while i < n and nums[i] == 1:
                count1 += 1
                i += 1
            if count1 > m:
                m = count1
            count1 = 0
            # print('count1=', count1)

            i += 1
        return m

    def findMaxConsecutiveOnes(self, nums):
        mx = cnt = 0
        for num in nums:
            if num == 1:
                cnt += 1
                mx = max(mx, cnt)
            else:
                cnt = 0
        return mx
