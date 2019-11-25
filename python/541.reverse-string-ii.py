#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#
# https://leetcode.com/problems/reverse-string-ii/description/
#
# algorithms
# Easy (45.60%)
# Total Accepted:    62.1K
# Total Submissions: 135.6K
# Testcase Example:  '"abcdefg"\n2'
#
# 
# Given a string and an integer k, you need to reverse the first k characters
# for every 2k characters counting from the start of the string. If there are
# less than k characters left, reverse all of them. If there are less than 2k
# but greater than or equal to k characters, then reverse the first k
# characters and left the other as original.
# 
# 
# Example:
#             ba  fe 
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
#          
# 
# 
# Restrictions: 
# 
# ⁠The string consists of lower English letters only.
# ⁠Length of the given string and k will in the range [1, 10000]
# 
#
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        n = len(s)
        for i in range(0, n, 2*k):
            print(i)
            if i+k <= n: 
                s[i:i+k] = s[i:i+k][::-1]
            else:
                s[i:n] = s[i:n][::-1]
        return "".join(s)

# S = Solution()
# s = "abcdefg"
# k = 2
# print(S.reverseStr(s, k))