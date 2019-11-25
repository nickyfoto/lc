#
# @lc app=leetcode id=258 lang=python3
#
# [258] Add Digits
#
# https://leetcode.com/problems/add-digits/description/
#
# algorithms
# Easy (53.90%)
# Total Accepted:    237.3K
# Total Submissions: 439K
# Testcase Example:  '38'
#
# Given a non-negative integer num, repeatedly add all its digits until the
# result has only one digit.
# 
# Example:
# 
# 
# Input: 38
# Output: 2 
# Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
# Since 2 has only one digit, return it.
# 
# 
# Follow up:
# Could you do it without any loop/recursion in O(1) runtime?
#
class Solution:
    # def addDigits(self, num: int) -> int:
    def addDigits(self, num: int) -> int:
        if num >= 10:
            return self.addDigits(num % 10 + self.addDigits(num // 10))
        else:
            return num
        
# s = Solution()
# print(s.addDigits(38))
# print(s.addDigits(138))
# print(s.addDigits(567))
# print(s.addDigits(1234))