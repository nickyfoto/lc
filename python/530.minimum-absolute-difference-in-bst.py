#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#
# https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
#
# algorithms
# Easy (50.64%)
# Total Accepted:    62.1K
# Total Submissions: 122.1K
# Testcase Example:  '[1,null,3,2]'
#
# Given a binary search tree with non-negative values, find the minimum
# absolute difference between values of any two nodes.
# 
# Example:
# 
# 
# Input:
# 
# ⁠  1
# ⁠   \
# ⁠    3
# ⁠   /
# ⁠  2
# 
# Output:
# 1
# 
# Explanation:
# The minimum absolute difference is 1, which is the difference between 2 and 1
# (or between 2 and 3).
# 
# 
# 
# 
# Note: There are at least two nodes in this BST.
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def getMinimumDifference(self, root: TreeNode) -> int:
    def getMinimumDifference(self, root):
        self.minimum = float('inf')

        def isLeaf(node):
            return not node.right and not node.left

        def bstMin(node):
            """
            given a root of a BST, find the val of min leaf
            """
            if isLeaf(node) or not node.left:
                return node.val
            else:
                return bstMin(node.left)

        def bstMax(node):
            if isLeaf(node) or not node.right:
                return node.val
            else:
                return bstMax(node.right)


        def findMin(node):
            if node.left and node.right:
                return min(bstMin(node.right) - node.val, node.val - bstMax(node.left))
            elif node.left and not node.right:
                return node.val - bstMax(node.left)
            elif node.right and not node.left:
                return bstMin(node.right) - node.val

        def dfs(node):
            fm = findMin(node)
            if fm < self.minimum:
                self.minimum = fm
            if node.left and not isLeaf(node.left):
                dfs(node.left)
            if node.right and not isLeaf(node.right):
                dfs(node.right)
        dfs(root)
        return self.minimum
























        
