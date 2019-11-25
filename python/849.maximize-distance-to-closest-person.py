#
# @lc app=leetcode id=849 lang=python3
#
# [849] Maximize Distance to Closest Person
#
# https://leetcode.com/problems/maximize-distance-to-closest-person/description/
#
# algorithms
# Easy (40.96%)
# Total Accepted:    34.9K
# Total Submissions: 85.1K
# Testcase Example:  '[1,0,0,0,1,0,1]'
#
# In a row of seats, 1 represents a person sitting in that seat, and 0
# represents that the seat is empty. 
# 
# There is at least one empty seat, and at least one person sitting.
# 
# Alex wants to sit in the seat such that the distance between him and the
# closest person to him is maximized. 
# 
# Return that maximum distance to closest person.
# 
# 
# Example 1:
# 
# 
# Input: [1,0,0,0,1,0,1]
# Output: 2
# Explanation: 
# If Alex sits in the second open seat (seats[2]), then the closest person has
# distance 2.
# If Alex sits in any other open seat, the closest person has distance 1.
# Thus, the maximum distance to the closest person is 2.
# 
# 
# Example 2:
# 
# 
# Input: [1,0,0,0]
# Output: 3
# Explanation: 
# If Alex sits in the last seat, the closest person is 3 seats away.
# This is the maximum distance possible, so the answer is 3.
# 
# 
# Note:
# 
# 
# 1 <= seats.length <= 20000
# seats contains only 0s or 1s, at least one 0, and at least one 1.
# 
# 
# 
# 
#
class Solution:
    # def maxDistToClosest(self, seats: List[int]) -> int:
    def maxDistToClosest(self, seats):
        md = 1
        n = len(seats)
        def getLeft(i):
            if i == 0:
                return 0
            d = 1
            while i - 1 >= 0 and seats[i-1] == 0:
                d += 1
                i -= 1
            return d
        def getRight(i):
            if i == n-1:
                return 0
            d = 1
            while i+1 < n and seats[i+1] == 0:
                d += 1
                i += 1
            return d
        for i in range(n):
            if seats[i] == 0:
                left = getLeft(i)
                right = getRight(i)
                if left == 0:
                    mlr = right
                elif right == 0:
                    mlr = left
                else:
                    mlr = min(left, right)
                # print('i=', i, left, right, mlr)
                if mlr > md:
                    md = mlr
        return md
# s = Solution()
# seats = [1,0,0,0,1,0,1]
# print(s.maxDistToClosest(seats))
# seats = [1,0,0,0]
# print(s.maxDistToClosest(seats))