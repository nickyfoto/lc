#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#
# https://leetcode.com/problems/binary-tree-preorder-traversal/description/
#
# algorithms
# Medium (52.57%)
# Total Accepted:    377.3K
# Total Submissions: 717.3K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the preorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,2,3]
# 
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def preorderTraversal(self, root: TreeNode) -> List[int]:
    def preorderTraversal2(self, root):
        if not root:
            return []
        self.res = []
        def dfs(node):
            if node:
                self.res.append(node.val)
                if node.left:
                    dfs(node.left)
                if node.right:
                    dfs(node.right)
        dfs(root)
        return self.res


    def preorderTraversal(self, root):
        if not root:
            return []
        self.res = []
        stack = [root]
        while stack:
            node = stack.pop()
            self.res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return self.res









        
