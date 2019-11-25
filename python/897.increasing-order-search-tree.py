#
# @lc app=leetcode id=897 lang=python3
#
# [897] Increasing Order Search Tree
#
# https://leetcode.com/problems/increasing-order-search-tree/description/
#
# algorithms
# Easy (63.95%)
# Total Accepted:    29.7K
# Total Submissions: 46.2K
# Testcase Example:  '[5,3,6,2,4,null,8,1,null,null,null,7,9]'
#
# Given a tree, rearrange the tree in in-order so that the leftmost node in the
# tree is now the root of the tree, and every node has no left child and only 1
# right child.
# 
# 
# Example 1:
# Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]
# 
# ⁠      5
# ⁠     / \
# ⁠   3    6
# ⁠  / \    \
# ⁠ 2   4    8
# /        / \ 
# 1        7   9
# 
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
# 
# ⁠1
# \
# 2
# \
# 3
# \
# 4
# \
# 5
# \
# 6
# \
# 7
# \
# 8
# \
# ⁠                9  
# 
# Note:
# 
# 
# The number of nodes in the given tree will be between 1 and 100.
# Each node will have a unique integer value from 0 to 1000.
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
    # def increasingBST(self, root: TreeNode) -> TreeNode:
    def increasingBST(self, root):
        self.q = []
        def addToQ(node):
            if node.left and node.right:
                addToQ(node.left)
                self.q.append(node.val)
                addToQ(node.right)
            elif node.left and not node.right:
                addToQ(node.left)
                self.q.append(node.val)
            elif node.right and not node.left:
                self.q.append(node.val)
                addToQ(node.right)
            else:
                self.q.append(node.val)
        addToQ(root)
        # print(self.q)
        self.root = TreeNode(self.q.pop(0))
        def buildIOST(node):
            if self.q:
                node.right = buildIOST(TreeNode(self.q.pop(0)))
            return node
        buildIOST(self.root)
        return self.root
