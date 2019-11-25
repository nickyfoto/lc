#
# @lc app=leetcode id=665 lang=python3
#
# [665] Non-decreasing Array
#
# https://leetcode.com/problems/non-decreasing-array/description/
#
# algorithms
# Easy (19.49%)
# Total Accepted:    56.6K
# Total Submissions: 290.8K
# Testcase Example:  '[4,2,3]'
#
# 
# Given an array with n integers, your task is to check if it could become
# non-decreasing by modifying at most 1 element.
# 
# 
# 
# We define an array is non-decreasing if array[i]  holds for every i (1 
# 
# Example 1:
# 
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing
# array.
# 
# 
# 
# Example 2:
# 
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one
# element.
# 
# 
# 
# Note:
# The n belongs to [1, 10,000].
# 
#
class Solution:
    # def checkPossibility(self, nums: List[int]) -> bool:
    def checkPossibility(self, nums):
        def check(nums):
            n = len(nums)
            # print(nums, nums[0], nums[1])
            for i in range(n-1):
                if nums[i] > nums[i+1]:
                    return i, False
            return min(nums), True
        nd, res = check(nums)
        # print(nd, res)
        if res:
            return True
        if nd == len(nums) - 2:
            return True
        
        else:
            if nd >= 1:
                temp = nums.copy()
                temp[nd] = temp[nd-1]
                if check(temp)[1]:
                    return True
                else:
                    nums[nd+1] = nums[nd+2]
                    # print('here', nums)
                    if check(nums)[1]:
                        return True
                    else:
                        return False
            else:
                # print(nums)
                return check(nums[nd+1:])[1]
           

# s = Solution()
# nums = [4,2,3]
# print(s.checkPossibility(nums) == True)
# nums = [4,2,1]
# print(s.checkPossibility(nums) == False)


# nums = [3,4,2,3]
# print(s.checkPossibility(nums) == False)

# nums = [2,3,3,2,4]
# print(s.checkPossibility(nums) == True)

# nums = [3,3,2,2]
# print(s.checkPossibility(nums) == False)

# nums = [1,2,4,5,3]
# print(s.checkPossibility(nums) == True)

# nums = [1,3,4,2,5]
# print(s.checkPossibility(nums) == True)

# nums = [1,3,5,2,4]
# print(s.checkPossibility(nums) == False)

# nums = [-1,4,2,3]
# print(s.checkPossibility(nums) == True)