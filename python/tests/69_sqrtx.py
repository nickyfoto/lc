#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# https://leetcode.com/problems/sqrtx/description/
#
# algorithms
# Easy (31.11%)
# Total Accepted:    363.8K
# Total Submissions: 1.2M
# Testcase Example:  '4'
#
# Implement int sqrt(int x).
# 
# Compute and return the square root of x, where x is guaranteed to be a
# non-negative integer.
# 
# Since the return type is an integer, the decimal digits are truncated and
# only the integer part of the result is returned.
# 
# Example 1:
# 
# 
# Input: 4
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
# the decimal part is truncated, 2 is returned.
# 
# 
#
class Solution:
    # def mySqrt(self, x: int) -> int:
    def mySqrt(self, x):
        if x < 2: return x
        l, r = 0, x // 2
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid == x:
                return mid
            elif x < mid * mid:
                r = mid - 1
            else:
                l = mid + 1
        return r

# s = Solution()

# print(s.mySqrt(0))
# print(s.mySqrt(1))
# print(s.mySqrt(4))
# print(s.mySqrt(8))



