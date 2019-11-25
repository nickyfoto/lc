#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
# https://leetcode.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (43.95%)
# Total Accepted:    397.1K
# Total Submissions: 900.9K
# Testcase Example:  '2'
#
# You are climbing a stair case. It takes n steps to reach to the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?
# 
# Note: Given n will be a positive integer.
# 
# Example 1:
# 
# 
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# 
# 
# Example 2:
# 
# 
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
# 
# 
#
class Solution:
    # def climbStairs(self, n: int) -> int:
    def climbStairs(self, n):
    	if n <= 2:
    		return n
    	L = [0, 1, 2]
    	for i in range(3, n+1):
    		L.append(L[i-2]+L[i-1])
    	# print(L)
    	return L[n]

# s = Solution()
# print(s.climbStairs(2))
# print(s.climbStairs(3))
# print(s.climbStairs(4))
# print(s.climbStairs(5))
# print(s.climbStairs(6))













        
