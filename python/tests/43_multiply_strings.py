#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#
# https://leetcode.com/problems/multiply-strings/description/
#
# algorithms
# Medium (32.49%)
# Likes:    1414
# Dislikes: 653
# Total Accepted:    253.4K
# Total Submissions: 779.3K
# Testcase Example:  '"2"\n"3"'
#
# Given two non-negative integers num1 and num2 represented as strings, return
# the product of num1 and num2, also represented as a string.
# 
# Example 1:
# 
# 
# Input: num1 = "2", num2 = "3"
# Output: "6"
# 
# Example 2:
# 
# 
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# 
# 
# Note:
# 
# 
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contain only digits 0-9.
# Both num1 and num2 do not contain any leading zero, except the number 0
# itself.
# You must not use any built-in BigInteger library or convert the inputs to
# integer directly.
# 
# 
#

# @lc code=start
class Solution:
    # def multiply(self, num1: str, num2: str) -> str:
    def multiply(self, num1, num2):
        m = len(num1)
        n = len(num2)
        pos = [0] * (m + n)
        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
                mul = int(num1[i]) * int(num2[j])
                p1 = i + j
                p2 = p1 + 1
                sm = mul + pos[p2]
                q, r = divmod(sm, 10)
                pos[p1] += q
                pos[p2] = r
        
        # print(pos)
        r = "".join(map(str, pos)).lstrip('0')
        if not r:
            return "0"
        return r
# @lc code=end
