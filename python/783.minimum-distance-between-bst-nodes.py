#
# @lc app=leetcode id=783 lang=python3
#
# [783] Minimum Distance Between BST Nodes
#
# https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
#
# algorithms
# Easy (50.16%)
# Total Accepted:    31.9K
# Total Submissions: 63.4K
# Testcase Example:  '[4,2,6,1,3,null,null]'
#
# Given a Binary Search Tree (BST) with the root node root, return the minimum
# difference between the values of any two different nodes in the tree.
# 
# Example :
# 
# 
# Input: root = [4,2,6,1,3,null,null]
# Output: 1
# Explanation:
# Note that root is a TreeNode object, not an array.
# 
# The given tree [4,2,6,1,3,null,null] is represented by the following
# diagram:
# 
# ⁠         4
# ⁠       /   \
# ⁠     2      6
# ⁠    / \    
# ⁠   1   3  
# 
# while the minimum difference in this tree is 1, it occurs between node 1 and
# node 2, also between node 3 and node 2.
# 
# 
# Note:
# 
# 
# The size of the BST will be between 2 and 100.
# The BST is always valid, each node's value is an integer, and each node's
# value is different.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def minDiffInBST(self, root: TreeNode) -> int:
    def minDiffInBST(self, root):
        # print("hello world")
        self.min_distance = float('inf')

        def dfs(node, parents):
            if node:
                if node.left:
                    if node.val - node.left.val < self.min_distance:
                        self.min_distance = node.val - node.left.val
                    if parents:
                        for parent in parents:
                            if node.left.val - parent.val > 0 and node.left.val - parent.val < self.min_distance:
                                self.min_distance = node.left.val - parent.val
                    parents.append(node)
                    dfs(node.left, parents)
                if node.right:
                    if node.right.val - node.val < self.min_distance:
                        self.min_distance = node.right.val - node.val
                    if parents:
                        for parent in parents:
                            if parent.val - node.right.val > 0 and parent.val - node.right.val < self.min_distance:
                                self.min_distance = parent.val - node.right.val
                    parents.append(node)
                    dfs(node.right, parents)
        dfs(root, [])
        
        return self.min_distance




















