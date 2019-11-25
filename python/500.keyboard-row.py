#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#
# https://leetcode.com/problems/keyboard-row/description/
#
# algorithms
# Easy (62.30%)
# Total Accepted:    90.1K
# Total Submissions: 144.5K
# Testcase Example:  '["Hello","Alaska","Dad","Peace"]'
#
# Given a List of words, return the words that can be typed using letters of
# alphabet on only one row's of American keyboard like the image below.
# 
# 
# 
# 
# 
# 
# Example:
# 
# 
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
# 
# 
# 
# 
# Note:
# 
# 
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.
# 
# 
#
class Solution:
    # def findWords(self, words: List[str]) -> List[str]:
    def findWords(self, words):
        row1 = dict(zip(list('qwertyuiop'), [None] * len('qwertyuiop')))
        row2 = dict(zip(list('asdfghjkl'), [None] * len('asdfghjkl')))
        row3 = dict(zip(list('zxcvbnm'), [None] * len('zxcvbnm')))
        # print(row1)
        res = []
        for word in words:
            for row in [row1, row2, row3]:
                if all(map(lambda x: x in row, word.lower())):
                    res.append(word)
                    break
        return res
# s = Solution()
# words = ["Hello", "Alaska", "Dad", "Peace"]
# print(s.findWords(words))