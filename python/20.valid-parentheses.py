#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (36.63%)
# Total Accepted:    618.3K
# Total Submissions: 1.7M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
# 
# An input string is valid if:
# 
# 
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# 
# 
# Note that an empty string is also considered valid.
# 
# Example 1:
# 
# 
# Input: "()"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "()[]{}"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: "(]"
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: "([)]"
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: "{[]}"
# Output: true
# 
# 
#
class Solution:
    # def isValid(self, s: str) -> bool:
    def isValid(self, s: str):
        stack = []
        for p in s:
            if p in ['(', '[', '{']:
                stack.append(p)
            else:
                if p == ')':
                    if not stack or (stack and stack.pop() != '('):
                        return False
                elif p == ']':
                    if not stack or (stack and stack.pop() != '['):
                        return False
                elif p == '}':
                    if not stack or (stack and stack.pop() != '{'):
                        return False
        if stack:
            return False
        return True

# sol = Solution()
# s = "()"
# print(sol.isValid(s))
# s = "()[]{}"
# print(sol.isValid(s))

# s = "(]"
# print(sol.isValid(s))
# s = "([)]"
# print(sol.isValid(s))

# s = "{[]}"
# print(sol.isValid(s))
























        
