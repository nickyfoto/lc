#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#
# https://leetcode.com/problems/reverse-string/description/
#
# algorithms
# Easy (63.11%)
# Total Accepted:    426.9K
# Total Submissions: 674.7K
# Testcase Example:  '["h","e","l","l","o"]'
#
# Write a function that reverses a string. The input string is given as an
# array of characters char[].
# 
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
# 
# You may assume all the characters consist of printable ascii characters.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# 
# 
# 
# Example 2:
# 
# 
# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
# 
# 
# 
# 
#
class Solution:
    # def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    def reverseString(self, s):
        n = len(s) // 2
        for i in range(n):
            s[i], s[-(i+1)] = s[-(i+1)], s[i]
        
