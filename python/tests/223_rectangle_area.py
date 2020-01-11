#
# @lc app=leetcode id=223 lang=python3
#
# [223] Rectangle Area
#
# https://leetcode.com/problems/rectangle-area/description/
#
# algorithms
# Medium (36.87%)
# Likes:    318
# Dislikes: 602
# Total Accepted:    97.6K
# Total Submissions: 264.6K
# Testcase Example:  '-3\n0\n3\n4\n0\n-1\n9\n2'
#
# Find the total area covered by two rectilinear rectangles in a 2D plane.
# 
# Each rectangle is defined by its bottom left corner and top right corner as
# shown in the figure.
# 
# 
# 
# Example:
# 
# 
# Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
# Output: 45
# 
# Note:
# 
# Assume that the total area is never beyond the maximum possible value of int.
# 
#

# @lc code=start
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        
        class Rect:
            def __init__(self, lower_left_x, lower_left_y,
                               upper_right_x, upper_right_y):
                self.lower_left_x = lower_left_x
                self.lower_left_y = lower_left_y
                self.upper_right_x = upper_right_x
                self.upper_right_y = upper_right_y

                self.w = upper_right_x - lower_left_x
                self.h = upper_right_y - lower_left_y
                self.left = lower_left_x
                self.right = upper_right_x
                self.bottom = lower_left_y
                self.top = upper_right_y
            @property
            def area(self):
                return self.w * self.h
        
        r1 = Rect(A, B, C, D)
        r2 = Rect(E, F, G, H)
        
        # print(r1.area, r2.area)

        def overlap(r1, r2):
            if r1.left >= r2.right or r2.left >= r1.right: return False
            if r1.bottom >= r2.top or r2.bottom >= r1.top: return False
            return True
            
        def get_overlap(r1, r2):
            """
            return a Rect instance
            """
            lower_left_x = max(r1.lower_left_x, r2.lower_left_x)
            lower_left_y = max(r1.lower_left_y, r2.lower_left_y)
            upper_right_x = min(r1.upper_right_x, r2.upper_right_x)
            upper_right_y = min(r1.upper_right_y, r2.upper_right_y)
            return Rect(lower_left_x, lower_left_y, upper_right_x, upper_right_y)

        def common(r1, r2):
            if not overlap(r1, r2):
                return 0
            else:
                ol_reat = get_overlap(r1, r2)
                return ol_reat.area


        c  = common(r1, r2)
        # print(r1.area, r2.area)
        return r1.area + r2.area - c
# @lc code=end
