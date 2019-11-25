#
# @lc app=leetcode id=1021 lang=python3
#
# [1021] Remove Outermost Parentheses
#
# https://leetcode.com/problems/remove-outermost-parentheses/description/
#
# algorithms
# Easy (78.00%)
# Total Accepted:    20.2K
# Total Submissions: 26.2K
# Testcase Example:  '"(()())(())"'
#
# A valid parentheses string is either empty (""), "(" + A + ")", or A + B,
# where A and B are valid parentheses strings, and + represents string
# concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid
# parentheses strings.
# 
# A valid parentheses string S is primitive if it is nonempty, and there does
# not exist a way to split it into S = A+B, with A and B nonempty valid
# parentheses strings.
# 
# Given a valid parentheses string S, consider its primitive decomposition: S =
# P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.
# 
# Return S after removing the outermost parentheses of every primitive string
# in the primitive decomposition of S.
# 
# 
# 
# Example 1:
# 
# 
# Input: "(()())(())"
# Output: "()()()"
# Explanation: 
# The input string is "(()())(())", with primitive decomposition "(()())" +
# "(())".
# After removing outer parentheses of each part, this is "()()" + "()" =
# "()()()".
# 
# 
# 
# Example 2:
# 
# 
# Input: "(()())(())(()(()))"
# Output: "()()()()(())"
# Explanation: 
# The input string is "(()())(())(()(()))", with primitive decomposition
# "(()())" + "(())" + "(()(()))".
# After removing outer parentheses of each part, this is "()()" + "()" +
# "()(())" = "()()()()(())".
# 
# 
# 
# Example 3:
# 
# 
# Input: "()()"
# Output: ""
# Explanation: 
# The input string is "()()", with primitive decomposition "()" + "()".
# After removing outer parentheses of each part, this is "" + "" = "".
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# S.length <= 10000
# S[i] is "(" or ")"
# S is a valid parentheses string
# 
# 
# 
# 
# 
# 
# 
#
class Solution:
    # def removeOuterParentheses(self, S: str) -> str:
    
    def removeOuterParentheses(self, S, debug=False):
        stack = []
        temp = []
        res = []
        n = len(S)
        l, r = 0, 0
        for i in range(n):
            if S[i] == '(':
                stack.append('(')
                l += 1
            else:
                stack.append(')')
                r += 1
            if l == r:
                res.extend(stack[1:-1])
                stack = []
                l, r = 0, 0
        print(res) if debug else None
        return "".join(res)
    """
    def removeOuterParentheses(self, S, debug=True):
        stack = []
        temp = []
        res = []
        n = len(S)
        for i in range(n):
            if S[i] == '(':
                stack.insert(0, '(')
                print('i=', i, 'add to stack', stack) if debug else None
            elif S[i] == ')':
                if len(stack) > 2:
                    temp.append(stack.pop())
                    temp.append(')')
                    print('i=', i, 'stack=', stack, 'temp=', temp) if debug else None
                elif len(stack) == 2:
                    temp.insert(0, stack.pop())
                    temp.append(')')
                    print('i=', i, 'stack=', stack, 'temp=', temp) if debug else None
                    res.extend(temp)
                    temp = []
                    print('i=', i, 'moving to res=', res) if debug else None
                else:
                    print('i=', i, 'liquid stack') if debug else None
                    res.extend(temp)
                    temp = []
                    stack = []
        print(res) if debug else None
        return "".join(res)
    """


# s = Solution()

# S = "(()())(())"
# print(s.removeOuterParentheses(S) == "()()()")

# S = "(()())(())(()(()))"
# print(s.removeOuterParentheses(S) == "()()()()(())")

# S = "(()(()))"
# print(s.removeOuterParentheses(S) == "()(())")

# S = "()()"
# print(s.removeOuterParentheses(S) == "")

# S = "((()())(()()))"
# print(s.removeOuterParentheses(S) == "(()())(()())")

# S = "(((((())))))"
# print(s.removeOuterParentheses(S) == "((((()))))")

