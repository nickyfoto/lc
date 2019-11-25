#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#
# https://leetcode.com/problems/excel-sheet-column-number/description/
#
# algorithms
# Easy (51.27%)
# Total Accepted:    218.6K
# Total Submissions: 424.9K
# Testcase Example:  '"A"'
#
# Given a column title as appear in an Excel sheet, return its corresponding
# column number.
# 
# For example:
# 
# 
# ⁠   A -> 1
# ⁠   B -> 2
# ⁠   C -> 3
# ⁠   ...
# ⁠   Z -> 26
# ⁠   AA -> 27
# ⁠   AB -> 28 
# ⁠   ...
# 
# 
# Example 1:
# 
# 
# Input: "A"
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: "AB"
# Output: 28
# 
# 
# Example 3:
# 
# 
# Input: "ZY"
# Output: 701=26*26+25
# 
#
class Solution:
    def titleToNumber(self, s: str) -> int:
        n = len(s)
        if n == 1:
            return ord(s) - 64
        else:
            return self.titleToNumber(s[-1]) + self.titleToNumber(s[:-1]) * 26

s = Solution()
# l = 'A'
# print(s.titleToNumber(l))
# l = 'AB'
# print(s.titleToNumber(l))
# l = 'ZY'
# print(s.titleToNumber(l))
# l = 'AAA'
# print(s.titleToNumber(l))
l = 'EZZI'
print(s.titleToNumber(l))
        
