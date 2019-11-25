#
# @lc app=leetcode id=1010 lang=python3
#
# [1010] Pairs of Songs With Total Durations Divisible by 60
#
# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/description/
#
# algorithms
# Easy (45.61%)
# Total Accepted:    13.1K
# Total Submissions: 28.6K
# Testcase Example:  '[30,20,150,100,40]'
#
# In a list of songs, the i-th song has a duration of time[i] seconds. 
# 
# Return the number of pairs of songs for which their total duration in seconds
# is divisible by 60.  Formally, we want the number of indices i < j with
# (time[i] + time[j]) % 60 == 0.
# 
# 
# 
# Example 1:
# 
# 
# Input: [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60
# 
# 
# 
# Example 2:
# 
# 
# Input: [60,60,60]
# Output: 3
# Explanation: All three pairs have a total duration of 120, which is divisible
# by 60.
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= time.length <= 60000
# 1 <= time[i] <= 500
# 
#
from collections import Counter
class Solution:
    # def numPairsDivisibleBy60(self, time: List[int]) -> int:
    def numPairsDivisibleBy60(self, time):
        # res = 0
        # n = len(time)
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         if (time[i]+time[j]) % 60 == 0:
        #             res += 1
        # return res
        c = Counter()
        res = 0
        for t in time:
            # print('t=',t, '-t % 60=', -t % 60, 't % 60', t % 60, c)
            res += c[-t % 60]
            c[t % 60] += 1
        return res

# s = Solution()
# time = [30,20,150,100,40]
# print(s.numPairsDivisibleBy60(time))
# time = [60,60,60]
# print(s.numPairsDivisibleBy60(time))
