#
# @lc app=leetcode id=812 lang=python3
#
# [812] Largest Triangle Area
#
# https://leetcode.com/problems/largest-triangle-area/description/
#
# algorithms
# Easy (55.55%)
# Total Accepted:    14.1K
# Total Submissions: 25.3K
# Testcase Example:  '[[0,0],[0,1],[1,0],[0,2],[2,0]]'
#
# You have a list of points in the plane. Return the area of the largest
# triangle that can be formed by any 3 of the points.
# 
# 
# Example:
# Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# Output: 2
# Explanation: 
# The five points are show in the figure below. The red triangle is the
# largest.
# 
# 
# 
# 
# Notes: 
# 
# 
# 3 <= points.length <= 50.
# No points will be duplicated.
# -50 <= points[i][j] <= 50.
# Answers within 10^-6 of the true value will be accepted as correct.
# 
# 
# 
# 
#
class Solution:
    # def largestTriangleArea(self, points: List[List[int]]) -> float:
    def getVertialPoints(self, points):
        n = len(points)
        max_x = points[-1][0]
        # print(max_x)
        vertial_points = [[]] * (max_x+1)
        for x in range(max_x+1):
            l = [p for p in points if p[0] == x]
            vertial_points[x] = l
        return vertial_points
    def largestTriangleArea(self, points):
        points.sort()
        # print(points)
        vertial_points = self.getVertialPoints(points)
        print(vertial_points)

s = Solution()
points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
s.largestTriangleArea(points)

