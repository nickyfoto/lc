#
# @lc app=leetcode id=1017 lang=python3
#
# [1017] Convert to Base -2
#
# https://leetcode.com/problems/convert-to-base-2/description/
#
# algorithms
# Medium (57.03%)
# Total Accepted:    7K
# Total Submissions: 12.3K
# Testcase Example:  '2'
#
# Given a number N, return a string consisting of "0"s and "1"s that represents
# its value in base -2 (negative two).
# 
# The returned string must have no leading zeroes, unless the string is
# "0".
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: 2
# Output: "110"
# Explantion: (-2) ^ 2 + (-2) ^ 1 = 2
#     
#     
#     
# Example 2:
# 
# 
# Input: 3
# Output: "111"
# Explantion: (-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3
# 
# 
# 
# Example 3:
# 
# 
# Input: 4
# Output: "100"
# Explantion: (-2) ^ 2 = 4
#            0   1  2   3  4    5   6
# availabie, 1, -2, 4, -8, 16, -32 64
# 
# 1 => 1      =>                 1
# 2 => 4 - 2 =>                110
# 3 => 4 - 2 + 1 =>            111
# 4 => (-2)^2 =>               100
# 5 => 4 + 1 =>                101
# 6 => 16 - 8 - 2 =>         11010
# 7 => 16 - 8 - 2 + 1 =>     11011
# 8 => 16 - 8 =>             11000
# 9 => 16 - 8 + 1 =>         11001
# 10 => 16 - 8 + 4 - 2 =>    11110
# 11 => 16 - 8 + 4 - 2 + 1 =>11111
# 12 => 16 - 8 + 4 =>        11100
# 13 => 16 - 8 + 4 + 1 =>    11101 
# 14 => 16 - 2         =>    10010
# 15                         10011
# 16                         10000
# 17                         10001
# Note:                      10 
# Note:                      10 
# Note:                      10 
# Note:                      10 
#                             
# 
# 0 <= N <= 10^9
# 
# 
# 
# 
#
class Solution:
    def baseNeg2(self, N: int) -> str:
        res = []
        x = N
        while x:
            res.append(x & 1)
            x = -(x >> 1)
        return "".join(map(str, res[::-1] or [0]))

# s = Solution()
# print(s.baseNeg2(11))



        
