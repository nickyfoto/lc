#
# @lc app=leetcode id=1473 lang=python3
#
# [1473] Paint House III
#
# https://leetcode.com/problems/paint-house-iii/description/
#
# algorithms
# Hard (42.84%)
# Likes:    127
# Dislikes: 6
# Total Accepted:    2.9K
# Total Submissions: 6.7K
# Testcase Example:  '[0,0,0,0,0]\n[[1,10],[10,1],[10,1],[1,10],[5,1]]\n5\n2\n3'
#
# There is a row of m houses in a small city, each house must be painted with
# one of the n colors (labeled from 1 to n), some houses that has been painted
# last summer should not be painted again.
# 
# A neighborhood is a maximal group of continuous houses that are painted with
# the same color. (For example: houses = [1,2,2,3,3,2,1,1] contains 5
# neighborhoods  [{1}, {2,2}, {3,3}, {2}, {1,1}]).
# 
# Given an array houses, an m * n matrix cost and an integer target
# where:
# 
# 
# houses[i]: is the color of the house i, 0 if the house is not painted
# yet.
# cost[i][j]: is the cost of paint the house i with the color j+1.
# 
# 
# Return the minimum cost of painting all the remaining houses in such a way
# that there are exactly target neighborhoods, if not possible return -1.
# 
# 
# Example 1:
# 
# 
# Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m =
# 5, n = 2, target = 3
# Output: 9
# Explanation: Paint houses of this way [1,2,2,1,1]
# This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
# Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.
# 
# 
# Example 2:
# 
# 
# Input: houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m =
# 5, n = 2, target = 3
# Output: 11
# Explanation: Some houses are already painted, Paint the houses of this way
# [2,2,1,2,2]
# This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}]. 
# Cost of paint the first and last house (10 + 1) = 11.
# 
# 
# Example 3:
# 
# 
# Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[1,10],[10,1],[1,10]], m =
# 5, n = 2, target = 5
# Output: 5
# 
# 
# Example 4:
# 
# 
# Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n
# = 3, target = 3
# Output: -1
# Explanation: Houses are already painted with a total of 4 neighborhoods
# [{3},{1},{2},{3}] different of target = 3.
# 
# 
# 
# Constraints:
# 
# 
# m == houses.length == cost.length
# n == cost[i].length
# 1 <= m <= 100
# 1 <= n <= 20
# 1 <= target <= m
# 0 <= houses[i] <= n
# 1 <= cost[i][j] <= 10^4
# 
#

# @lc code=start
import math
from functools import lru_cache
class Solution:
    def minCost(self, houses, cost, m, n, target):
        """
        first step, all houses are zero, no target constrain
        what's the minCost
        return sum(min(c) for c in cost)

        no matter what
        for houses[m - 1], we there's some cost to paint it
        the cost can be zero, but the min accumulate cost is the result
        """
        @lru_cache(None)
        def recur(i, k, c):
            if i < 0 and k <= 1: return 0
            if k > i + 1 or k < 1: return math.inf
            if houses[i] and c != houses[i]: return math.inf
            paint_cost = cost[i][c - 1] * (not houses[i])
            prev_costs = min(recur(i - 1, k, c), min([recur(i - 1, k - 1, cc) for cc in range(1, n + 1) if cc != c] or [math.inf]))
            return paint_cost + prev_costs
        res = min(recur(m - 1, target, c) for c in range(1, n + 1))
        return res if res < math.inf else -1

# @lc code=end
