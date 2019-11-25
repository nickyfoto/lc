#
# @lc app=leetcode id=1008 lang=python3
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/
#
# algorithms
# Medium (73.36%)
# Total Accepted:    21.6K
# Total Submissions: 29.4K
# Testcase Example:  '[8,5,1,7,10,12]'
#
# Return the root node of a binary search tree that matches the given preorder
# traversal.
# 
# (Recall that a binary search tree is a binary tree where for every node, any
# descendant of node.left has a value < node.val, and any descendant of
# node.right has a value > node.val.  Also recall that a preorder traversal
# displays the value of the node first, then traverses node.left, then
# traverses node.right.)
# 
# 
# 
# Example 1:
# 
# 
# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]
# 
# 
# 
# 
# 
# Note: 
# 
# 
# 1 <= preorder.length <= 100
# The values of preorder are distinct.
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder):
        root = TreeNode(preorder.pop(0))

        def add(node, v):
            if not node:
                node = TreeNode(v)
                return node
            else:
                if v < node.val:
                    node.left = add(node.left, v)
                else:
                    node.right = add(node.right,v)
                return node
        while preorder:
           add(root, preorder.pop(0))

        return root

# from tn import TreeNode
# s = Solution()
# preorder = [8,5,1,7,10,12]
# print(s.bstFromPreorder(preorder))












