#
# @lc app=leetcode id=557 lang=python3
#
# [557] Reverse Words in a String III
#
# https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
#
# algorithms
# Easy (64.29%)
# Total Accepted:    129.8K
# Total Submissions: 201.5K
# Testcase Example:  `"Let's take LeetCode contest"`
#
# Given a string, you need to reverse the order of characters in each word
# within a sentence while still preserving whitespace and initial word order.
# 
# Example 1:
# 
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# 
# 
# 
# Note:
# In the string, each word is separated by single space and there will not be
# any extra space in the string.
# 
#
class Solution:
    # def reverseWords(self, s: str) -> str:
    def reverseWords(self, s):
        def reverse(s):
            l = list(s)
            l.reverse()
            # n = len(s)
            # for i in range(n // 2 + 1):
                # l[i], l[-(i+1)] = l[-(i+1)], l[i]
            return "".join(l)
        # print(reverse("Let's"))
        # print(reverse("contest"))
        # print(reverse("take"))
        return " ".join(map(reverse, s.split(" ")))
# s = Solution()

# print(s.reverseWords("Let's take LeetCode contest")=="s'teL ekat edoCteeL tsetnoc")