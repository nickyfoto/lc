#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#
# https://leetcode.com/problems/jewels-and-stones/description/
#
# algorithms
# Easy (82.98%)
# Total Accepted:    250.3K
# Total Submissions: 301.3K
# Testcase Example:  '"aA"\n"aAAbbbb"'
#
# You're given strings J representing the types of stones that are jewels, and
# S representing the stones you have.  Each character in S is a type of stone
# you have.  You want to know how many of the stones you have are also jewels.
# 
# The letters in J are guaranteed distinct, and all characters in J and S are
# letters. Letters are case sensitive, so "a" is considered a different type of
# stone from "A".
# 
# Example 1:
# 
# 
# Input: J = "aA", S = "aAAbbbb"
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: J = "z", S = "ZZ"
# Output: 0
# 
# 
# Note:
# 
# 
# S and J will consist of letters and have length at most 50.
# The characters in J are distinct.
# 
# 
#
class Solution:
    # def numJewelsInStones(self, J: str, S: str) -> int:
    def numJewelsInStones(self, J, S):
        # print([s for s in S if s in J])
        return len([S.count(s) for s in S if s in J])
        
# s = Solution()
# J = "aA"
# S = "aAAbbbb"
# print(s.numJewelsInStones(J, S))
