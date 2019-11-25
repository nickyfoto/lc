#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/
#
# algorithms
# Easy (63.42%)
# Total Accepted:    12.2K
# Total Submissions: 19.2K
# Testcase Example:  '"abbaca"'
#
# Given a string S of lowercase letters, a duplicate removal consists of
# choosing two adjacent and equal letters, and removing them.
# 
# We repeatedly make duplicate removals on S until we no longer can.
# 
# Return the final string after all such duplicate removals have been made.  It
# is guaranteed the answer is unique.
# 
# 
# 
# Example 1:
# 
# 
# Input: "abbaca"
# Output: "ca"
# Explanation: 
# For example, in "abbaca" we could remove "bb" since the letters are adjacent
# and equal, and this is the only possible move.  The result of this move is
# that the string is "aaca", of which only "aa" is possible, so the final
# string is "ca".
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= S.length <= 20000
# S consists only of English lowercase letters.
# 
#
class Solution:
    # def removeDuplicates(self, S: str) -> str:
    def removeDuplicates(self, S):
        stack = []
        n = len(S)
        i = 0
        while i < n:
            if not stack:
                stack.append(S[i])
            else:
                while stack and i < n and S[i] == stack[-1]:
                    stack.pop()
                    i += 1
                if i < n:
                    stack.append(S[i])
            i += 1
        return "".join(stack)


# s = Solution()
# S = "abbaca"
# print(s.removeDuplicates(S))


# S = "aaaaaaaa"
# print(s.removeDuplicates(S))

# S = "aababaab"
# print(s.removeDuplicates(S))





































