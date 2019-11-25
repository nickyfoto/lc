#
# @lc app=leetcode id=367 lang=python3
#
# [367] Valid Perfect Square
#
# https://leetcode.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (39.65%)
# Total Accepted:    108.8K
# Total Submissions: 274K
# Testcase Example:  '16'
#
# Given a positive integer num, write a function which returns True if num is a
# perfect square else False.
# 
# Note: Do not use any built-in library function such as sqrt.
# 
# Example 1:
# 
# 
# 
# Input: 16
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: 14
# Output: false
# 
# 
# 
#
class Solution:
    # def isPerfectSquare(self, num: int) -> bool:
    def isPerfectSquare(self, num):
    	if num == 1:
    		return True
    	i = 2
    	while not i**2 > num:
    		if i**2 == num:
    			return True
    		i += 1
    	return False

        
# s = Solution()
# num = 16
# print(s.isPerfectSquare(num))
# num = 14
# print(s.isPerfectSquare(num))





