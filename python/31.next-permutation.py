#
# @lc app=leetcode id=31 lang=python3
#
# [31] Next Permutation
#
# https://leetcode.com/problems/next-permutation/description/
#
# algorithms
# Medium (31.68%)
# Likes:    2618
# Dislikes: 887
# Total Accepted:    310.9K
# Total Submissions: 981.4K
# Testcase Example:  '[1,2,3]'
#
# Implement next permutation, which rearranges numbers into the
# lexicographically next greater permutation of numbers.
# 
# If such arrangement is not possible, it must rearrange it as the lowest
# possible order (ie, sorted in ascending order).
# 
# The replacement must be in-place and use only constant extra memory.
# 
# Here are some examples. Inputs are in the left-hand column and its
# corresponding outputs are in the right-hand column.
# 
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1
# 
#

# @lc code=start
class Solution:
    # def nextPermutation(self, nums: List[int]) -> None:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n >= 2:
            mx_idx = n - 1
            mx_val = nums[mx_idx]
            while nums[mx_idx - 1] >= mx_val:
                mx_val = nums[mx_idx - 1]
                mx_idx -= 1
            stop = mx_idx
            mx_idx = n - 1
            while mx_val < nums[mx_idx]:
                mx_idx -= 1
            nums[mx_idx], nums[stop] = nums[stop], nums[mx_idx]
            nums[stop:] = sorted(nums[stop:])
        print(nums)
        
# @lc code=end
