#
# @lc app=leetcode id=427 lang=python3
#
# [427] Construct Quad Tree
#
# https://leetcode.com/problems/construct-quad-tree/description/
#
# algorithms
# Medium (58.72%)
# Total Accepted:    16.2K
# Total Submissions: 27.5K
# Testcase Example:  '[[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]'
#
# We want to use quad trees to store an N x N boolean grid. Each cell in the
# grid can only be true or false. The root node represents the whole grid. For
# each node, it will be subdivided into four children nodes until the values in
# the region it represents are all the same.
# 
# Each node has another two boolean attributes : isLeaf and val. isLeaf is true
# if and only if the node is a leaf node. The val attribute for a leaf node
# contains the value of the region it represents.
# 
# Your task is to use a quad tree to represent a given grid. The following
# example may help you understand the problem better:
# 
# Given the 8 x 8 grid below, we want to construct the corresponding quad
# tree:
# 
# 
# 
# It can be divided according to the definition above:
# 
# 
# 
# 
# 
# The corresponding quad tree should be as following, where each node is
# represented as a (isLeaf, val) pair.
# 
# For the non-leaf nodes, val can be arbitrary, so it is represented as *.
# 
# 
# 
# Note:
# 
# 
# N is less than 1000 and guaranteened to be a power of 2.
# If you want to know more about the quad tree, you can refer to its wiki.
# 
# 
#
"""
# Definition for a QuadTree node.
"""
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    # def construct(self, grid: List[List[int]]) -> 'Node':
    def construct(self, grid):
        

        def build(node, grid):
            n = len(grid)
            s = sum(sum(r) for r in grid) 
            if s == n**2:
                val = True
                isLeaf = True
                node = Node(val, isLeaf, None, None, None,None)
                return node
            elif s == 0:
                val = False
                isLeaf = True
                node = Node(val, isLeaf, None, None, None,None)
                return node
            else:
                val = True
                isLeaf = False
                top = grid[:n//2]
                bottom = grid[n//2:]
                # print(top)
                tl = [r[:n//2] for r in top]
                tr = [r[n//2:] for r in top]
                bl = [r[:n//2] for r in bottom]
                br = [r[n//2:] for r in bottom]
            if not node:
                topLeft     = build(None, tl)
                topRight    = build(None, tr)
                bottomLeft  = build(None, bl)
                bottomRight = build(None, br)
                node = Node(val, isLeaf, topLeft, topRight,
                                         bottomLeft, bottomRight)

            return node


        return build(None, grid)



s = Solution()
grid = [[1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,1,1,1,1],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,0,0],
        [1,1,1,1,0,0,0,0]]
print(s.construct(grid))