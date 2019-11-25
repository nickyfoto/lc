#
# @lc app=leetcode id=709 lang=python3
#
# [709] To Lower Case
#
# https://leetcode.com/problems/to-lower-case/description/
#
# algorithms
# Easy (76.63%)
# Total Accepted:    104.4K
# Total Submissions: 135.9K
# Testcase Example:  '"Hello"'
#
# Implement function ToLowerCase() that has a string parameter str, and returns
# the same string in lowercase.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: "Hello"
# Output: "hello"
# 
# 
# 
# Example 2:
# 
# 
# Input: "here"
# Output: "here"
# 
# 
# 
# Example 3:
# 
# 
# Input: "LOVELY"
# Output: "lovely"
# 
# 
# 
# 
# 
#
class Solution:
    # def toLowerCase(self, str: str) -> str:
    def toLowerCase(self, str):
        l = list(str)
        for i in range(len(l)):
            if 64 < ord(l[i]) and ord(l[i]) < 97:
                l[i] = chr(ord(l[i]) + 32)
        return "".join(l)

# s = Solution()
# str = "LOVELY"
# print(s.toLowerCase(str))
        
