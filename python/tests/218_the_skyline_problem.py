#
# @lc app=leetcode id=218 lang=python3
#
# [218] The Skyline Problem
#
# https://leetcode.com/problems/the-skyline-problem/description/
#
# algorithms
# Hard (33.37%)
# Likes:    1781
# Dislikes: 98
# Total Accepted:    121.2K
# Total Submissions: 360.5K
# Testcase Example:  '[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]'
#
# A city's skyline is the outer contour of the silhouette formed by all the
# buildings in that city when viewed from a distance. Now suppose you are given
# the locations and height of all the buildings as shown on a cityscape photo
# (Figure A), write a program to output the skyline formed by these buildings
# collectively (Figure B).
# ⁠   
# 
# The geometric information of each building is represented by a triplet of
# integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and
# right edge of the ith building, respectively, and Hi is its height. It is
# guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You
# may assume all buildings are perfect rectangles grounded on an absolutely
# flat surface at height 0.
# 
# For instance, the dimensions of all buildings in Figure A are recorded as: [
# [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .
# 
# The output is a list of "key points" (red dots in Figure B) in the format of
# [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key
# point is the left endpoint of a horizontal line segment. Note that the last
# key point, where the rightmost building ends, is merely used to mark the
# termination of the skyline, and always has zero height. Also, the ground in
# between any two adjacent buildings should be considered part of the skyline
# contour.
# 
# For instance, the skyline in Figure B should be represented as:[ [2 10], [3
# 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].
# 
# Notes:
# 
# 
# The number of buildings in any input list is guaranteed to be in the range
# [0, 10000].
# The input list is already sorted in ascending order by the left x position
# Li.
# The output list must be sorted by the x position.
# There must be no consecutive horizontal lines of equal height in the output
# skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not
# acceptable; the three lines of height 5 should be merged into one in the
# final output as such: [...[2 3], [4 5], [12 7], ...]
# 
# 
#

# @lc code=start
from heapq import heappop, heappush
import math
class Solution:
    # def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
    def mergeSkyline(self, left, right):
        
        def update_output(x, y):
            if not output or output[-1][0] != x:
                output.append([x, y])
            else:
                output[-1][1] = y
                
        def append_skyline(p, lst, n, y, curr_y):
            while p < n:
                x, y = lst[p]
                p += 1
                if curr_y != y:
                    update_output(x, y)
                    curr_y = y
        
        nl, nr = len(left), len(right)
        pl = pr = 0
        curr_y = left_y = right_y = 0
        output = []
        while pl < nl and pr < nr:
            point_l, point_r = left[pl], right[pr]
            if point_l[0] < point_r[0]:
                x, left_y = point_l
                pl += 1
            else:
                x, right_y = point_r
                pr += 1
            max_y = max(left_y, right_y)
            if curr_y != max_y:
                update_output(x, max_y)
                curr_y = max_y
        append_skyline(pl, left, nl, left_y, curr_y)
        append_skyline(pr, right, nr, right_y, curr_y)
        return output

    def getSkyline(self, buildings):
        n = len(buildings)
        if n == 0: return []
        if n == 1:
            x_start, x_end, y = buildings[0]
            return [[x_start, y], [x_end, 0]]
        left_skyline = self.getSkyline(buildings[:n // 2])
        right_skyline = self.getSkyline(buildings[n // 2:])
        return self.mergeSkyline(left_skyline, right_skyline)

    def getSkyline(self, buildings):
        events = [(L, -H, R) for L, R, H in buildings]
        events += list({(R, 0, 0) for _, R, _ in buildings})
        events.sort()

        res = [[0, 0]]
        live = [(0, math.inf)]
        for pos, negH, R in events:
            while live[0][1] <= pos:
                heappop(live)
            if negH:
                heappush(live, (negH, R))
            if res[-1][1] != - live[0][0]:
                res += [[pos, - live[0][0]]]
        return res[1:]
# @lc code=end
