#
# @lc app=leetcode id=559 lang=python3
#
# [559] Maximum Depth of N-ary Tree
#
# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/
#
# algorithms
# Easy (65.24%)
# Total Accepted:    46.1K
# Total Submissions: 70.4K
# Testcase Example:  '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}'
#
# Given a n-ary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
# 
# For example, given a 3-ary tree:
# 
# 
# 
# 
# 
# 
# We should return its max depth, which is 3.
# 
# 
# 
# Note:
# 
# 
# The depth of the tree is at most 1000.
# The total number of nodes is at most 5000.
# 
# 
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    # def maxDepth(self, root: 'Node') -> int:
    def maxDepth(self, root):
        # print(root.children)
        if not root:
            return 0
        self.max_level = 1
        q = [(root, 1)]
        def dfs(p):
            node, level = p
            if node.children:
                level += 1
                if level > self.max_level:
                    self.max_level = level
                q.extend([(n, level) for n in node.children])
            while q:
                dfs(q.pop(0))
        dfs(q.pop(0))
        return self.max_level
        
