#
# @lc app=leetcode id=687 lang=python3
#
# [687] Longest Univalue Path
#
# https://leetcode.com/problems/longest-univalue-path/description/
#
# algorithms
# Easy (33.56%)
# Total Accepted:    58.1K
# Total Submissions: 172.5K
# Testcase Example:  '[5,4,5,1,1,5]'
#
# Given a binary tree, find the length of the longest path where each node in
# the path has the same value. This path may or may not pass through the root.
# 
# The length of path between two nodes is represented by the number of edges
# between them.
# 
# 
# 
# Example 1:
# 
# Input:
# 
# 
# ⁠             5
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         1   1   5
# 
# 
# Output: 2
# 
# 
# 
# Example 2:
# 
# Input:
# 
# 
# ⁠             1
# ⁠            / \
# ⁠           4   5
# ⁠          / \   \
# ⁠         4   4   5
# 
# 
# Output: 2
# 
# 
# 
# Note: The given binary tree has not more than 10000 nodes. The height of the
# tree is not more than 1000.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def longestUnivaluePath(self, root: TreeNode) -> int:
    def longestUnivaluePath(self, root):
        if not root:
            return 0
        self.length = []
        self.q = [root]
        def pathLength(node, parent):
            if not node or node.val != parent.val:
                return 0
            return 1 + max([pathLength(node.left, node), pathLength(node.right, node)])
        def dfs(node):
            while self.q:
                node = self.q.pop(0)
                l = pathLength(node.left, node) + pathLength(node.right, node)
                self.length.append(l)
                if node.right:
                    self.q.insert(0, node.right)
                if node.left:
                    self.q.insert(0, node.left)
        dfs(root)
        # print(self.length)
        if self.length:
            return max(self.length)
        else:
            return 0






















