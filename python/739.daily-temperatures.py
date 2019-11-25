#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
# https://leetcode.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (60.04%)
# Total Accepted:    76.7K
# Total Submissions: 127.4K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# 
# Given a list of daily temperatures T, return a list such that, for each day
# in the input, tells you how many days you would have to wait until a warmer
# temperature.  If there is no future day for which this is possible, put 0
# instead.
# 
# For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76,
# 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
# 
# 
# Note:
# The length of temperatures will be in the range [1, 30000].
# Each temperature will be an integer in the range [30, 100].
# 
#

# naive approach
# def dailyTemperatures(self, T):
#     n = len(T)
#     res = [0]*n
#     for i in range(n):
#         for j in range(i+1, n):
#             if T[j] > T[i]:
#                 res[i] = j-i
#                 break
#     return res

from collections import Counter
from functools import reduce
class Solution:
    # def dailyTemperatures(self, T: List[int]) -> List[int]:

    def dailyTemperatures3(self, T):
        ans = [0] * len(T)
        stack = [] #indexes from hottest to coldest
        for i in range(len(T) - 1, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                print('update i=', i, 'stack=', stack)
                ans[i] = stack[-1] - i
            stack.append(i)
            print('i=', i, 'stack=', stack)
        return ans

    def dailyTemperatures2(self, T):
        n = len(T)
        res = [0]*n
        for i in range(n):
            for j in range(i+1, n):
                if T[j] > T[i]:
                    res[i] = j-i
                    break
        return res

    def dailyTemperatures(self, T):
        c = Counter(T)
        # print(c)
        s = sorted([[k, v] for k, v in c.items()])
        # print(s)
        for i in range(1, len(s)):
            # print(i)
            # print(s[i])
            s[i][1] += s[i-1][1]
        # print(s)
        percentile = dict(s)
        # print(percentile)
        n = len(T)
        res = [0] * n
        
        def method1(i):
            for j in range(i+1, n):
                if T[j] > T[i]:
                    return j - i
            return 0
        d = {}
        for i in range(n):
            if T[i] not in d:
                d[T[i]] = [i]
            else:
                d[T[i]].append(i)
        # print(d)
        order = [x[0] for x in s]
        # print(order)
        def method2(i):
            min_ = float('inf')
            for j in range(order.index(T[i])+1, len(s)):
                # print('here')
                for idx in d[order[j]]:
                    if idx > i:
                        if idx < min_:
                            min_ = idx
            if min_ < float('inf'):
                return min_ - i
            else:
                return 0
        cut = int(n*0.9)
        for i in range(n):
            if percentile[T[i]] < cut:
                res[i] = method1(i)
            else:
                res[i] = method2(i)
        return res
s = Solution()
T = [73, 74, 75, 71, 69, 72, 76, 73]
print(s.dailyTemperatures3(T))
# print(s.dailyTemperatures(T) == s.dailyTemperatures2(T))
# T = [34,80,80,34,34,80,80,80,80,34]

# print(s.dailyTemperatures(T))




# print(s.dailyTemperatures(T) == s.dailyTemperatures2(T))
















