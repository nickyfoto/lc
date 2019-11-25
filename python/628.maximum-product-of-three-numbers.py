#
# @lc app=leetcode id=628 lang=python3
#
# [628] Maximum Product of Three Numbers
#
# https://leetcode.com/problems/maximum-product-of-three-numbers/description/
#
# algorithms
# Easy (45.81%)
# Total Accepted:    69.2K
# Total Submissions: 150.4K
# Testcase Example:  '[1,2,3]'
#
# Given an integer array, find three numbers whose product is maximum and
# output the maximum product.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# Output: 6
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,4]
# Output: 24
# 
# 
# 
# 
# Note:
# 
# 
# The length of the given array will be in range [3,104] and all elements are
# in the range [-1000, 1000].
# Multiplication of any three numbers in the input won't exceed the range of
# 32-bit signed integer.
# 
# 
# 
# 
#
class Solution:
    # def maximumProduct(self, nums: List[int]) -> int:
    # def maximumProduct(self, nums, debug=False):
    #     n = len(nums)
    #     start = nums[0]
    #     two_positive = [start] * n
    #     two_negative = [start] * n
    #     max_pos = start
    #     min_neg = start
    #     for i in range(1, n):
    #         if nums[i] > 0:
    #             pos = max_pos * nums[i]
    #             two_positive[i] = pos
    #             neg = min_neg * nums[i]
    #             # print(two_negative, i)
    #             two_negative[i] = neg
    #         elif nums[i] < 0:        
    #             neg = max_pos * nums[i]
    #             two_negative[i] = neg
    #             pos = min_neg * nums[i]
    #             two_positive[i] = pos
    #         else:
    #             two_positive[i] = 0
    #             two_negative[i] = 0
    #             if max_pos < 0:
    #                 max_pos = 0
    #             if min_neg > 0:
    #                 min_neg = 0
    #         if nums[i] > max_pos:
    #             max_pos = nums[i]
    #         if nums[i] < min_neg:
    #             min_neg = nums[i]
    #     if debug:
    #         print(max_pos, min_neg)
    #         print(two_positive)
    #         print(two_negative)

    #     # construct 3 max prod
    #     start = nums[0] * nums[1]
    #     max_3_prod = [nums[2]] * (n-2)
    #     for i in range(n-2):
    #         if nums[i+2] > 0:
    #             # print('here', two_positive[1:i+2])
    #             max_3_prod[i] = nums[i+2] * max(two_positive[1:i+2])
    #         elif nums[i+2] < 0:
    #             max_3_prod[i] = nums[i+2] * min(two_negative[1:i+2])
    #         else:
    #             max_3_prod[i] = 0
    #     # print('final', max_3_prod)
    #     return max(max_3_prod)



    def maximumProduct(self, nums, debug=False):
        nums.sort()
        # min(nums) >= 0 or max(nums) < 0
        if nums[0] >= 0 or nums[-1] < 0:
            return nums[-1] * nums[-2] * nums[-3]
        else:
            if nums[-1] * nums[-2] * nums[-3] > nums[-1] * nums[0] * nums[1]:
                return nums[-1] * nums[-2] * nums[-3]
            else:
                return nums[-1] * nums[0] * nums[1]

# s = Solution()
# nums = [1,2,3]
# print(s.maximumProduct(nums) == 6)

# nums = [1,2,3,4]
# print(s.maximumProduct(nums) == 24)
# # 2/83
# nums = [-1,-2,-3]
# print(s.maximumProduct(nums) == -6)


# # 3/83
# nums = [1,0,100]
# print(s.maximumProduct(nums) == 0)


# # 59/83
# nums = [-1000,-1000,1000]
# print(s.maximumProduct(nums) == 1000000000)













        
