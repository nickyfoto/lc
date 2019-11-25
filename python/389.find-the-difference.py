#
# @lc app=leetcode id=389 lang=python3
#
# [389] Find the Difference
#
# https://leetcode.com/problems/find-the-difference/description/
#
# algorithms
# Easy (53.16%)
# Total Accepted:    148.1K
# Total Submissions: 278.3K
# Testcase Example:  '"abcd"\n"abcde"'
#
# 
# Given two strings s and t which consist of only lowercase letters.
# 
# String t is generated by random shuffling string s and then add one more
# letter at a random position.
# 
# Find the letter that was added in t.
# 
# Example:
# 
# Input:
# s = "abcd"
# t = "abcde"
# 
# Output:
# e
# 
# Explanation:
# 'e' is the letter that was added.
# 
#
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        pass
        s = sum(map(ord, s))
        t = sum(map(ord, t))
        return chr(t - s)
# sol = Solution()
# s = "abcd"
# t = "abcde"
# print(sol.findTheDifference(s, t))