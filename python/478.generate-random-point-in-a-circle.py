#
# @lc app=leetcode id=478 lang=python3
#
# [478] Generate Random Point in a Circle
#
# https://leetcode.com/problems/generate-random-point-in-a-circle/description/
#
# algorithms
# Medium (37.33%)
# Total Accepted:    6.4K
# Total Submissions: 17.2K
# Testcase Example:  '["Solution", "randPoint", "randPoint", "randPoint"]\n[[1.0, 0.0, 0.0], [], [], []]'
#
# Given the radius and x-y positions of the center of a circle, write a
# function randPoint which generates a uniform random point in the circle.
# 
# Note:
# 
# 
# input and output values are in floating-point.
# radius and x-y position of the center of the circle is passed into the class
# constructor.
# a point on the circumference of the circle is considered to be in the
# circle.
# randPoint returns a size 2 array containing x-position and y-position of the
# random point, in that order.
# 
# 
# 
# Example 1:
# 
# 
# Input: 
# ["Solution","randPoint","randPoint","randPoint"]
# [[1,0,0],[],[],[]]
# Output: [null,[-0.72939,-0.65505],[-0.78502,-0.28626],[-0.83119,-0.19803]]
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# ["Solution","randPoint","randPoint","randPoint"]
# [[10,5,-7.5],[],[],[]]
# Output: [null,[11.52438,-8.33273],[2.46992,-16.21705],[11.13430,-12.42337]]
# 
# 
# Explanation of Input Syntax:
# 
# The input is two lists: the subroutines called and their arguments.
# Solution's constructor has three arguments, the radius, x-position of the
# center, and y-position of the center of the circle. randPoint has no
# arguments. Arguments are always wrapped with a list, even if there aren't
# any.
# 
# 
#
# from math import sqrt
# from random import uniform
# class Solution:

#     def __init__(self, radius: float, x_center: float, y_center: float):
#         self.radius = radius
#         self.x_center = x_center
#         self.x_left = x_center - radius
#         self.x_right = x_center + radius
#         self.y_center = y_center
#     # def randPoint(self) -> List[float]:
#     def randPoint(self):

#         x = uniform(self.x_left, self.x_right)
#         x_to_center = abs(x-self.x_center)
#         y = sqrt(self.radius**2 - x_to_center**2)
#         y = uniform(self.y_center - y, self.y_center + y)
#         return [x,y]


import random
class Solution(object):

    def __init__(self, radius, x_center, y_center):
        """
        :type radius: float
        :type x_center: float
        :type y_center: float
        """
        self.x_min, self.x_max = x_center - radius, x_center + radius
        self.y_min, self.y_max = y_center - radius, y_center + radius
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        """
        :rtype: List[float]
        """
        while True:
            x, y = random.uniform(self.x_min, self.x_max), random.uniform(self.y_min, self.y_max)
            if (x - self.x_center)**2 + (y - self.y_center)**2 <= self.radius**2:
                return [x, y]

# Your Solution object will be instantiated and called as such:
# radius, x_center, y_center = tuple([1,0,0])
# radius, x_center, y_center = tuple([10,5,-7.5])
# radius, x_center, y_center = [0.01, -73839.1, -3289891.3]
# obj = Solution(radius, x_center, y_center)
# res = []
# for i in range(300):
    # p = obj.randPoint()
    # print(p[0], ',', p[1])
# print(res)
# p = obj.randPoint()

# print('r=', radius, 'distance=', sqrt((p[0] - x_center)**2+(p[1] - y_center)**2))
# param_1 = obj.randPoint()


# x = [-0.72939,-0.65505]
# x = [-0.78502,-0.28626]
# x = [-0.83119,-0.19803]

# print(x[0]**2+x[1]**2)


# x = [11.52438,-8.33273]
# print((x[0] - 5)**2 + (x[1] - (-7.5))**2)



