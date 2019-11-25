#
# @lc app=leetcode id=824 lang=python3
#
# [824] Goat Latin
#
# https://leetcode.com/problems/goat-latin/description/
#
# algorithms
# Easy (57.85%)
# Total Accepted:    33.3K
# Total Submissions: 57.4K
# Testcase Example:  '"I speak Goat Latin"'
#
# A sentence S is given, composed of words separated by spaces. Each word
# consists of lowercase and uppercase letters only.
# 
# We would like to convert the sentence to "Goat Latin" (a made-up language
# similar to Pig Latin.)
# 
# The rules of Goat Latin are as follows:
# 
# 
# If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of
# the word.
# For example, the word 'apple' becomes 'applema'.
# 
# If a word begins with a consonant (i.e. not a vowel), remove the first letter
# and append it to the end, then add "ma".
# For example, the word "goat" becomes "oatgma".
# 
# Add one letter 'a' to the end of each word per its word index in the
# sentence, starting with 1.
# For example, the first word gets "a" added to the end, the second word gets
# "aa" added to the end and so on.
# 
# 
# Return the final sentence representing the conversion from S to Goat
# Latin. 
# 
# 
# 
# Example 1:
# 
# 
# Input: "I speak Goat Latin"
# Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
# 
# 
# Example 2:
# 
# 
# Input: "The quick brown fox jumped over the lazy dog"
# Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa
# hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
# 
# 
# 
# 
# Notes:
# 
# 
# S contains only uppercase, lowercase and spaces. Exactly one space between
# each word.
# 1 <= S.length <= 150.
# 
# 
#
class Solution:
    def toGoatLatin(self, S: str) -> str:
        S = S.split()
        n = len(S)
        vowels = list('aeiou')+list('AEIOU')
        for i in range(n):
            # If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of
            # the word.
            if S[i][0] in vowels:
                S[i] = S[i]+'ma'+'a'*(i+1)
            # If a word begins with a consonant (i.e. not a vowel), remove the first letter
            # and append it to the end, then add "ma".
            # For example, the word "goat" becomes "oatgma".
            else:
                S[i] = S[i][1:]+ S[i][0]+'ma' + 'a'*(i+1)

        # print(S)
        return " ".join(S)

# s = Solution()
# S = "I speak Goat Latin"
# print(s.toGoatLatin(S) == "Imaa peaksmaaa oatGmaaaa atinLmaaaaa")


# S = "The quick brown fox jumped over the lazy dog"
# print(s.toGoatLatin(S) == "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa")














        
