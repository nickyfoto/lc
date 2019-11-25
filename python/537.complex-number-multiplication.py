#
# @lc app=leetcode id=537 lang=python3
#
# [537] Complex Number Multiplication
#
# https://leetcode.com/problems/complex-number-multiplication/description/
#
# algorithms
# Medium (65.88%)
# Total Accepted:    38.9K
# Total Submissions: 59.1K
# Testcase Example:  '"1+1i"\n"1+1i"'
#
# 
# Given two strings representing two complex numbers.
# 
# 
# You need to return a string representing their multiplication. Note i2 = -1
# according to the definition.
# 
# 
# Example 1:
# 
# Input: "1+1i", "1+1i"
# Output: "0+2i"
# Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it
# to the form of 0+2i.
# 
# 
# 
# Example 2:
# 
# Input: "1+-1i", "1+-1i"
# Output: "0+-2i"
# Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert
# it to the form of 0+-2i.
# 
# 
# 
# Note:
# 
# The input strings will not have extra blank.
# The input strings will be given in the form of a+bi, where the integer a and
# b will both belong to the range of [-100, 100]. And the output should be also
# in this form.
# 
# 
#

class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i
        


    def __mul__(self, other):
        r = self.r * other.r - self.i * other.i
        i = self.r * other.i + self.i * other.r
        return Complex(r, i)

    __rmul__ = __mul__

    def __str__(self):
        return str(self.r)+'+'+str(self.i)+'i'



class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        def to_complex(s):
            r, i = s[:-1].split('+')
            return Complex(int(r), int(i))
        a = to_complex(a)
        b = to_complex(b)
        # print(a*b)
        return str(a*b)


# s = Solution()
# a = "1+1i"
# b = "1+1i"
# print(s.complexNumberMultiply(a, b))



# a = "1+-1i"
# b = "1+-1i"
# print(s.complexNumberMultiply(a, b))



# a = "1+-1i"
# b = "0+0i"
# print(s.complexNumberMultiply(a, b))

# a = "78+-76i"
# b = "-86+72i"
# print(s.complexNumberMultiply(a, b))
# "-1236+12152i"





        
