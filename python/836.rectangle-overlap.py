#
# @lc app=leetcode id=836 lang=python3
#
# [836] Rectangle Overlap
#
# https://leetcode.com/problems/rectangle-overlap/description/
#
# algorithms
# Easy (46.21%)
# Total Accepted:    24.1K
# Total Submissions: 52K
# Testcase Example:  '[0,0,2,2]\n[1,1,3,3]'
#
# A rectangle is represented as a list [x1, y1, x2, y2], where (x1, y1) are the
# coordinates of its bottom-left corner, and (x2, y2) are the coordinates of
# its top-right corner.
# 
# Two rectangles overlap if the area of their intersection is positive.  To be
# clear, two rectangles that only touch at the corner or edges do not overlap.
# 
# Given two (axis-aligned) rectangles, return whether they overlap.
# 
# Example 1:
# 
# 
# Input: rec1 = [0,0,2,2], rec2 = [1,1,3,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: rec1 = [0,0,1,1], rec2 = [1,0,2,1]
# Output: false
# 
# 
# Notes:
# 
# 
# Both rectangles rec1 and rec2 are lists of 4 integers.
# All coordinates in rectangles will be between -10^9 and 10^9.
# 
# 
#
class Solution:
    # def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
    def isRectangleOverlap(self, rec1, rec2):


        def recur(rec1, rec2, final=False):
            x1, y1, x2, y2 = tuple(rec1)
            a1, b1, a2, b2 = tuple(rec2)
            # print(a2, b2)
            # print(x1, y1)
            # print(x2, y2)
            if (x1 <= a1 and y1 <=b1) and (a1 < x2 and b1 < y2): #a1b1
                return True
            elif (x1 < a2 and y1 < b2) and (a2 <= x2 and b2 <= y2): #a2b2
                return True
            elif (a2 <= x2 and y1 <= b1) and (x1 < a2 and b1 < y2): #a2b1
                # print('here')
                return True
            elif (a1 < x2 and y1 < b2) and (x1 <= a1 and b2 <= y2): #a1b2
                return True
            elif (x1 <= a1 and a2 <= x2) and (b1 < y1 and y2 < b2):
                # print('here')
                return True
            else:
                if not final:
                    return recur(rec2, rec1, True)
                else:
                    return False
        return recur(rec1, rec2)
# s = Solution()
# # rec1 = [0,0,2,2]
# # rec2 = [1,1,3,3]
# # print(s.isRectangleOverlap(rec1, rec2))


# # rec1 = [0,0,1,1]
# # rec2 = [1,0,2,1]

# # print(s.isRectangleOverlap(rec1, rec2))


# # rec1 = [4,4,14,7]
# # rec2 = [4,3,8,8]
# # print(s.isRectangleOverlap(rec1, rec2))

# rec1 = [-7,-3,10,5]
# rec2 = [-6,-5,5,10]
# print(s.isRectangleOverlap(rec1, rec2))

