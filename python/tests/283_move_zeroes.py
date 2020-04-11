#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# https://leetcode.com/problems/move-zeroes/description/
#
# algorithms
# Easy (54.45%)
# Total Accepted:    474.1K
# Total Submissions: 870.7K
# Testcase Example:  '[0,1,0,3,12]'
#
# <p>Given an array <code>nums</code>, write a function to move all
# <code>0</code>&#39;s to the end of it while maintaining the relative order of
# the non-zero elements.</p>
# 
# <p><b>Example:</b></p>
# 
# <pre>
# <b>Input:</b> <code>[0,1,0,3,12]</code>
# <b>Output:</b> <code>[1,3,12,0,0]</code></pre>
# 
# <p><b>Note</b>:</p>
# 
# <ol>
# <li>You must do this <b>in-place</b> without making a copy of the
# array.</li>
# <li>Minimize the total number of operations.</li>
# </ol>
#
class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                for j in range(i+1, n):
                    if nums[j] != 0:
                        nums[i], nums[j] = nums[j], 0
                        break
        # print(nums)

    def moveZeroes(self, nums):
        """
        https://leetcode.com/problems/move-zeroes/discuss/562911/Two-pointers-technique-(Python-O(n)-time-O(1)-space)
        """
        zero = none_zero = 0
        while none_zero < len(nums):
            if nums[zero] == 0 and nums[none_zero] != 0:
                nums[zero], nums[none_zero] = nums[none_zero], nums[zero]
            # wait while we find a non-zero element to
            # switch with you
            if nums[zero] != 0:
                zero += 1
            # keep going
            none_zero += 1


    def moveZeros(self, nums):
        none_zero = curr = 0
        while curr < len(nums):
            if nums[curr] != 0:
                nums[none_zero], nums[curr] = nums[curr], nums[none_zero]
                none_zero += 1
        
