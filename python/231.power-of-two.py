#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#
# https://leetcode.com/problems/power-of-two/description/
#
# algorithms
# Easy (41.83%)
# Total Accepted:    226.8K
# Total Submissions: 541.1K
# Testcase Example:  '1'
#
# Given an integer, write a function to determine if it is a power of two.
# 
# Example 1:
# 
# 
# Input: 1
# Output: true 
# Explanation: 20 = 1
# 
# 
# Example 2:
# 
# 
# Input: 16
# Output: true
# Explanation: 24 = 16
# 
# Example 3:
# 
# 
# Input: 218
# Output: false
# 
#
class Solution:
    # def isPowerOfTwo(self, n: int) -> bool:
    def isPowerOfTwo(self, n):
        if n == 1:
            return True
        i = 0
        t = 2**i
        while t <= n:
            if t == n:
                return True
            i += 1
            t = 2**i
        return False



# s = Solution()
# print(s.isPowerOfTwo(1))
# print(s.isPowerOfTwo(16))
# print(s.isPowerOfTwo(218))