#
# @lc app=leetcode id=993 lang=python3
#
# [993] Cousins in Binary Tree
#
# https://leetcode.com/problems/cousins-in-binary-tree/description/
#
# algorithms
# Easy (52.42%)
# Total Accepted:    18.2K
# Total Submissions: 34.8K
# Testcase Example:  '[1,2,3,4]\n4\n3'
#
# In a binary tree, the root node is at depth 0, and children of each depth k
# node are at depth k+1.
# 
# Two nodes of a binary tree are cousins if they have the same depth, but have
# different parents.
# 
# We are given the root of a binary tree with unique values, and the values x
# and y of two different nodes in the tree.
# 
# Return true if and only if the nodes corresponding to the values x and y are
# cousins.
# 
# 
# 
# Example 1:
# 
# 
# 
# Input: root = [1,2,3,4], x = 4, y = 3
# Output: false
# 
# 
# 
# Example 2:
# 
# 
# 
# Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: root = [1,2,3,null,4], x = 2, y = 3
# Output: false
# 
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the tree will be between 2 and 100.
# Each node has a unique integer value from 1 to 100.
# 
# 
# 
# 
# 
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
    # def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
    def isCousins(self, root, x, y):
        def recur(node, parent, level, target):
            if node.val == target:
                if parent:
                    return parent.val, level
                return None, level
            else:
                if node.left:
                    p, l = recur(node.left, node, level+1, target)
                    if l:
                        return p, l
                if node.right:
                    p, r = recur(node.right, node, level+1, target)
                    if r:
                        return p, r
                return None, None
                # print(node.val)
                # return None, None
                # print('here')
                # if parent:
                    # return parent.val, level
                # return None, level
        px, lx = recur(root, None, 0, x)
        py, ly = recur(root, None, 0, y)
        if lx == ly and px != py:
            return True
        return False





































        
