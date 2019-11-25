#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#
# https://leetcode.com/problems/backspace-string-compare/description/
#
# algorithms
# Easy (46.03%)
# Total Accepted:    59.7K
# Total Submissions: 129.6K
# Testcase Example:  '"ab#c"\n"ad#c"'
#
# Given two strings S and T, return if they are equal when both are typed into
# empty text editors. # means a backspace character.
# 
# 
# Example 1:
# 
# 
# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac".
# 
# 
# 
# Example 2:
# 
# 
# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# 
# 
# 
# Example 3:
# 
# 
# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# 
# 
# 
# Example 4:
# 
# 
# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
# 
# 
# Note:
# 
# 
# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.
# 
# 
# Follow up:
# 
# 
# Can you solve it in O(N) time and O(1) space?
# 
# 
# 
# 
# 
# 
#
class Solution:
    # def backspaceCompare(self, S: str, T: str) -> bool:
    def backspaceCompare(self, S, T):
        stack_S = []
        stack_T = []
        for s in S:
            if s != '#':
                stack_S.append(s)
            else:
                if stack_S:
                    stack_S.pop()
        for s in T:
            if s != '#':
                stack_T.append(s)
            else:
                if stack_T:
                    stack_T.pop()
        if stack_S == stack_T:
            return True
        return False

# s = Solution()

# S = "ab#c"
# T = "ad#c"
# print(s.backspaceCompare(S, T))

# S = "ab##"
# T = "c#d#"
# print(s.backspaceCompare(S, T))

# S = "a##c"
# T = "#a#c"
# print(s.backspaceCompare(S, T))

# S = "a#c"
# T = "b"
# print(s.backspaceCompare(S, T))


























        
