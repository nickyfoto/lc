#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#
# https://leetcode.com/problems/product-of-array-except-self/description/
#
# algorithms
# Medium (56.29%)
# Total Accepted:    299K
# Total Submissions: 530.4K
# Testcase Example:  '[1,2,3,4]'
#
# Given an array nums of n integers where n > 1,  return an array output such
# that output[i] is equal to the product of all the elements of nums except
# nums[i].
# 
# Example:
# 
# 
# Input:  [1,2,3,4]
# Output: [24,12,8,6]
# 
# 
# Note: Please solve it without division and in O(n).
# 
# Follow up:
# Could you solve it with constant space complexity? (The output array does not
# count as extra space for the purpose of space complexity analysis.)
# 
#
class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    def productExceptSelf(self, nums):
        
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        # print(output)
        p = 1
        for i in range(n-1,-1,-1):
            # print(i, output[i], p)
            output[i] = output[i] * p
            p = p * nums[i]
        # print(output)
        return output

# s = Solution()
# nums = [1,2,3,4]
# print(s.productExceptSelf(nums))
