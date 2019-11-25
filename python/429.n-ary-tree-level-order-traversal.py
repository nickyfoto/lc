#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#
# https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/
#
# algorithms
# Easy (59.06%)
# Total Accepted:    32.1K
# Total Submissions: 54K
# Testcase Example:  '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}'
#
# Given an n-ary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
# 
# For example, given a 3-ary tree:
# 
# 
# 
# 
# 
# 
# 
# We should return its level order traversal:
# 
# 
# [
# ⁠    [1],
# ⁠    [3,2,4],
# ⁠    [5,6]
# ]
# 
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
    # def levelOrder(self, root: 'Node') -> List[List[int]]:
    def levelOrder(self, root):
        if not root:
            return []
        # self.max_level = 1
        res = [[root.val]]
        def bfs(nodes):
            if not nodes:
                return res
            l = []
            children_list = []
            for node in nodes:
                if node.children:
                    children_list.extend(node.children)
                    l.extend([n.val for n in node.children])
            if l:
                res.append(l)
            return bfs(children_list)
        res = bfs([root])
        return res
