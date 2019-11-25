#
# @lc app=leetcode id=983 lang=python3
#
# [983] Minimum Cost For Tickets
#
# https://leetcode.com/problems/minimum-cost-for-tickets/description/
#
# algorithms
# Medium (57.74%)
# Total Accepted:    21.3K
# Total Submissions: 36.9K
# Testcase Example:  '[1,4,6,7,8,20]\n[2,7,15]'
#
# In a country popular for train travel, you have planned some train travelling
# one year in advance.  The days of the year that you will travel is given as
# an array days.  Each day is an integer from 1 to 365.
# 
# Train tickets are sold in 3 different ways:
# 
# 
# a 1-day pass is sold for costs[0] dollars;
# a 7-day pass is sold for costs[1] dollars;
# a 30-day pass is sold for costs[2] dollars.
# 
# 
# The passes allow that many days of consecutive travel.  For example, if we
# get a 7-day pass on day 2, then we can travel for 7 days: day 2, 3, 4, 5, 6,
# 7, and 8.
# 
# Return the minimum number of dollars you need to travel every day in the
# given list of days.
# 
# 
# 
# Example 1:
# 
# 
# Input: days = [1,4,6,7,8,20], costs = [2,7,15]
# Output: 11
# Explanation: 
# For example, here is one way to buy passes that lets you travel your travel
# plan:
# On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
# On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4,
# ..., 9.
# On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
# In total you spent $11 and covered all the days of your travel.
# 
# 
# 
# Example 2:
# 
# 
# Input: days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
# Output: 17
# Explanation: 
# For example, here is one way to buy passes that lets you travel your travel
# plan:
# On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1,
# 2, ..., 30.
# On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
# In total you spent $17 and covered all the days of your travel.
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= days.length <= 365
# 1 <= days[i] <= 365
# days is in strictly increasing order.
# costs.length == 3
# 1 <= costs[i] <= 1000
# 
# 
#

class Ticket:
    def __init__(self, cost, coverage):
        self.cost = cost    
        self.coverage = coverage

    def __str__(self):
        return str({'cost': self.cost, 'coverage': self.coverage})


from functools import lru_cache


class Solution:
    # def mincostTickets(self, days: List[int], costs: List[int]) -> int:
    def mincostTickets1(self, days, costs) -> int:
        n = len(days)
        
        def mark_ticket(t, day, costs_idx):
            if costs_idx == 0:
                t[day] = Ticket(costs[0], 1)
            elif costs_idx == 1:
                t[day] = Ticket(costs[1], 7)
            else:
                t[day] = Ticket(costs[2], 30)

            return t

        def covered(t, i):
            if i == 0:
                return False
            if t[i-1].coverage == 1:
                return False
            else:
                if days[i] - days[i-1] < t[i-1].coverage:
                    return True
                else:
                    return False

        def recur(t,i):
            if not covered(t, i):
                t1  = mark_ticket(t=t.copy(), day=i, costs_idx=0)
                t7  = mark_ticket(t=t.copy(), day=i, costs_idx=1)
                t30 = mark_ticket(t=t.copy(), day=i, costs_idx=2)
                if i != n - 1:
                    r1 = recur(t1,i+1)
                    r7 = recur(t7,i+1)
                    r30 = recur(t30,i+1)
                    return min(t1[i].cost + r1, t7[i].cost + r7, t30[i].cost + r30)
                else:
                    return min(costs)
            else:
                ticket = Ticket(0, t[i-1].coverage - (days[i] - days[i-1]))
                t[i] = ticket
                if i != n - 1:
                    return recur(t, i+1)
                else:
                    return 0
        
        return recur(t=[None] * n, i=0)


    def mincostTickets(self, days, costs):
        dayset = set(days)
        durations = [1, 7, 30]

        @lru_cache(None)
        def dp(i):
            if i > 365:
                return 0
            elif i in dayset:
                return min(dp(i + d) + c
                           for c, d in zip(costs, durations))
            else:
                return dp(i + 1)

        return dp(1)



# s = Solution()
# days = [1,4,6,7,8,20]
# # days = [1,4,6,7,8]
# costs = [2,7,15]
# print(s.mincostTickets(days, costs))


# days = [1,2,3,4,5,6,7,8,9,10,30,31]
# costs = [2,7,15]
# print(s.mincostTickets(days, costs))



# days = [1,4,6,7,8,20]
# costs = [7,2,15]
# print(s.mincostTickets(days, costs)) # 6



# days = [1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,24,25,27,28,29,30,31,34,37,38,39,41,43,44,45,47,48,49,54,57,60,62,63,66,69,70,72,74,76,78,80,81,82,83,84,85,88,89,91,93,94,97,99]
# costs = [9,38,134]
# print(s.mincostTickets(days, costs)) # time limit exceeded








        
