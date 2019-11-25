#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#
# https://leetcode.com/problems/flood-fill/description/
#
# algorithms
# Easy (50.98%)
# Total Accepted:    50.6K
# Total Submissions: 99.1K
# Testcase Example:  '[[1,1,1],[1,1,0],[1,0,1]]\n1\n1\n2'
#
# 
# An image is represented by a 2-D array of integers, each integer representing
# the pixel value of the image (from 0 to 65535).
# 
# Given a coordinate (sr, sc) representing the starting pixel (row and column)
# of the flood fill, and a pixel value newColor, "flood fill" the image.
# 
# To perform a "flood fill", consider the starting pixel, plus any pixels
# connected 4-directionally to the starting pixel of the same color as the
# starting pixel, plus any pixels connected 4-directionally to those pixels
# (also with the same color as the starting pixel), and so on.  Replace the
# color of all of the aforementioned pixels with the newColor.
# 
# At the end, return the modified image.
# 
# Example 1:
# 
# Input: 
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: 
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels
# connected 
# by a path of the same color as the starting pixel are colored with the new
# color.
# Note the bottom corner is not colored 2, because it is not 4-directionally
# connected
# to the starting pixel.
# 
# 
# 
# Note:
# The length of image and image[0] will be in the range [1, 50].
# The given starting pixel will satisfy 0  and 0 .
# The value of each color in image[i][j] and newColor will be an integer in [0,
# 65535].
# 
#
class Solution:
    # def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    def floodFill(self, image, sr, sc, newColor):
        if image[sr][sc] == newColor:
            return image
        n_rows = len(image)
        n_cols = len(image[0])

        def getUp(r, c):
            if r < 0 or image[r][c] != start_pixel or explored[r][c]:
                return None
            return r, c
        def getDown(r, c):
            if r >= n_rows or image[r][c] != start_pixel or explored[r][c]:
                return None
            return r, c
        def getLeft(r, c):
            if c < 0 or image[r][c] != start_pixel or explored[r][c]:
                return None
            return r, c
        def getRight(r, c):
            if c >= n_cols or image[r][c] != start_pixel or explored[r][c]:
                return None
            return r,c

        
        start_pixel = image[sr][sc]
        # print(n_cols, n_rows)
        explored = [[False] * n_cols for i in [False] * n_rows]
        # print(explored)
        # for r in range(n_rows):
            # for c in range(n_cols):
                # if
        def dfs(sr, sc):
             if image[sr][sc] == start_pixel and not explored[sr][sc]:
                image[sr][sc] = newColor
                explored[sr][sc] = True
                for child in [getUp(sr-1, sc), getDown(sr+1, sc), getLeft(sr, sc-1), getRight(sr, sc+1)]:
                    if child:
                        dfs(*child)
        dfs(sr, sc)
        return image
# s = Solution()
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1
# sc = 1
# newColor = 2
# print(s.floodFill(image, sr, sc, newColor))




















        
