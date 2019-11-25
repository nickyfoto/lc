#
# @lc app=leetcode id=856 lang=python3
#
# [856] Score of Parentheses
#
# https://leetcode.com/problems/score-of-parentheses/description/
#
# algorithms
# Medium (57.33%)
# Total Accepted:    22.4K
# Total Submissions: 39.1K
# Testcase Example:  '"()"'
#
# Given a balanced parentheses string S, compute the score of the string based
# on the following rule:
# 
# 
# () has score 1
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: "()"
# Output: 1
# 
# 
# 
# Example 2:
# 
# 
# Input: "(())"
# Output: 2
# 
# 
# 
# Example 3:
# 
# 
# Input: "()()"
# Output: 2
# 
# 
# 
# Example 4:
# 
# 
# Input: "(()(()))"
# Output: 6
# 
# 
# 
# 
# Note:
# 
# 
# S is a balanced parentheses string, containing only ( and ).
# 2 <= S.length <= 50
# 
# 
# 
# 
# 
# 
#
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        
        def recur(S):
            n = len(S)
            if n == 2:
                return 1
            stack = []
            res = 0
            l, r = 0, 0
            for i in range(n):
                if S[i] == '(':
                    stack.append('(')
                    l += 1
                else:
                    stack.append(')')
                    r += 1
                if l == r:
                    if l == 1:
                        res += l
                    else:
                        res += recur("".join(stack[1:-1])) * 2
                    stack = []
                    l, r = 0, 0
            # print(res) if debug else None
            return res
        return recur(S)

# s = Solution()
# S = "()"
# print(s.scoreOfParentheses(S))
# S = "(())"
# print(s.scoreOfParentheses(S))
# S = "()()"
# print(s.scoreOfParentheses(S))
# S = "(()(()))"
# print(s.scoreOfParentheses(S))

# S = "((()()))"
# print(s.scoreOfParentheses(S)) # exp 8
