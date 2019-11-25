#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#
# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (60.77%)
# Total Accepted:    523.8K
# Total Submissions: 860.3K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its maximum depth.
# 
# The maximum depth is the number of nodes along the longest path from the root
# node down to the farthest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given binary tree [3,9,20,null,null,15,7],
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# return its depth = 3.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def maxDepth(self, root: TreeNode) -> int:
    def maxDepth(self, root):
        if not root:
            return 0
        self.max_depth = 1
        def dfs(node, level):
            if not node.left and not node.right:
                if level > self.max_depth:
                    self.max_depth = level
            else:
                if node.left:
                    dfs(node.left, level+1)
                if node.right:
                    dfs(node.right, level+1)
        dfs(root, 1)
        return self.max_depth






























        
