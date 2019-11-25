#
# @lc app=leetcode id=375 lang=python3
#
# [375] Guess Number Higher or Lower II
#
# https://leetcode.com/problems/guess-number-higher-or-lower-ii/description/
#
# algorithms
# Medium (38.45%)
# Total Accepted:    48.2K
# Total Submissions: 125.2K
# Testcase Example:  '1'
#
# We are playing the Guess Game. The game is as follows:
# 
# I pick a number from 1 to n. You have to guess which number I picked.
# 
# Every time you guess wrong, I'll tell you whether the number I picked is
# higher or lower.
# 
# However, when you guess a particular number x, and you guess wrong, you pay
# $x. You win the game when you guess the number I picked.
# 
# Example:
# 
# 
# n = 10, I pick 8.
# 
# First round:  You guess 5, I tell you that it's higher. You pay $5.
# Second round: You guess 7, I tell you that it's higher. You pay $7.
# Third round:  You guess 9, I tell you that it's lower. You pay $9.
# 
# Game over. 8 is the number I picked.
# 
# You end up paying $5 + $7 + $9 = $21.
# 
# 
# Given a particular n ≥ 1, find out how much money you need to have to
# guarantee a win.
#
# from math import ceil, log
from functools import lru_cache
class Solution:
    def getMoneyAmount(self, n: int) -> int:
        @lru_cache(maxsize=None) 
        def cost(arr):
            l = len(arr)
            if not l: return 0
            if l == 1: return 0
            if l == 2: return arr[0]
            if l == 3: return arr[1]
            minimum = float('inf')
            for i in range(len(arr)-2, -1, -2):
                left, right = cost(arr[:i]), cost(arr[i+1:])
                minimum = min(minimum, max(left + arr[i], arr[i] + right))
            return minimum
        return cost(tuple(range(1, n+1)))

#   *
# 1 2 3
# *   *
# 1 2 3 4   multiple of 4
#   *   *  
# 1 2 3 4 5
#     *   *
# 1 2 3 4 5 6
#       *   * 
# 1 2 3 4 5 6 7
# *   *   *   *
# 1 2 3 4 5 6 7 8 (16) multiple of 4
#       *   *   *  
# 1 2 3 4 5 6 7 8 9
# s = Solution()
# n = 1
# print(s.getMoneyAmount(n) == 0)
# n = 2
# print(s.getMoneyAmount(n))
# n = 3
# print(s.getMoneyAmount(n) == 2)
# n = 4
# print(s.getMoneyAmount(n) == 4)
# n = 5
# print(s.getMoneyAmount(n) == 6)
# n = 6
# print(s.getMoneyAmount(n) == 8)
# n = 7
# print(s.getMoneyAmount(n) == 10)
# n = 8
# print(s.getMoneyAmount(n) == 12)
# n = 9
# print(s.getMoneyAmount(n) == 14)
# n = 30
# print(s.getMoneyAmount(n))

# for i in range(21):
#     print(s.getMoneyAmount(i))