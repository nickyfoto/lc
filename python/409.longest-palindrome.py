#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#
# https://leetcode.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (48.12%)
# Total Accepted:    100.8K
# Total Submissions: 208.8K
# Testcase Example:  '"abccccdd"'
#
# Given a string which consists of lowercase or uppercase letters, find the
# length of the longest palindromes that can be built with those letters.
# 
# This is case sensitive, for example "Aa" is not considered a palindrome
# here.
# 
# Note:
# Assume the length of given string will not exceed 1,010.
# 
# 
# Example: 
# 
# Input:
# "abccccdd"
# 
# Output:
# 7
# 
# Explanation:
# One longest palindrome that can be built is "dccaccd", whose length is 7.
# 
# 
#
class Solution:
    # def longestPalindrome(self, s: str) -> int:
    def longestPalindrome(self, s):
        # s = s.lower()
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        # print(d)
        # print(sum([v for k, v in d.items()]))
        # print(len(s))
        res = 0
        max_center = 0
        for k, v in d.items():
            if v % 2 == 0:
                # print(k, v)
                res += v
        # for k, v in d.items():
            else:
                if v > 1:
                    res += v - 1
                # if v > max_center:
                    # max_center = v
        for k, v in d.items():
            if v == 1 or v % 2 == 1:
                res += 1
                break
        # print(max_center)
        # res += max_center
        return res

# S = Solution()
# s = "abccccdd"

# print(S.longestPalindrome(s))

