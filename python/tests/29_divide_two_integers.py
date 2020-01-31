#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#
# https://leetcode.com/problems/divide-two-integers/description/
#
# algorithms
# Medium (16.19%)
# Likes:    906
# Dislikes: 4383
# Total Accepted:    240.5K
# Total Submissions: 1.5M
# Testcase Example:  '10\n3'
#
# Given two integers dividend and divisor, divide two integers without using
# multiplication, division and mod operator.
# 
# Return the quotient after dividing dividend by divisor.
# 
# The integer division should truncate toward zero.
# 
# Example 1:
# 
# 
# Input: dividend = 10, divisor = 3
# Output: 3
# 
# Example 2:
# 
# 
# Input: dividend = 7, divisor = -3
# Output: -2
# 
# Note:
# 
# 
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose
# of this problem, assume that your function returns 2^31 − 1 when the division
# result overflows.
# 
# 
#

# @lc code=start
class Solution:
    def divide(self, dividend, divisor):
        if dividend < 0 and divisor < 0:
            return self.divide(- dividend, - divisor)
        if divisor == 1:
            limit = 2**31 - 1
            if dividend > limit:
                return limit
            return dividend
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
            return - self.divide(abs(dividend), abs(divisor))
        if dividend == 0:
            return 0
        if dividend < divisor:
            return 0
        if dividend == divisor:
            return 1
        
        def get_shift(dividend, divisor):
            # print('here', dividend, divisor)

            if dividend == divisor:
                return 1, 0
            bits = 0
            while divisor << 1 < dividend:
                divisor <<= 1
                bits += 1
            if bits:
                quo = 1 << bits
                r = dividend - divisor
                return quo, r
            else:
                if dividend > divisor:
                    return 1, dividend - divisor
                else:
                    return 0, 0
            
            
        res = 0
        while dividend:
            quo, dividend = get_shift(dividend, divisor)
            res += quo
        
        limit = 2**31 - 1
        if res > limit:
            return limit
        return res
# @lc code=end
