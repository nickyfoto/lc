#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#
# https://leetcode.com/problems/repeated-substring-pattern/description/
#
# algorithms
# Easy (39.98%)
# Total Accepted:    83K
# Total Submissions: 207K
# Testcase Example:  '"abab"'
#
# Given a non-empty string check if it can be constructed by taking a substring
# of it and appending multiple copies of the substring together. You may assume
# the given string consists of lowercase English letters only and its length
# will not exceed 10000.
# 
# 
# 
# Example 1:
# 
# 
# Input: "abab"
# Output: True
# Explanation: It's the substring "ab" twice.
# 
# 
# Example 2:
# 
# 
# Input: "aba"
# Output: False
# 
# 
# Example 3:
# 
# 
# Input: "abcabcabcabc"
# Output: True
# Explanation: It's the substring "abc" four times. (And the substring "abcabc"
# twice.)
# 
# 
#
class Solution:
    # def repeatedSubstringPattern(self, s: str) -> bool:
    def repeatedSubstringPattern(self, s):
        n = len(s)
        # print('n=', n)
        i = 1
        sub = s[:i]
        l = len(sub)
        while i < n:
            # print('s[i:i+l]=', s[i:i+l])
            count = 0
            while s[i:i+l] == sub:
                # print('here', 'i=', i, 'l=', l)
                i += l
                count += l
            if i == n:
                return True
            # print('i=', i, 'sub=', sub, 'count=', count)
            i -= count
            i += 1
            sub = s[:i]
            l += 1
        return False

# S = Solution()
# s = "abcabcabcabc"
# print(S.repeatedSubstringPattern(s))



# s = "abab"
# print(S.repeatedSubstringPattern(s))



# s = "aba"
# print(S.repeatedSubstringPattern(s))

# s = "abaababaab"
# print(S.repeatedSubstringPattern(s))
















        
