#
# @lc app=leetcode id=1016 lang=python3
#
# [1016] Binary String With Substrings Representing 1 To N
#
# https://leetcode.com/problems/binary-string-with-substrings-representing-1-to-n/description/
#
# algorithms
# Medium (58.90%)
# Total Accepted:    8.6K
# Total Submissions: 14.5K
# Testcase Example:  '"0110"\n3'
#
# Given a binary string S (a string consisting only of '0' and '1's) and a
# positive integer N, return true if and only if for every integer X from 1 to
# N, the binary representation of X is a substring of S.
# 
# 
# 
# Example 1:
# 
# 
# Input: S = "0110", N = 3
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: S = "0110", N = 4
# Output: false
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= S.length <= 1000
# 1 <= N <= 10^9
# 
# 
#
class Solution:
    def queryString(self, S: str, N: int) -> bool:
        
        for i in range(1, N+1):
            # print(bin(i))
            if bin(i)[2:] not in S:
                return False
        return True

# s = Solution()
# S = "0110"
# N = 3
# print(s.queryString(S, N))















