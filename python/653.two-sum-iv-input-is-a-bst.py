#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
#
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
#
# algorithms
# Easy (52.56%)
# Total Accepted:    92K
# Total Submissions: 174.6K
# Testcase Example:  '[5,3,6,2,4,null,7]\n9'
#
# Given a Binary Search Tree and a target number, return true if there exist
# two elements in the BST such that their sum is equal to the given target.
# 
# Example 1:
# 
# 
# Input: 
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
# 
# Target = 9
# 
# Output: True
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
# 
# Target = 28
# 
# Output: False
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
    # def findTarget(self, root: TreeNode, k: int) -> bool:
    def findTarget(self, root, k):
        self.l = []
        def dfs(node):
            if node:
                self.l.append(node.val)
                if node.left:
                    dfs(node.left)
                if node.right:
                    dfs(node.right)
        dfs(root)

        def bs(node, target):
            if not node:
                return False
            if node.val == target:
                return True
            else:
                if node.val < target:
                    return bs(node.right, target)
                else:
                    return bs(node.left, target)
        for i in self.l:
            # print(i, k-i)
            if k - i != i and bs(root, k-i):
                return True
        
        return False

        # print(self.l)


























        
