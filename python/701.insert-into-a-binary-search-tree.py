#
# @lc app=leetcode id=701 lang=python3
#
# [701] Insert into a Binary Search Tree
#
# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
#
# algorithms
# Medium (76.73%)
# Total Accepted:    56.6K
# Total Submissions: 73.7K
# Testcase Example:  '[4,2,7,1,3]\n5'
#
# Given the root node of a binary search tree (BST) and a value to be inserted
# into the tree, insert the value into the BST. Return the root node of the BST
# after the insertion. It is guaranteed that the new value does not exist in
# the original BST.
# 
# Note that there may exist multiple valid ways for the insertion, as long as
# the tree remains a BST after insertion. You can return any of them.
# 
# For example, 
# 
# 
# Given the tree:
# ⁠       4
# ⁠      / \
# ⁠     2   7
# ⁠    / \
# ⁠   1   3
# And the value to insert: 5
# 
# 
# You can return this binary search tree:
# 
# 
# ⁠        4
# ⁠      /   \
# ⁠     2     7
# ⁠    / \   /
# ⁠   1   3 5
# 
# 
# This tree is also valid:
# 
# 
# ⁠        5
# ⁠      /   \
# ⁠     2     7
# ⁠    / \   
# ⁠   1   3
# ⁠        \
# ⁠         4
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
    # def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
    def insertIntoBST(self, root, val):

        n = TreeNode(val)
        def bst(node):
            if node:
                if val < node.val:
                    if not node.left:
                        node.left = n
                    else:
                        bst(node.left)
                else:
                    if not node.right:
                        node.right = n
                    else:
                        bst(node.right)
        bst(root)
        return root




# from tn import buildRoot, null, TreeNode


# s = Solution()
# root = buildRoot([4,2,7,1,3])
# val = 5
# print(s.insertIntoBST(root, val))
























        
