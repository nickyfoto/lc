#
# @lc app=leetcode id=645 lang=python3
#
# [645] Set Mismatch
#
# https://leetcode.com/problems/set-mismatch/description/
#
# algorithms
# Easy (40.53%)
# Total Accepted:    46.9K
# Total Submissions: 115.5K
# Testcase Example:  '[1,2,2,4]'
#
# 
# The set S originally contains numbers from 1 to n. But unfortunately, due to
# the data error, one of the numbers in the set got duplicated to another
# number in the set, which results in repetition of one number and loss of
# another number. 
# 
# 
# 
# Given an array nums representing the data status of this set after the error.
# Your task is to firstly find the number occurs twice and then find the number
# that is missing. Return them in the form of an array.
# 
# 
# 
# Example 1:
# 
# Input: nums = [1,2,2,4]
# Output: [2,3]
# 
# 
# 
# Note:
# 
# The given array size will in the range [2, 10000].
# The given array's numbers won't have any order.
# 
# 
#
class Solution:
    # def findErrorNums(self, nums: List[int]) -> List[int]:
    def findErrorNums(self, nums):
        n = len(nums)
        nums.sort()
        # print(nums)
        rep, missing = 0, 0
        for i in range(n):
            if i < n-1:
                if nums[i] == nums[i+1]:
                    rep = nums[i]
            if not rep:
                if nums[i] != i+1:
                    if not missing:
                        # print('i=', i, 'missing=',missing)
                        missing = i+1
            else:
                if nums[i] != i+1:
                    # print('i=', i, 'rep=', rep,  'missing=',missing)
                    # if nums[i] != rep:
                    if not missing:
                        if i+1<n and nums[i+1] != i+1:
                            missing = i+1
                        # print('i=', i, 'rep=', rep,  'missing=',missing)
        # print([rep, missing])
        if not missing:
            missing = n
        return [rep, missing]


        
# s = Solution()
# nums = [1,2,2,4]
# print(s.findErrorNums(nums) == [2, 3])

# nums = [1,1]
# print(s.findErrorNums(nums) == [1, 2])

# nums = [2,2]
# print(s.findErrorNums(nums) == [2, 1])

# nums = [1, 3, 3, 4]
# print(s.findErrorNums(nums) == [3, 2])
        
# nums = [3,2,3,4,6,5]
# print(s.findErrorNums(nums) == [3, 1])

# nums = [1,5,3,2,2,7,6,4,8,9]
# print(s.findErrorNums(nums) == [2, 10])




