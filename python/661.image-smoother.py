#
# @lc app=leetcode id=661 lang=python3
#
# [661] Image Smoother
#
# https://leetcode.com/problems/image-smoother/description/
#
# algorithms
# Easy (48.90%)
# Total Accepted:    36.5K
# Total Submissions: 74.5K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a 2D integer matrix M representing the gray scale of an image, you need
# to design a smoother to make the gray scale of each cell becomes the average
# gray scale (rounding down) of all the 8 surrounding cells and itself.  If a
# cell has less than 8 surrounding cells, then use as many as you can.
# 
# Example 1:
# 
# Input:
# [[1,1,1],
# ⁠[1,0,1],
# ⁠[1,1,1]]
# Output:
# [[0, 0, 0],
# ⁠[0, 0, 0],
# ⁠[0, 0, 0]]
# Explanation:
# For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# For the point (1,1): floor(8/9) = floor(0.88888889) = 0
# 
# 
# 
# Note:
# 
# The value in the given matrix is in the range of [0, 255].
# The length and width of the given matrix are in the range of [1, 150].
# 
# 
#
from copy import deepcopy
class Solution:
    # def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
    def imageSmoother(self, M):
        res = deepcopy(M)
        n_rows = len(M)
        n_cols = len(M[0])
        def getUp(r,c):
            if r < 0:
                return []
            elif c == 0:
                return M[r][:c+2]
            else:
                return M[r][c-1:c+2]
        def getMid(r, c):
            if c == 0:
                return M[r][:c+2]
            else:
                return M[r][c-1:c+2]
        def getDown(r, c):
            if r == n_rows:
                return []
            elif c == 0:
                return M[r][:c+2]
            else:
                return M[r][c-1:c+2]
        def update(r,c):
            # print(r,c, getUp(r-1, c), getMid(r, c), getDown(r+1, c))
            l = getUp(r-1, c) + getMid(r, c) + getDown(r+1, c)
            # print(r,c, l)
            return int(sum(l) / len(l))
        for r in range(n_rows):
            for c in range(n_cols):
                res[r][c] = update(r,c)
        return res

# s = Solution()
# M =  [[1,1,1],[1,0,1],[1,1,1]]
# print(s.imageSmoother(M))