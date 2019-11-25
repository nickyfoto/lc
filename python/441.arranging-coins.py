#
# @lc app=leetcode id=441 lang=python3
#
# [441] Arranging Coins
#
# https://leetcode.com/problems/arranging-coins/description/
#
# algorithms
# Easy (37.77%)
# Total Accepted:    68.7K
# Total Submissions: 181.3K
# Testcase Example:  '5'
#
# You have a total of n coins that you want to form in a staircase shape, where
# every k-th row must have exactly k coins.
# ⁠
# Given n, find the total number of full staircase rows that can be formed.
# 
# n is a non-negative integer and fits within the range of a 32-bit signed
# integer.
# 
# Example 1:
# 
# n = 5
# 
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤
# 
# Because the 3rd row is incomplete, we return 2.
# 
# 
# 
# Example 2:
# 
# n = 8
# 
# The coins can form the following rows:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
# 
# Because the 4th row is incomplete, we return 3.
# 
# 
#
class Solution:
    # def arrangeCoins(self, n: int) -> int:
    def arrangeCoins(self, n):
        if n == 0:
            return 0
        i = 1
        total = 1
        while n - total > i:
            i += 1
            total += i
        return i

# s = Solution()
# n = 5
# print(s.arrangeCoins(n))
# n = 8
# print(s.arrangeCoins(n))




