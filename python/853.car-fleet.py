#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#
# https://leetcode.com/problems/car-fleet/description/
#
# algorithms
# Medium (40.70%)
# Total Accepted:    18.4K
# Total Submissions: 45.1K
# Testcase Example:  '12\n[10,8,0,5,3]\n[2,4,1,1,3]'
#
# N cars are going to the same destination along a one lane road.  The
# destination is target miles away.
# 
# Each car i has a constant speed speed[i] (in miles per hour), and initial
# position position[i] miles towards the target along the road.
# 
# A car can never pass another car ahead of it, but it can catch up to it, and
# drive bumper to bumper at the same speed.
# 
# The distance between these two cars is ignored - they are assumed to have the
# same position.
# 
# A car fleet is some non-empty set of cars driving at the same position and
# same speed.  Note that a single car is also a car fleet.
# 
# If a car catches up to a car fleet right at the destination point, it will
# still be considered as one car fleet.
# 
# 
# How many car fleets will arrive at the destination?
# 
# 
# 
# Example 1:
# 
# 
# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
# Output: 3
# Explanation:
# The cars starting at 10 and 8 become a fleet, meeting each other at 12.
# The car starting at 0 doesn't catch up to any other car, so it is a fleet by
# itself.
# The cars starting at 5 and 3 become a fleet, meeting each other at 6.
# Note that no other cars meet these fleets before the destination, so the
# answer is 3.
# 
# 
# 
# Note:
# 
# 
# 0 <= N <= 10 ^ 4
# 0 < target <= 10 ^ 6
# 0 < speed[i] <= 10 ^ 6
# 0 <= position[i] < target
# All initial positions are different.
# 
#
import math
from itertools import combinations
class Solution:
    # def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    def carFleet2(self, target, position, speed) -> int:
        
        def lcm(a, b):
            return abs(a*b) // math.gcd(a, b)

        l = list(zip(position, speed))
        combinations(l, 2)

        car = []
        res = 0
        for t in range(target, -1, -1):
            for a, b in combinations(l, 2):
                # print((t-a[0])/a[1], (t-b[0])/b[1])
                if t > a[0] and t > b[0]:
                    if (t-a[0])/a[1] == (t-b[0])/b[1]:
                        # print(t, a, b, (t-a[0])/a[1])
                        res += 1
                        car += [a[0], b[0]]
        # print(res, car)
        res += len(set(position) - set(car))
        # print(res)
        return res

    def carFleet1(self, target, position, speed) -> int:

        n = len(position)
        ps = list(zip(position, speed))
        ps.sort()
        print(ps)
        while ps[0][0] < target:
            ps = [(p+s,s) for p, s in ps]
            print('before', ps)
            i = 1
            while i < n:
                while ps[i-1][0] >= ps[i][0] and ps[i][0] <= target:
                    ps.remove(ps[i-1])
                    n -= 1
                    i -= 1
                    # print('i=', i, ps)
                    if i == 0:
                        break
                i += 1
            print('after=', ps)

        return n


    def carFleet(self, target, position, speed) -> int:

        n = len(position)
        if not n:
            return 0
        ps = list(zip(position, speed))
        ps.sort()
        # distance = [target - p for p in position]
        # print(distance)
        t = [(target-p)/s for p,s in ps]
        # res = 0
        i = 1
        while i < n:
            while t[i] >= t[i-1]:
                t.remove(t[i-1])
                n -= 1
                i -= 1
                # print('i=', i, ps)
                if i == 0:
                    break
            i += 1
        # print(res)
        return n
s = Solution()
target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
print(s.carFleet(target, position, speed) == 3)




target = 10
position = [0,4,2]
speed = [2,1,3]
print(s.carFleet(target, position, speed) == 1)


target = 10
position = [6,8]
speed = [3,2]
print(s.carFleet(target, position, speed) == 2)

target = 20
position = [6,2,17]
speed = [3,9,2]
print(s.carFleet(target, position, speed) == 2)



target = 16
position = [11,14,13,6]
speed = [2,2,6,7]
print(s.carFleet(target, position, speed) == 2)




target = 13
position = [10,2,5,7,4,6,11]
speed = [7,5,10,5,9,4,1]
print(s.carFleet(target, position, speed) == 2)

target = 21
position = [1,15,6,8,18,14,16,2,19,17,3,20,5]
speed = [8,5,5,7,10,10,7,9,3,4,4,10,2]
# print(s.carFleet(target, position, speed))
print(s.carFleet(target, position, speed) == 7)


