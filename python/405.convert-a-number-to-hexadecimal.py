#
# @lc app=leetcode id=405 lang=python3
#
# [405] Convert a Number to Hexadecimal
#
# https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/
#
# algorithms
# Easy (41.95%)
# Total Accepted:    48.9K
# Total Submissions: 116.3K
# Testcase Example:  '26'
#
# 
# Given an integer, write an algorithm to convert it to hexadecimal. For
# negative integer, two’s complement method is used.
# 
# 
# Note:
# 
# All letters in hexadecimal (a-f) must be in lowercase.
# The hexadecimal string must not contain extra leading 0s. If the number is
# zero, it is represented by a single zero character '0'; otherwise, the first
# character in the hexadecimal string will not be the zero character.
# The given number is guaranteed to fit within the range of a 32-bit signed
# integer.
# You must not use any method provided by the library which converts/formats
# the number to hex directly.
# 
# 
# 
# Example 1:
# 
# Input:
# 26
# 
# Output:
# "1a"
# 
# 
# 
# Example 2:
# 
# Input:
# -1
# 
# Output:
# "ffffffff"
# 
# 
#
class Solution:
    # def toHex(self, num: int) -> str:
    def toHex(self, num):
        d = {0: '0', 1: '1', 2: '2', 3: '3',
             4: '4', 5: '5', 6: '6', 7: '7',
             8: '8', 9: '9', 10: 'a', 11: 'b',
             12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        if num >= 0:
            self.res = []
            i = 0
            def recur(n):
                # print(n)
                a, b = divmod(n, 16)
                self.res.insert(0, d[b])
                if a > 0:
                    recur(a)
            recur(num)
            return "".join(self.res)
        else:
            return self.toHex(2**32 + num)
            # print(self.res)

# s = Solution()
# print(s.toHex(26))
# print(s.toHex(256))
# print(s.toHex(3840))
# print(s.toHex(4096))
# print(s.toHex(4294967295))
# print(s.toHex(-1))






























