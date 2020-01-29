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
    def nextPermutation_v1(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n > 1:
            mx_idx = n - 1
            mx_val = nums[mx_idx]
            stop = mx_idx - 1
            while stop > 0 and nums[stop] >= mx_val:
                mx_val = nums[stop]
                stop -= 1
            
            if stop == 0 and nums[0] >= mx_val:
                nums.sort()
                return
            
            mx_val = nums[stop]
            
            mx_idx = n - 1
            while nums[mx_idx] <= mx_val:
                mx_idx -= 1
            nums[mx_idx], nums[stop] = nums[stop], nums[mx_idx]
            nums[stop+1:] = sorted(nums[stop+1:])

    def nextPermutation(self, nums):

        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        # reverse(nums, i + 1)
        nums[i+1:] = sorted(nums[i+1:])
        # return nums
# @lc code=end
