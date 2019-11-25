#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#
# https://leetcode.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (34.29%)
# Total Accepted:    79.1K
# Total Submissions: 229.9K
# Testcase Example:  '"aba"'
#
# 
# Given a non-empty string s, you may delete at most one character.  Judge
# whether you can make it a palindrome.
# 
# 
# Example 1:
# 
# Input: "aba"
# Output: True
# 
# 
# 
# Example 2:
# acabaa
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# 
# 
# 
# Note:
# 
# The string will only contain lowercase characters a-z.
# The maximum length of the string is 50000.
# 
# 
#
class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = list(s)
        n = len(s)
        def IsPalindrome(s, n):
            # print(s)
            for i in range(n//2):
                if s[i] != s[-(i+1)]:
                    return False
            return True
        for i in range(n//2):
            if s[i] != s[-(i+1)]:
                l1 = s[:i] + s[i+1:]
                if IsPalindrome(l1, n-1):
                    return True
                else:

                    l2 = s[:-(i+1)] + s[n-i:]
                    # print(s, s[:-(i+1)], s[n-i:])
                    if IsPalindrome(l2, n-1):
                        return True
                    else:
                        return False
        return True
        

S = Solution()
# s = "aba" 
# print(S.validPalindrome(s))

# s = "abca"
# print(S.validPalindrome(s))

# s = "abc"
# print(S.validPalindrome(s))

# s = "tebbem"
# print(S.validPalindrome(s))























