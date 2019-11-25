#
# @lc app=leetcode id=290 lang=python3
#
# [290] Word Pattern
#
# https://leetcode.com/problems/word-pattern/description/
#
# algorithms
# Easy (35.09%)
# Total Accepted:    145.6K
# Total Submissions: 413.2K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# Given a pattern and a string str, find if str follows the same pattern.
# 
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty word in str.
# 
# Example 1:
# 
# 
# Input: pattern = "abba", str = "dog cat cat dog"
# Output: true
# 
# Example 2:
# 
# 
# Input:pattern = "abba", str = "dog cat cat fish"
# Output: false
# 
# Example 3:
# 
# 
# Input: pattern = "aaaa", str = "dog cat cat dog"
# Output: false
# 
# Example 4:
# 
# 
# Input: pattern = "abba", str = "dog dog dog dog"
# Output: false
# 
# Notes:
# You may assume pattern contains only lowercase letters, and str contains
# lowercase letters that may be separated by a single space.
# 
#
from collections import Counter
class Solution:
    # def wordPattern(self, pattern: str, str: str) -> bool:
    def wordPattern(self, pattern, str):
        # pc = Counter(pattern).most_common()
        # ps = Counter(str.split()).most_common()



        # return [v for k, v in pc] == [v for k, v in ps]


    # def isIsomorphic(self, s: str, t: str) -> bool:
        # if count == 1: only require number of letters are the same
        # if count > 1: must have the same position
        s = str.split()
        def getIndexD(s):
            d = {}
            n = len(s)
            for i in range(n):
                if s[i] not in d:
                    d[s[i]] = [i]
                else:
                    d[s[i]].append(i)
            return d
        indexP = getIndexD(pattern)
        indexS = getIndexD(s)
        if len(indexP) != len(indexS):
            return False
        # print(indexS)
        pc = Counter(pattern).most_common()
        ps = Counter(s).most_common()
        for i in range(len(pc)):
            if indexP[pc[i][0]] != indexS[ps[i][0]]:
                return False
        return True






















        
