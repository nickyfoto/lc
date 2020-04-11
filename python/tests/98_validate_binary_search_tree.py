#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (27.06%)
# Likes:    3084
# Dislikes: 445
# Total Accepted:    580.2K
# Total Submissions: 2.1M
# Testcase Example:  '[2,1,3]'
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
# 
# Assume a BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# 
# Example 1:
# 
# 
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 
# Input: [2,1,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# 
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def isValidBST(self, root: TreeNode) -> bool:
    def isValidBST(self, root):
        stack = [(root, -float('inf'), float('inf'))]
        while stack:
            node, lower, upper = stack.pop()
            if node:
                if node.val <= lower or node.val >= upper:
                    return False
                stack.append((node.left, lower, node.val))
                stack.append((node.right, node.val, upper))
        return True

    def isValidBST(self, root):
        """
        recursive
        """
        def recur(node, l=-math.inf, r=math.inf):
            if not node: return True
            val = node.val
            if val <= l or r <=val:
                return False
            if not recur(node.left, l, val) or not recur(node.right, val, r):
                return False
            return True
        return recur(root)
# @lc code=end
