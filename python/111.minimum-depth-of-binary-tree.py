#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (35.38%)
# Total Accepted:    302.5K
# Total Submissions: 853.4K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
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
# return its minimum depth = 2.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def minDepth(self, root: TreeNode) -> int:
    def minDepth(self, root):
        def bfs(node, level):
            if not node.left and not node.right:
                return level
            else:
                if not node.left:
                    return bfs(node.right, level+1)
                elif not node.right:
                    return bfs(node.left, level+1)
                else:
                    return min(bfs(node.left, level+1), bfs(node.right, level+1))
        if not root:
            return 0
        return bfs(root, 1)
                


















        
