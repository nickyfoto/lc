#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (44.53%)
# Likes:    2177
# Dislikes: 169
# Total Accepted:    248.2K
# Total Submissions: 555.9K
# Testcase Example:  '12'
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
# 
# Example 1:
# 
# 
# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# 
# Example 2:
# 
# 
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#

# @lc code=start
from math import sqrt, inf
from functools import lru_cache
class Solution:
    # def numSquares(self, n: int) -> int:
    def numSquares(self, n):
        """
        recursive
        """
        square_sums = [i**2 for i in range(1, int(sqrt(n) + 1))]
        square_sums = {k:k for k in square_sums}
        
        @lru_cache(None)
        def recur(n):
            if n in square_sums:
                return 1
            mn = inf
            for square in square_sums:
                if n < square:
                    break
                mn = min(mn, recur(n - square) + 1)
            return mn
        return recur(n)

    def numSquares(self, n):
        """
        follow up question
            - how many ways N can be divided into perfect squares
            - if it is possible to divide N into k perfect squares
        """
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = min(dp[i - j * j] + 1 for j in range(1, int(sqrt(i)) + 1))
        return dp[-1]
    
    def numSquares(self, n):
        """
        greedy + bfs
        didn't understand bfs version yet
        """
        square_sums = [i * i for i in range(1, int(sqrt(n)) + 1)]
        level = 0
        q = {n}
        while q:
            level += 1
            next_queue = set()
            for remainder in q:
                for square_sum in square_sums:
                    if remainder == square_sum:
                        return level # find the node!
                    elif remainder < square_sum:
                        break
                    else:
                        next_queue.add(remainder - square_sum)
            q = next_queue
        return level

    
# @lc code=end
