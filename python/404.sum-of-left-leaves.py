#
# @lc app=leetcode id=404 lang=python3
#
# [404] Sum of Left Leaves
#
# https://leetcode.com/problems/sum-of-left-leaves/description/
#
# algorithms
# Easy (49.17%)
# Total Accepted:    130.6K
# Total Submissions: 264.8K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Find the sum of all left leaves in a given binary tree.
# 
# Example:
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# There are two left leaves in the binary tree, with values 9 and 15
# respectively. Return 24.
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
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        def isLeaf(node):
            return not node.left and not node.right
        def dfs(node):
            if node.left and isLeaf(node.left):
                self.res += node.left.val
            if node.left and not isLeaf(node.left):
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        return self.res
