#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#
# https://leetcode.com/problems/power-of-three/description/
#
# algorithms
# Easy (41.54%)
# Total Accepted:    182.7K
# Total Submissions: 438.7K
# Testcase Example:  '27'
#
# Given an integer, write a function to determine if it is a power of three.
# 
# Example 1:
# 
# 
# Input: 27
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: 0
# Output: false
# 
# Example 3:
# 
# 
# Input: 9
# Output: true
# 
# Example 4:
# 
# 
# Input: 45
# Output: false
# 
# Follow up:
# Could you do it without using any loop / recursion?
#
class Solution:
    # def isPowerOfThree(self, n: int) -> bool:
    def isPowerOfThree(self, n):
        if n == 1:
            return True
        i = 0
        t = 3**i
        while t <= n:
            if t == n:
                return True
            i += 1
            t = 3**i
        return False
