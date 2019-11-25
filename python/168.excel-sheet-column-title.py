#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#
# https://leetcode.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (28.81%)
# Total Accepted:    171.7K
# Total Submissions: 593.2K
# Testcase Example:  '1'
#
# Given a positive integer, return its corresponding column title as appear in
# an Excel sheet.
# 
# For example:
# 
# 
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB 
# ⁠   ...
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: "A"
# 
# 
# Example 2:
# 
# 
# Input: 28
# Output: "AB"
# 
# 
# Example 3:
# 
# 
# Input: 701
# Output: "ZY"
# 
#
class Solution:
    # def convertToTitle(self, n: int) -> str:
    def convertToTitle(self, n, debug=False):
        t = 64
        res = ""
        print('n=', n) if debug else None
        if n <= 26:
            res = chr(n+t)
            return res
        else:
            d, n = divmod(n, 26)
            if n == 0 and d > 1:
                return self.convertToTitle(d-1, debug=debug) + self.convertToTitle(26, debug=debug)    
            return self.convertToTitle(d, debug=debug) + self.convertToTitle(n, debug=debug)

































