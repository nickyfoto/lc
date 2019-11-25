#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#
# https://leetcode.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (41.57%)
# Total Accepted:    159.9K
# Total Submissions: 383.7K
# Testcase Example:  '"hello"'
#
# Write a function that takes a string as input and reverse only the vowels of
# a string.
# 
# Example 1:
# 
# 
# Input: "hello"
# Output: "holle"
# 
# 
# 
# Example 2:
# 
# 
# Input: "leetcode"
# Output: "leotcede"
# 
# 
# Note:
# The vowels does not include the letter "y".
# 
# 
# 
#
class Solution:
    # def reverseVowels(self, s: str) -> str:
    def reverseVowels(self, s):
        n = len(s)
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowels_indices = [idx for idx in range(n) if s[idx] in vowels]
        # print(vowels_indices)
        s = list(s)
        mid = len(vowels_indices) // 2
        for i in range(mid):
            # print(s[vowels_indices[i]], s[vowels_indices[-(i+1)]])
            s[vowels_indices[i]], s[vowels_indices[-(i+1)]] = s[vowels_indices[-(i+1)]], s[vowels_indices[i]]
        # print(s)
        return "".join(s)

# sol = Solution()
# s = 'hello'
# print(sol.reverseVowels(s))
# s = 'leetcode'
# print(sol.reverseVowels(s))