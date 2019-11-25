#
# @lc app=leetcode id=1071 lang=python3
#
# [1071] Greatest Common Divisor of Strings
#
# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/
#
# algorithms
# Easy (53.45%)
# Total Accepted:    7.1K
# Total Submissions: 13.2K
# Testcase Example:  '"ABCABC"\n"ABC"'
#
# For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T
# concatenated with itself 1 or more times)
# 
# Return the largest string X such that X divides str1 and X divides str2.
# 
# 
# 
# Example 1:
# 
# 
# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# 
# 
# Example 2:
# 
# 
# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# 
# 
# Example 3:
# 
# 
# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= str1.length <= 1000
# 1 <= str2.length <= 1000
# str1[i] and str2[i] are English uppercase letters.
# 
#
class Solution:
    # def gcdOfStrings(self, str1: str, str2: str) -> str:
    def gcdOfStrings(self, str1, str2):
        if str1 == str2:
            return str1
        def div(str1, str2, n1, n2):
            # print(str1)
            # print(str2)
            if n1 % n2 != 0:
                return False
            for i in range(0, n1, n2):
                if str1[i:i+n2] != str2:
                    # print('here')
                    return False
            return True


        n1 = len(str1)
        n2 = len(str2)
        if n2 == n1:
            return ""
        elif n2 < n1:
            op = str2
            op_length = len(str2)
            while op_length > 0:
                if div(str2, op, n2, op_length) and div(str1, op, n1, op_length):
                    return op
                else:
                    op = str2[:op_length-1]
                    op_length -= 1

        else:
            return self.gcdOfStrings(str2, str1)

s = Solution()
# str1 = "ABCABC"
# str2 = "ABC"
# print(s.gcdOfStrings(str1, str2))
# str1 = "ABABAB"
# str2 = "ABAB"
# print(s.gcdOfStrings(str1, str2))
# str1 = "LEET"
# str2 = "CODE"
# print(s.gcdOfStrings(str1, str2))

# str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
# str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
# s3 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"
# print(s.gcdOfStrings(str1, str2))
# print(str2 == s3)
