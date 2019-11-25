#
# @lc app=leetcode id=152 lang=python3
#
# [152] Maximum Product Subarray
#
# https://leetcode.com/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (28.96%)
# Total Accepted:    203.3K
# Total Submissions: 701.4K
# Testcase Example:  '[2,3,-2,4]'
#
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.
# 
# Example 1:
# 
# 
# Input: [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# 
# 
# Example 2:
# 
# 
# Input: [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
# 
#
class Solution:
    # def maxProduct(self, nums: List[int]) -> int:
    def maxProduct(self, nums):
        n = len(nums)
        Lmax = [1] * n
        Lmin = [1] * n
        Lmax[0] = nums[0]
        Lmin[0] = nums[0]
        for i in range(1, n):
            if nums[i] >= 0:
                # update Lmax
                if Lmax[i-1] > 0:
                    Lmax[i] = nums[i] * Lmax[i-1]
                else:
                    Lmax[i] = nums[i]
                # update Lmin
                if Lmin[i-1] > 0:
                    Lmin[i] = nums[i]
                else:
                    # print('here', "i=", i)
                    Lmin[i] = nums[i] * Lmin[i-1]
            else:
                # update Lmax
                if Lmin[i-1] < 0:
                    Lmax[i] = nums[i] * Lmin[i-1]
                else:
                    Lmax[i] = nums[i]
                # update Lmin
                if Lmax[i-1] > 0:
                    Lmin[i] = nums[i] * Lmax[i-1]
                else:
                    Lmin[i] = nums[i]
        # print(Lmax)
        # print(Lmin)
        return max(Lmax)


# s = Solution()


# a1 = [2,3,-2,4] # 6
# print(s.maxProduct(a1))
# a2 = [-2, 0, -1] # 0
# print(s.maxProduct(a2))
# a3 = [-4,-3] # 12
# print(s.maxProduct(a3))

# a4 = [-2,3,-4] # 24
# print(s.maxProduct(a4))

# a5 = [-4,-3,-2] # 12
# print(s.maxProduct(a5)) # 

# a6 = [1,2,-1,-2,2,1,-2,1,4,-5,4] # 1280
# print(s.maxProduct(a6)) # 



