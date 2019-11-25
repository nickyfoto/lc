#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
# https://leetcode.com/problems/ransom-note/description/
#
# algorithms
# Easy (50.00%)
# Total Accepted:    116.3K
# Total Submissions: 231.6K
# Testcase Example:  '"a"\n"b"'
#
# 
# Given an arbitrary ransom note string and another string containing letters
# from all the magazines, write a function that will return true if the ransom 
# note can be constructed from the magazines ; otherwise, it will return
# false. 
# 
# 
# Each letter in the magazine string can only be used once in your ransom
# note.
# 
# 
# Note:
# You may assume that both strings contain only lowercase letters.
# 
# 
# 
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
# 
# 
#
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # dm = {}
        def getD(str):
            d = {}
            for i in str:
                if i not in d:
                    d[i] = 1
                else:
                    d[i] += 1
            return d
        dm = getD(magazine)
        dr = getD(ransomNote)

        for k, v in dr.items():
            if k not in dm or dm[k] < dr[k]:
                return False
        return True





