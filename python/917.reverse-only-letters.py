#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#
# https://leetcode.com/problems/reverse-only-letters/description/
#
# algorithms
# Easy (56.00%)
# Total Accepted:    29K
# Total Submissions: 51.7K
# Testcase Example:  '"ab-cd"'
#
# Given a string S, return the "reversed" string where all characters that are
# not a letter stay in the same place, and all letters reverse their
# positions.
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: "ab-cd"
# Output: "dc-ba"
# 
# 
# 
# Example 2:
# 
# 
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# 
# 
# 
# Example 3:
# 
# 
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
# 
# 
# 
# 
# 
# Note:
# 
# 
# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122 
# S doesn't contain \ or "
# 
# 
# 
# 
# 
#
class Solution:
    # def reverseOnlyLetters(self, S: str) -> str:
    def reverseOnlyLetters(self, S):
        import string
        q = []
        for s in S:
            if s in string.ascii_letters:
                q.append(s)
        n = len(S)
        S = list(S)
        for i in range(n):
            if S[i] in string.ascii_letters:
                S[i] = q.pop()
        return "".join(S)

# s = Solution()
# S = "a-bC-dEf-ghIj"
# print(s.reverseOnlyLetters(S))
