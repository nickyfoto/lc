#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (37.48%)
# Total Accepted:    211.5K
# Total Submissions: 561.7K
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
# 
# Two strings are isomorphic if the characters in s can be replaced to get t.
# 
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character but a character may map to itself.
# 
# Example 1:
# 
# 
# Input: s = "egg", t = "add"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "foo", t = "bar"
# Output: false
# 
# Example 3:
# 
# 
# Input: s = "paper", t = "title"
# Output: true
# 
# Note:
# You may assume both s and t have the same length.
# 
#
from collections import Counter
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # if count == 1: only require number of letters are the same
        # if count > 1: must have the same position
        def getIndexD(s):
            d = {}
            n = len(s)
            for i in range(n):
                if s[i] not in d:
                    d[s[i]] = [i]
                else:
                    d[s[i]].append(i)
            return d
        indexS = getIndexD(s)
        indexT = getIndexD(t)
        if len(indexS) != len(indexT):
            return False
        # print(indexS)
        cs = Counter(s).most_common()
        ct = Counter(t).most_common()
        for i in range(len(cs)):
            if indexT[ct[i][0]] != indexS[cs[i][0]]:
                return False
        return True
# S = Solution()
# s = "paper"
# t = "title"
# print(S.isIsomorphic(s, t))
# s = 'foo'
# s = 'bar'
# print(S.isIsomorphic(s, t))




















