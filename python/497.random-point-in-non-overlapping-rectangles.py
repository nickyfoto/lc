#
# @lc app=leetcode id=497 lang=python3
#
# [497] Random Point in Non-overlapping Rectangles
#
# https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/description/
#
# algorithms
# Medium (36.06%)
# Total Accepted:    8.2K
# Total Submissions: 22.7K
# Testcase Example:  '["Solution", "pick", "pick", "pick"]\n[[[[1, 1, 5, 5]]], [], [], []]'
#
# Given a list of non-overlapping axis-aligned rectangles rects, write a
# function pick which randomly and uniformily picks an integer point in the
# space covered by the rectangles.
# 
# Note:
# 
# 
# An integer point is a point that has integer coordinates. 
# A point on the perimeter of a rectangle is included in the space covered by
# the rectangles. 
# ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the integer
# coordinates of the bottom-left corner, and [x2, y2] are the integer
# coordinates of the top-right corner.
# length and width of each rectangle does not exceed 2000.
# 1 <= rects.length <= 100
# pick return a point as an array of integer coordinates [p_x, p_y]
# pick is called at most 10000 times.
# 
# 
# 
# Example 1:
# 
# 
# Input: 
# ["Solution","pick","pick","pick"]
# [[[[1,1,5,5]]],[],[],[]]
# Output: 
# [null,[4,1],[4,1],[3,3]]
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# ["Solution","pick","pick","pick","pick","pick"]
# [[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
# Output: 
# [null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]]
# 
# 
# 
# Explanation of Input Syntax:
# 
# The input is two lists: the subroutines called and their arguments.
# Solution's constructor has one argument, the array of rectangles rects. pick
# has no arguments. Arguments are always wrapped with a list, even if there
# aren't any.
# 
# 
# 
# 
# 
# 
# 
#
from random import randint, choices
import bisect
class Rect:
    def __init__(self, x1,y1,x2,y2):
        self.left = x1
        self.right = x2
        self.bottom = y1
        self.top = y2
        self.area = self.total_points()
        # print(self.area)

    def total_points(self):
        high = self.top - self.bottom + 1
        width = self.right - self.left + 1
        return high * width

class Solution:

    def __init__(self, rects):
        self.rects, self.ranges, sm = rects, [0], 0
        for x1, y1, x2, y2 in rects:
            sm += (x2 - x1 + 1) * (y2 - y1 + 1)
            self.ranges.append(sm)
        print(self.ranges)

    # def __init__(self, rects: List[List[int]]):
    # def __init__(self, rects):
    #     self.rects = list(map(lambda x: Rect(*x), rects))
    #     self.weights = list(map(lambda x: x.area, self.rects))
        
        # print(self.rects)
    
    def pick(self):
        n = randint(0, self.ranges[-1] - 1)
        i = bisect.bisect(self.ranges, n)
        print(n, i)
        x1, y1, x2, y2 = self.rects[i - 1]
        n -= self.ranges[i - 1]
        print('here', self.ranges[i - 1])
        return [x1 + n % (x2 - x1 + 1), y1 + n // (x2 - x1 + 1)]

    # def pick(self):
    #     rect = choices(population=self.rects, weights=self.weights)[0]
    #     # print('here', rect)
    #     return [randint(rect.left, rect.right), randint(rect.bottom, rect.top)]

# Your Solution object will be instantiated and called as such:
# rects = [[1,1,5,5]]
rects = [[-2,-2,-1,-1],[1,0,3,0]]
obj = Solution(rects)
for i in range(10):
    print(obj.pick())
# param_1 = obj.pick()
