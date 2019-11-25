#
# @lc app=leetcode id=319 lang=python3
#
# [319] Bulb Switcher
#
# https://leetcode.com/problems/bulb-switcher/description/
#
# algorithms
# Medium (44.22%)
# Total Accepted:    62.7K
# Total Submissions: 141.6K
# Testcase Example:  '3'
#
# There are n bulbs that are initially off. You first turn on all the bulbs.
# Then, you turn off every second bulb. On the third round, you toggle every
# third bulb (turning on if it's off or turning off if it's on). For the i-th
# round, you toggle every i bulb. For the n-th round, you only toggle the last
# bulb. Find how many bulbs are on after n rounds.
# 
# Example:
# 
# 
# Input: 3
# Output: 1 
# Explanation: 
# At first, the three bulbs are [off, off, off].
# After first round, the three bulbs are [on, on, on].
# After second round, the three bulbs are [on, off, on].
# After third round, the three bulbs are [on, off, off]. 
# 
# So you should return 1, because there is only one bulb is on.
# 
# 
#
from math import ceil
class Solution:
    def bulbSwitch2(self, n: int) -> int:
        if n <= 1:
            return 0
        if n == 2:
            return 1
        def recur(bulbs, n, round):
            if round == n:
                bulbs[-1] = not bulbs[-1]
                # print(bulbs)
                return len([x for x in bulbs if x])
            else:
                for i in range(round-1, n, round):
                    # print(round, 'i=', i)
                    bulbs[i] = not bulbs[i]
                # print(bulbs, round)
                return recur(bulbs, n, round+1)
            
        bulbs = [True] * n
        # print(recur(bulbs, n, 2))
        return recur(bulbs, n, 2)

    def bulbSwitch(self, n: int) -> int:
        if n < 1:
            return 0
        if n < 4:
            return 1
        i = 2
        while not (i**2 <= n and n <= i * (i+2)):
            i += 1
        return i


# s = Solution()
# print(s.bulbSwitch(3))
# print(s.bulbSwitch(0))
# print(s.bulbSwitch(99999))
# print(s.bulbSwitch(4))
# print(s.bulbSwitch(8))
# print(s.bulbSwitch(9))
# print(s.bulbSwitch(48))
# print(s.bulbSwitch(49))
# for i in range(50):
#     print('i=', i, s.bulbSwitch2(i))
    
# starting from n = 4, it has the following growth rule
# i= 4 2
# i= 5 2
# i= 6 2
# i= 7 2
# i= 8 2
# i= 9 3
# i= 10 3
# i= 11 3
# i= 12 3
# i= 13 3
# i= 14 3
# i= 15 3
# i= 16 4
# i= 17 4
# i= 18 4
# i= 19 4
# i= 20 4
# i= 21 4
# i= 22 4
# i= 23 4
# i= 24 4
# i= 25 5
# i= 26 5
# i= 27 5
# i= 28 5
# i= 29 5
# i= 30 5
# i= 31 5
# i= 32 5
# i= 33 5
# i= 34 5
# i= 35 5
# i= 36 6
# i= 37 6
# i= 38 6
# i= 39 6
# i= 40 6
# i= 41 6
# i= 42 6
# i= 43 6
# i= 44 6
# i= 45 6
# i= 46 6
# i= 47 6
# i= 48 6
