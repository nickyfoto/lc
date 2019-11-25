#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (31.29%)
# Total Accepted:    371.2K
# Total Submissions: 1.2M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
# 
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
# 
# Example 1:
# 
# 
# Input: "A man, a plan, a canal: Panama"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: "race a car"
# Output: false
# 
# 
#
class Solution:
    # def isPalindrome(self, s: str) -> bool:
    def isPalindrome(self, s):
        fs = list(filter(str.isalnum, s.lower()))
        # print(fs)
        n = len(fs)
        for i in range(n//2):
            if fs[i] != fs[-(i+1)]:
                return False
        return True
# S = Solution()
# s = "A man, a plan, a canal: Panama"
# print(S.isPalindrome(s))
# s = "race a car"
# print(S.isPalindrome(s))