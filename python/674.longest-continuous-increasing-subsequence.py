#
# @lc app=leetcode id=674 lang=python3
#
# [674] Longest Continuous Increasing Subsequence
#
# https://leetcode.com/problems/longest-continuous-increasing-subsequence/description/
#
# algorithms
# Easy (44.11%)
# Total Accepted:    63.9K
# Total Submissions: 144.8K
# Testcase Example:  '[1,3,5,4,7]'
#
# 
# Given an unsorted array of integers, find the length of longest continuous
# increasing subsequence (subarray).
# 
# 
# Example 1:
# 
# Input: [1,3,5,4,7]
# Output: 3
# Explanation: The longest continuous increasing subsequence is [1,3,5], its
# length is 3. 
# Even though [1,3,5,7] is also an increasing subsequence, it's not a
# continuous one where 5 and 7 are separated by 4. 
# 
# 
# 
# Example 2:
# 
# Input: [2,2,2,2,2]
# Output: 1
# Explanation: The longest continuous increasing subsequence is [2], its length
# is 1. 
# 
# 
# 
# Note:
# Length of the array will not exceed 10,000.
# 
#
class Solution:
    # def findLengthOfLCIS(self, nums: List[int]) -> int:
    def findLengthOfLCIS(self, nums):
        if not nums:
            return 0
        i = 1
        l = len(nums)
        res_list = []
        res = 1
        while i < l:
            if nums[i] > nums[i-1]:
                res += 1
            else:
                res_list.append(res)
                res = 1
            i += 1
        res_list.append(res)
        # print(max(res_list))
        return max(res_list)

# s = Solution()
# a1 = [1,3,5,4,7] # 3
# a2 = [1,3,5,7] # 4
# a3 = [1,3,5,4,2,3,4,5] # 4
# s.findLengthOfLCIS(a1)
# s.findLengthOfLCIS(a2)
# s.findLengthOfLCIS(a3)








        
