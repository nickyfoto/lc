#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#
# https://leetcode.com/problems/add-strings/description/
#
# algorithms
# Easy (43.77%)
# Total Accepted:    103.1K
# Total Submissions: 233.9K
# Testcase Example:  '"0"\n"0"'
#
# Given two non-negative integers num1 and num2 represented as string, return
# the sum of num1 and num2.
# 
# Note:
# 
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
# 
# 
#
import string
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = []
        # print(string.digits)
        d = dict(zip(list(string.digits), [int(i) for i in string.digits]))
        # print(d)
        def add(d1, d2, idx, extra):
            s = d[d1[-idx]] + d[d2[-idx]] + extra
            s = str(s)
            if len(s) == 1:
                res.insert(0, s)
                if idx < len(d1):
                    add(d1, d2, idx+1, 0)
            else:
                res.insert(0, s[-1])
                if idx < len(d1):
                    add(d1, d2, idx+1, 1)
            # res.insert(s[])
        l1 = len(num1)
        l2 = len(num2)
        if l1 >= l2:
            num1 = "0" + num1
            num2 = "0" * (len(num1) - l2) + num2
            # for i in range(1, len(l1)+1):
            add(num1, num2, 1, 0)
            if len(res) > 1 and res[0] == '0':
                res = res[1:]
            return "".join(res)
            # return "".join()
            # print(res)
            # final_res = 0
            # for i in range(len(res)):
            #     final_res += d[res[-(i+1)]]*10**i
            # # print(final_res)
            # return final_res
        else:
            return self.addStrings(num2, num1)


# s = Solution()
# num1 = "999"
# num2 = "1"
# print(s.addStrings(num1, num2))
# num1 = "0"
# num2 = "0"
# print(s.addStrings(num1, num2))