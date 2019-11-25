#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#
# https://leetcode.com/problems/sum-of-two-integers/description/
#
# algorithms
# Easy (50.91%)
# Total Accepted:    137.8K
# Total Submissions: 270.9K
# Testcase Example:  '1\n2'
#
# Calculate the sum of two integers a and b, but you are not allowed to use the
# operator + and -.
# 
# 
# Example 1:
# 
# 
# Input: a = 1, b = 2
# Output: 3
# 
# 
# 
# Example 2:
# 
# 
# Input: a = -2, b = 3
# Output: 1
# 
# 
# 
# 
#
class Solution:
    def getSum(self, a: int, b: int) -> int:
        print(a, b)
        if b < 0 and a > 0 and a > abs(b):
            return - self.getSum(-b, -a)
        elif b < 0 and a > 0 and a == abs(b):
            return 0
        elif b > 0 and a < 0 and b > abs(a):
            return self.getSum(b, a)
        elif b > 0 and a < 0 and b == abs(a):
            return 0
        else:
            if b == 0:
                return a
            else:
                return self.getSum(a^b, (a&b)<<1)
        # return int("".join(self.res), 2)
        
# s = Solution()
# a = -14
# b = 16
# print(s.getSum(a, b))
# # a = 1
# b = 2
# print(s.getSum(a, b))
# a = -2
# b = -3
# print(s.getSum(a, b))
# a = 2
# b = -3
# print(s.getSum(a, b))
# a = -3
# b = 2
# print(s.getSum(a, b))
# a = 3
# b = -2
# print(s.getSum(a, b))
# a = -2
# b = 3
# print(s.getSum(a, b))


