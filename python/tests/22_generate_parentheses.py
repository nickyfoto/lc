#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (56.62%)
# Total Accepted:    381.2K
# Total Submissions: 673K
# Testcase Example:  '3'
#
# 
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# 
# For example, given n = 3, a solution set is:
# 
# 
# [
# ⁠ "((()))",
# ⁠ "(()())",
# ⁠ "(())()",
# ⁠ "()(())",
# ⁠ "()()()"
# ]
# 
#
class Solution:
    # def generateParenthesis(self, n: int) -> List[str]:
    def generateParenthesis(self, n):
        self.res = []
        def backtrack(left, right, temp):
            if len(temp) == 2 * n:
                self.res.append(temp)
            else:
                if left < n:
                    backtrack(left + 1, right, temp + '(')
                if right < left:
                    backtrack(left, right + 1, temp + ')')

        backtrack(0, 0, "")
        return self.res