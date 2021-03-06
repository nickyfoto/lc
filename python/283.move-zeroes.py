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


# s = Solution()
# nums = [0,1,0,3,12]
# s.moveZeroes(nums)
