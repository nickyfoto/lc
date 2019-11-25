#
# @lc app=leetcode id=647 lang=python3
#
# [647] Palindromic Substrings
#
# https://leetcode.com/problems/palindromic-substrings/description/
#
# algorithms
# Medium (57.73%)
# Total Accepted:    116.1K
# Total Submissions: 200.9K
# Testcase Example:  '"abc"'
#
# Given a string, your task is to count how many palindromic substrings in this
# string.
# 
# The substrings with different start indexes or end indexes are counted as
# different substrings even they consist of same characters.
# 
# Example 1:
# 
# 
# Input: "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
# 
# 
# 
# 
# Note:
# 
# 
# The input string length won't exceed 1000.
# 
# 
# 
# 
#
class Solution:
    def countSubstrings2(self, s: str) -> int:
        n = len(s)
        res = 0
        res += n

        def isPalindromic(s, k):
            for i in range(k//2):
                # print(s[i], s[-(i+1)])
                if s[i] != s[-(i+1)]:
                    return False
            return True

        # print(isPalindromic('ttgt', 4))

        for k in range(2, n+1):
            for i in range(n - k+1):
                # print(i, i+k)
                if isPalindromic(s[i:i+k], k):
                    # print(s[i:i+k])
                    res += 1
        return res

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        self.res = 0

        def check(i, r):
            if not r:
                self.res += 1
                if i > 0 and i < n-1:
                    check(i, r+1)
            else:
                # print('i=', i)
                left, right = i - r, i + r
                if left >= 0 and right <= n-1:
                    # print(left, right)
                    if s[left] == s[right]:
                        self.res += 1
                        check(i, r+1)

        for i in range(n):
            check(i, r=0)
        # print(self.res)
        def doubleCheck(left, right, r):
            # print(left, right, 'r=', r)
            if not r:
                if s[left] == s[right]:
                    self.res += 1
                    if left != 0 and right != n-1:
                        doubleCheck(left, right, r+1)
            else:
                # print('before', left, right, 'r=', r)
                left, right = left - r, right + r
                # print(left, right)
                if left >= 0 and right <= n-1:
                    # print(left, right)
                    if s[left] == s[right]:
                        self.res += 1
                        doubleCheck(left, right, r)

        for i in range(n-1):
            # print(i,i+1)
            doubleCheck(i, i+1, 0)
        return self.res

S = Solution()
# s = "aaaaaa"
# print(S.countSubstrings(s))

# s = "abcabc"
# print(S.countSubstrings(s))


# s = "dnncbwoneinoplypwgbwktmvkoimcooyiwirgbxlcttgteqthcvyoueyftiwgwwxvxvg"
# print(S.countSubstrings(s)) #exp 77 


# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# print(S.countSubstrings(s)) #exp 500500
