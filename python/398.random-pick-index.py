#
# @lc app=leetcode id=398 lang=python3
#
# [398] Random Pick Index
#
# https://leetcode.com/problems/random-pick-index/description/
#
# algorithms
# Medium (50.80%)
# Total Accepted:    59.6K
# Total Submissions: 117.1K
# Testcase Example:  '["Solution","pick"]\n[[[1,2,3,3,3]],[3]]'
#
# Given an array of integers with possible duplicates, randomly output the
# index of a given target number. You can assume that the given target number
# must exist in the array.
# 
# Note:
# The array size can be very large. Solution that uses too much extra space
# will not pass the judge.
# 
# Example:
# 
# 
# int[] nums = new int[] {1,2,3,3,3};
# Solution solution = new Solution(nums);
# 
# // pick(3) should return either index 2, 3, or 4 randomly. Each index should
# have equal probability of returning.
# solution.pick(3);
# 
# // pick(1) should return 0. Since in the array only nums[0] is equal to 1.
# solution.pick(1);
# 
# 
#
from random import choice
class Solution:

    # def __init__(self, nums: List[int]):
    def __init__(self, nums):
        self.n = len(nums)
        # nums.sort()
        self.nums = nums

    def pick(self, target: int) -> int:
        i = 0
        indices = []
        while i < self.n:
            if self.nums[i] == target:
                indices.append(i)
            i += 1
        
        return choice(indices)
        # print(i, j)


# Your Solution object will be instantiated and called as such:
# nums = [1,2,3,3,3]
# obj = Solution(nums)
# target = 1
# target = 3
# param_1 = obj.pick(target)
# print(param_1)


  # ✘ answer: [null,6415]
  # ✘ expected_answer: [null,4857]
  # ✘ stdout: 



