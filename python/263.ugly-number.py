#
# @lc app=leetcode id=263 lang=python3
#
# [263] Ugly Number
#
# https://leetcode.com/problems/ugly-number/description/
#
# algorithms
# Easy (40.53%)
# Total Accepted:    156.3K
# Total Submissions: 385.1K
# Testcase Example:  '6'
#
# Write a program to check whether a given number is an ugly number.
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
# 
# Example 1:
# 
# 
# Input: 6
# Output: true
# Explanation: 6 = 2 × 3
# 
# Example 2:
# 
# 
# Input: 8
# Output: true
# Explanation: 8 = 2 × 2 × 2
# 
# 
# Example 3:
# 
# 
# Input: 14
# Output: false 
# Explanation: 14 is not ugly since it includes another prime factor 7.
# 
# 
# Note:
# 
# 
# 1 is typically treated as an ugly number.
# Input is within the 32-bit signed integer range: [−231,  231 − 1].
# 
#
class Solution:
    # def isUgly(self, num: int) -> bool:
    def isUgly(self, num):
        if num == 1:
            return True
        if num == 0:
            return False
        factors = [2,3,5]
        for f in factors: 
            d, r = divmod(num, f)
            if d in [2,3,5] and r == 0:
                return True
        d, r = divmod(num, 2)
        if r == 0:
            return self.isUgly(d)
        d, r = divmod(num, 3)
        if r == 0:
            return self.isUgly(d)
        d, r = divmod(num, 5)
        if r == 0:
            return self.isUgly(d)
        else:
            return False


# s = Solution()
# print(s.isUgly(6))
# print(s.isUgly(8))
# print(s.isUgly(14))






















        
