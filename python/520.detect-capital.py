#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#
# https://leetcode.com/problems/detect-capital/description/
#
# algorithms
# Easy (52.50%)
# Total Accepted:    87.3K
# Total Submissions: 166K
# Testcase Example:  '"USA"'
#
# Given a word, you need to judge whether the usage of capitals in it is right
# or not.
# 
# We define the usage of capitals in a word to be right when one of the
# following cases holds:
# 
# 
# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# 
# Otherwise, we define that this word doesn't use capitals in a right way.
# 
# 
# 
# Example 1:
# 
# 
# Input: "USA"
# Output: True
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: "FlaG"
# Output: False
# 
# 
# 
# 
# Note: The input will be a non-empty word consisting of uppercase and
# lowercase latin letters.
# 
#
import string
class Solution:
    # def detectCapitalUse(self, word: str) -> bool:
    def detectCapitalUse(self, word):
        # def capital(word):
            # if len(word) <= 1:
            #     return False


        return all(map(lambda x: x in string.ascii_uppercase, word)) or \
               all(map(lambda x: x in string.ascii_lowercase, word)) or \
               (word[0] in string.ascii_uppercase and all(map(lambda x: x in string.ascii_lowercase, word[1:])))


# s = Solution()
# word = 'USA'
# print(s.detectCapitalUse(word))
# word = 'leetcode'
# print(s.detectCapitalUse(word))
# word = 'FlaG'
# print(s.detectCapitalUse(word))
        
