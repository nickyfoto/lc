#
# @lc app=leetcode id=633 lang=python3
#
# [633] Sum of Square Numbers
#
# https://leetcode.com/problems/sum-of-square-numbers/description/
#
# algorithms
# Easy (32.72%)
# Total Accepted:    43.6K
# Total Submissions: 133.3K
# Testcase Example:  '5'
#
# Given a non-negative integer c, your task is to decide whether there're two
# integers a and b such that a2 + b2 = c.
# 
# Example 1:
# 
# 
# Input: 5
# Output: True
# Explanation: 1 * 1 + 2 * 2 = 5
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: 3
# Output: False
# 
# 
# 
# 
#
class Solution:
    # def judgeSquareSum(self, c: int) -> bool:
    def judgeSquareSum(self, c, debug=False):
        if c == 0:
            return True
        import math

        def findRoot(num):
            f = math.sqrt(num)
            if f - int(f) == 0:
                return num
            return None

        for i in range(int(math.sqrt(c)) + 1):
            # print('i=', i) if debug else None
            other = findRoot(c - i**2)
            if other and other + i**2 == c:
                print(i, other) if debug else None
                return True    
        return False





