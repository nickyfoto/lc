#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#
# https://leetcode.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (27.20%)
# Likes:    2707
# Dislikes: 119
# Total Accepted:    244.8K
# Total Submissions: 900K
# Testcase Example:  '"(()"'
#
# Given a string containing just the characters '(' and ')', find the length of
# the longest valid (well-formed) parentheses substring.
# 
# Example 1:
# 
# 
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
# 
# 
# Example 2:
# 
# 
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"
# 
# 
#

# @lc code=start
class Solution:
    # def longestValidParentheses(self, s: str) -> int:
    def longestValidParentheses_answer(self, s):
        if not s:
            return 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i - 1] == "(":
                    if i > 1:
                        dp[i] = dp[i - 2] + 2
                    else:
                        dp[i] = 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    if i - dp[i - 1] > 1:
                        dp[i] = dp[i - 1] + dp[i - dp[i - 1] - 2] + 2
                    else:
                        dp[i] = dp[i - 1] + 2
        return max(dp)

    def longestValidParentheses_me(self, s):
        """
        me
        """
        if not s:
            return 0
        dp = [0] * len(s)
        un_used_lp = []
        for i in range(0, len(s)):
            if s[i] == ')':
                if i > 0:
                    # print('i=', i)
                    if s[i - 1] == "(":
                        un_used_lp.pop()
                        if i > 1:
                            dp[i] = dp[i - 2] + 2
                        else:
                            dp[i] = 2
                    else:
                        # todo
                        # print(un_used_lp)
                        if un_used_lp:
                            u = un_used_lp.pop() 
                            dp[i] = i - u + 1
                            if u > 0:
                                dp[i] += dp[u - 1]
            else:
                un_used_lp.append(i)
        # print(dp)
        return max(dp)


    def longestValidParentheses_stack(self, s):
        """
        official stack
        """
        stack = [-1]
        mx = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    mx = max(mx, i - stack[-1])
        return mx

    
# @lc code=end
