#
# @lc app=leetcode id=939 lang=python3
#
# [939] Minimum Area Rectangle
#
# https://leetcode.com/problems/minimum-area-rectangle/description/
#
# algorithms
# Medium (51.23%)
# Total Accepted:    25.3K
# Total Submissions: 49.3K
# Testcase Example:  '[[1,1],[1,3],[3,1],[3,3],[2,2]]'
#
# Given a set of points in the xy-plane, determine the minimum area of a
# rectangle formed from these points, with sides parallel to the x and y axes.
# 
# If there isn't any rectangle, return 0.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
# Output: 4
# 
# 
# 
# Example 2:
# 
# 
# Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# Output: 2
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= points.length <= 500
# 0 <= points[i][0] <= 40000
# 0 <= points[i][1] <= 40000
# All points are distinct.
# 
# 
# 
#
class Solution:
    # def minAreaRect(self, points: List[List[int]]) -> int:
    def minAreaRect(self, points) -> int:

        points.sort()
        n = len(points)
        print(points)

        y_axis_indices = sorted(range(n), key=lambda k: points[k][1])
        print(y_axis_indices)

        class Point:
            def __init__(self, x, y, x_idx, y_idx):
                self.x = x
                self.y = y
                self.x_idx = x_idx
                self.y_idx = y_idx

            def __str__(self):
                return str(dict({'x': self.x, 'y': self.y, 'x_idx': self.x_idx, 'y_idx': self.y_idx}))

        points = [Point(p[0], p[1], x_idx, y_axis_indices[x_idx]) for x_idx, p in enumerate(points)]


        def valid_rect(low_left, high_right):
            # print(high_right.x_idx, high_right.y_idx)
            # print(low_left.x_idx, low_left.y_idx)
            print(low_left, high_right)
            for i in range(high_right.x_idx - 1, low_left.x_idx + 1, -1):
                for j in range(high_right.y_idx - 1, low_left.y_idx + 1, -1):
                    # print('here', points[i], points[j])
                    

        for i in range(n-1, -1, -1):
            for j in range(points[i].y_idx-1, -1, -1):
                if points[j].x < points[i].x and points[j].y < points[i].y:
                    # print(points[i])
                    # print(points[j])
                    # print('='*20)
                    valid_rect(low_left = points[j], high_right= points[i])

s = Solution()
points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
print(s.minAreaRect(points))


# points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
# print(s.minAreaRect(points))

























        
