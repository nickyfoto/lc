#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (25.25%)
# Total Accepted:    690K
# Total Submissions: 2.7M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
# 
# Example 1:
# 
# 
# Input: 123
# Output: 321
# 
# 
# Example 2:
# 
# 
# Input: -123
# Output: -321
# 
# 
# Example 3:
# 
# 
# Input: 120
# Output: 21
# 
# 
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of
# this problem, assume that your function returns 0 when the reversed integer
# overflows.
# 
#
class Solution:
    # def reverse(self, x: int) -> int:
    def reverse(self, x):
        # if x < 10 and -10 < x:
        #     return x
        # i = 1
        # d, r = divmod(x, 10)
        # while d > 0:
        #     print(d, r)
        #     d, r = divmod(d, 10)
        if x == 0:
            return 0
        l = list(str(x))
        l.reverse()
        i = 0
        while l[0] == '0':
            l.pop(0)
        if l[-1] == '-':
            l = ['-'] + l[:-1] 
        res = int("".join(l))
        if res > 2**31 - 1 or res < - 2**31:
            return 0
        return res

# s = Solution()
# x = 123
# print(s.reverse(x))
# x = -123
# print(s.reverse(x))
# x = 120
# print(s.reverse(x))




























        
