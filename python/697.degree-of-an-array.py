#
# @lc app=leetcode id=697 lang=python3
#
# [697] Degree of an Array
#
# https://leetcode.com/problems/degree-of-an-array/description/
#
# algorithms
# Easy (50.52%)
# Total Accepted:    52.4K
# Total Submissions: 103.3K
# Testcase Example:  '[1,2,2,3,1]'
#
# Given a non-empty array of non-negative integers nums, the degree of this
# array is defined as the maximum frequency of any one of its elements.
# Your task is to find the smallest possible length of a (contiguous) subarray
# of nums, that has the same degree as nums.
# 
# Example 1:
# 
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# 
# 
# 
# 
# Example 2:
# 
# Input: [1,2,2,3,1,4,2]
# Output: 6
# 
# 
# 
# Note:
# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.
# 
#
class Solution:
    # def findShortestSubArray(self, nums: List[int]) -> int:
    def findShortestSubArray(self, nums):
        len_nums = len(nums)
        d = {}
        for n in nums:
            if n not in d:
                d[n] = 1
            else:
                d[n] += 1
        # print(d)
        degree = max([v for k, v in d.items()])
        # print(degree)
        elements = [k for k, v in d.items() if v == degree]
        # print(elements)
        shortest = float('inf')

        def distance(e):
            for i in range(len_nums):
                if nums[i] == e:
                    start = i
                    break
            for i in range(len_nums-1, -1, -1):
                if nums[i] == e:
                    end = i
                    break
            # print(e, end, start)
            return end-start

        for e in elements:
            de = distance(e)
            if de < shortest:
                shortest = de
        return shortest + 1

# s = Solution()
# nums = [1, 2, 2, 3, 1]
# nums = [1,2,2,3,1,4,2]
# print(s.findShortestSubArray(nums))































        
