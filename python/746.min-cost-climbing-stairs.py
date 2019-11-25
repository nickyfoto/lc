#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#
# https://leetcode.com/problems/min-cost-climbing-stairs/description/
#
# algorithms
# Easy (46.84%)
# Total Accepted:    78.5K
# Total Submissions: 167K
# Testcase Example:  '[0,0,0,0]'
#
# 
# On a staircase, the i-th step has some non-negative cost cost[i] assigned (0
# indexed).
# 
# Once you pay the cost, you can either climb one or two steps. You need to
# find minimum cost to reach the top of the floor, and you can either start
# from the step with index 0, or the step with index 1.
# 
# 
# Example 1:
# 
# Input: cost = [10, 15, 20]
# Output: 15
# Explanation: Cheapest is start on cost[1], pay that cost and go to the
# top.
# 
# 
# 
# Example 2:
# 
# Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output: 6
# Explanation: Cheapest is start on cost[0], and only step on 1s, skipping
# cost[3].
# 
# 
# 
# Note:
# 
# cost will have a length in the range [2, 1000].
# Every cost[i] will be an integer in the range [0, 999].
# 
# 
#
class Solution:
    # def minCostClimbingStairs(self, cost: List[int]) -> int:
    def minCostClimbingStairs(self, cost, debug=False):
        if len(cost) == 0:
            return 0
        if len(cost) < 3:
            return min(cost)
        cost.insert(0, 0)
        cost.append(0)
        # print(cost)
        n = len(cost)
        L = [0] * n
        L[1] = cost[1]
        for i in range(2, n):
            L[i] = cost[i] + min([L[i-2], L[i-1]])
        # print(L)
        return L[-1]

# s = Solution()
# a = [10, 15, 20]
# print(s.minCostClimbingStairs(a) == 15)
# a = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# print(s.minCostClimbingStairs(a) == 6)
# a = [0,0,0,1]
# print(s.minCostClimbingStairs(a) == 0)
# a = [1,0,2,2]
# print(s.minCostClimbingStairs(a) == 2)
# a = [1,1,3,2]
# print(s.minCostClimbingStairs(a) == 3)
# a = [2,1,3,3]
# print(s.minCostClimbingStairs(a) == 4)
# a = [0,0,1,2]
# print(s.minCostClimbingStairs(a) == 1)
# a = [2,1,0,2]
# print(s.minCostClimbingStairs(a) == 1)










