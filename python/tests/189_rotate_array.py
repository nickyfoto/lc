#
# @lc app=leetcode id=189 lang=python3
#
# [189] Rotate Array
#
# https://leetcode.com/problems/rotate-array/description/
#
# algorithms
# Easy (30.32%)
# Total Accepted:    316.3K
# Total Submissions: 1M
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# Given an array, rotate the array to the right by k steps, where k is
# non-negative.
# 
# Example 1:
# 
# 
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# 
# 
# Example 2:
# 
# 
# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
# 
# 
# Note:
# 
# 
# Try to come up as many solutions as you can, there are at least 3 different
# ways to solve this problem.
# Could you do it in-place with O(1) extra space?
# 
#
class Solution:
    # def rotate(self, nums: List[int], k: int) -> None:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        124 ms, 15.3 MB
        """
        count = 0
        n = len(nums)
        while count < k % n:
            nums.insert(0, nums.pop())
            count += 1

    def rotate(self, nums, k):
        """
        60 ms, 15.4 MB
        """
        n = len(nums)
        k = k % n
        nums[:k], nums[k:] = nums[n - k:], nums[:n - k]

    def rotate(self, nums, k):
        """
        use extra array
        64 ms, 15.2 MB
        """
        n = len(nums)
        a = [0] * n
        for i in range(n):
            a[(i + k) % n] = nums[i]
        for i in range(n):
            nums[i] = a[i]

    def rotate(self, nums, k):
        """
        cyclic replacement
        """
        n = len(nums)
        k = k % n
        cnt = 0
        start = 0
        while cnt < n:
            curr = start
            prev = nums[start]
            while True:
                nxt = (curr + k) % n
                temp = nums[nxt]
                nums[nxt] = prev
                prev = temp
                curr = nxt
                cnt += 1
                if start == curr:
                    break
            start += 1
