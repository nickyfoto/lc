#
# @lc app=leetcode id=447 lang=python3
#
# [447] Number of Boomerangs
#
# https://leetcode.com/problems/number-of-boomerangs/description/
#
# algorithms
# Easy (49.96%)
# Total Accepted:    56K
# Total Submissions: 111.7K
# Testcase Example:  '[[0,0],[1,0],[2,0]]'
#
# Given n points in the plane that are all pairwise distinct, a "boomerang" is
# a tuple of points (i, j, k) such that the distance between i and j equals the
# distance between i and k (the order of the tuple matters).
# 
# Find the number of boomerangs. You may assume that n will be at most 500 and
# coordinates of points are all in the range [-10000, 10000] (inclusive).
# 
# Example:
# 
# 
# Input:
# [[0,0],[1,0],[2,0]]
# 
# Output:
# 2
# 
# Explanation:
# The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
# 
# 
# 
# 
#
import operator as op
from functools import reduce
class Solution:
    # def numberOfBoomerangs(self, points: List[List[int]]) -> int:


    def ncr(self, n, r):
        r = min(r, n-r)
        numer = reduce(op.mul, range(n, n-r, -1), 1)
        denom = reduce(op.mul, range(1, r+1), 1)
        return numer // denom

    def numberOfBoomerangs(self, points):
        n = len(points)
        res = 0
        for i in range(n):
            others = points[:i] + points[i+1:]
            l = list(map(lambda x: (x[0] - points[i][0])**2 + (x[1] - points[i][1])**2, others))
            d = {}
            for i in l:
                if i not in d:
                    d[i] = 1
                else:
                    d[i] += 1
            # print(d)
            for k, v in d.items():
                if v > 1:
                    res += self.ncr(v, 2) * 2
        return res


# s = Solution()
# points = [[0,0],[1,0],[2,0]]
# print(s.numberOfBoomerangs(points))


# print(ncr(4,2))