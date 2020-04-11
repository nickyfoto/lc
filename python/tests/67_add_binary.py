#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (38.72%)
# Total Accepted:    301.4K
# Total Submissions: 771.7K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
# 
# The input strings are both non-empty and contains only characters 1 or 0.
# 
# Example 1:
# 
# 
# Input: a = "11", b = "1"
# Output: "100"
# 
# Example 2:
# 
# 
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
#
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = 1
        res = []
        al, bl = len(a), len(b)
        if al >= bl:
            longer = a
        else:
            longer = b
        l = max(len(a), len(b))
        shorter = min(len(a), len(b))
        def recur(a, b, i, carry=""):
            # print('a=', a, 'b=', b, 'i=', i, 'carry=', carry)
            if shorter < i and i <= l:
                if not carry:
                    # print('here6', longer[:i-1])
                    return longer[:-(i-1)] + "".join(res)
                else:
                    if longer[-i] == '1':
                        res.insert(0, '0')
                        # print('here', 'i=', i, res)
                        return recur(a, b, i+1, '1')
                    elif longer[-i] == '0':
                        res.insert(0, '1')
                        # print('here2', 'i=', i, res)
                        return recur(a, b, i+1)
            if i > l:   
                if carry:
                    # print('i=', i)
                    return "1" + "".join(res)
                else:
                    return "".join(res)
            if a[-i] == '0' and b[-i] == '0':
                if not carry:
                    res.insert(0, '0')
                    return recur(a, b, i+1)
                else:
                    res.insert(0, '1')
                    return recur(a, b, i+1)
            elif a[-i] == '1' and b[-i] == '0' or  a[-i] == '0' and b[-i] == '1':
                if not carry:
                    res.insert(0, '1')
                    return recur(a, b, i+1)
                else:
                    res.insert(0, '0')
                    return recur(a, b, i+1, '1')
            elif a[-i] == '1' and b[-i] == '1':
                if not carry:
                    res.insert(0, '0')
                    # print(res)
                    return recur(a, b, i+1, "1")
                else:
                    res.insert(0, '1')
                    return recur(a, b, i+1, "1")
        

        return recur(a, b, 1)        



    def addBinary(self, a, b):
        x, y = int(a, 2), int(b, 2)
        while y:
            # print(x & y, (x & y) << 1)
            x, y = x ^ y, (x & y) << 1
        return bin(x)[2:]