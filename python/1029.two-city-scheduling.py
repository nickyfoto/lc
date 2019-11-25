#
# @lc app=leetcode id=1029 lang=python3
#
# [1029] Two City Scheduling
#
# https://leetcode.com/problems/two-city-scheduling/description/
#
# algorithms
# Easy (52.49%)
# Total Accepted:    8K
# Total Submissions: 14.8K
# Testcase Example:  '[[10,20],[30,200],[400,50],[30,20]]'
#
# There are 2N people a company is planning to interview. The cost of flying
# the i-th person to city A is costs[i][0], and the cost of flying the i-th
# person to city B is costs[i][1].
# 
# Return the minimum cost to fly every person to a city such that exactly N
# people arrive in each city.
# 
# 
# 
# Example 1:
# 
# 
# Input: [[10,20],[30,200],[400,50],[30,20]]
# Output: 110
# Explanation: 
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.
# 
# The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people
# interviewing in each city.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= costs.length <= 100
# It is guaranteed that costs.length is even.
# 1 <= costs[i][0], costs[i][1] <= 1000
# 
#
class Solution:
    # def twoCitySchedCost(self, costs: List[List[int]]) -> int:
    def twoCitySchedCost(self, costs):
        N = len(costs) // 2
        # diff = [abs(c[0]-c[1]) for c in costs]
        # print(diff)
        costs = sorted(costs, key=lambda c: abs(c[0]-c[1]), reverse=True)
        # print(costs)
        A = []
        B = []
        for c in costs:
            if c[0] > c[1]:
                if len(B) < N:
                    B.append(c[1])
                else:
                    if len(A) < N:
                        A.append(c[0])
            else:
                if len(A) < N:
                    A.append(c[0])
                else:
                    if len(B) < N:
                        B.append(c[1])
        # print(A, B)
        return sum(A+B)
# s = Solution()
# costs = [[10,20],[30,200],[400,50],[30,20]]
# print(s.twoCitySchedCost(costs))
# costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]

# # print(259+184+577+54+667+118)

# print(s.twoCitySchedCost(costs))
# print([x[1] for x in a])

# ✘ 7/49 cases passed (N/A)
# ✘ testcase: '[[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]'
# ✘ answer: 1706
# ✘ expected_answer: 1859
# ✘ stdout:
