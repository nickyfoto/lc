#
# @lc app=leetcode id=671 lang=python3
#
# [671] Second Minimum Node In a Binary Tree
#
# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/
#
# algorithms
# Easy (43.42%)
# Total Accepted:    51.5K
# Total Submissions: 119.2K
# Testcase Example:  '[2,2,5,null,null,5,7]'
#
# Given a non-empty special binary tree consisting of nodes with the
# non-negative value, where each node in this tree has exactly two or zero
# sub-node. If the node has two sub-nodes, then this node's value is the
# smaller value among its two sub-nodes. More formally, the property root.val =
# min(root.left.val, root.right.val) always holds.
# 
# Given such a binary tree, you need to output the second minimum value in the
# set made of all the nodes' value in the whole tree.
# 
# If no such second minimum value exists, output -1 instead.
# 
# Example 1:
# 
# 
# Input: 
# ⁠   2
# ⁠  / \
# ⁠ 2   5
# ⁠    / \
# ⁠   5   7
# 
# Output: 5
# Explanation: The smallest value is 2, the second smallest value is 5.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# ⁠   2
# ⁠  / \
# ⁠ 2   2
# 
# Output: -1
# Explanation: The smallest value is 2, but there isn't any second smallest
# value.
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
    # def findSecondMinimumValue(self, root: TreeNode) -> int:
    def findSecondMinimumValue(self, root):
        self.small = []
        # [smallest, second_smallest]
        def update(node):
            if not self.small:
                self.small.append(node.val)
            if len(self.small) == 1:
                if node.left and node.left.val > self.small[0]:
                    self.small.append(node.left.val)
                elif node.right and node.right.val > self.small[0]:
                    self.small.append(node.right.val)
            else:
                if node.val < self.small[0]:
                    self.small = [node.val, self.small[0]]
                elif self.small[0] < node.val and node.val < self.small[1]:
                    self.small = [self.small[0], node.val]
        def dfs(node):
            update(node)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        # print(self.small)
        if len(self.small) < 2:
            return -1
        else:
            return self.small[1]
        # return self.small[1]
        
