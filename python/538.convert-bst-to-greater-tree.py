#
# @lc app=leetcode id=538 lang=python3
#
# [538] Convert BST to Greater Tree
#
# https://leetcode.com/problems/convert-bst-to-greater-tree/description/
#
# algorithms
# Easy (51.14%)
# Total Accepted:    83.2K
# Total Submissions: 161.7K
# Testcase Example:  '[5,2,13]'
#
# Given a Binary Search Tree (BST), convert it to a Greater Tree such that
# every key of the original BST is changed to the original key plus sum of all
# keys greater than the original key in BST.
# 
# 
# Example:
# 
# Input: The root of a Binary Search Tree like this:
# ⁠             5
# ⁠           /   \
# ⁠          2     13
# 
# Output: The root of a Greater Tree like this:
# ⁠            18
# ⁠           /   \
# ⁠         20     13
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
    # def convertBST(self, root: TreeNode) -> TreeNode:
    def convertBST(self, root):
        if not root:
            return None

        # def getNewVal(node, key, res=0):
        #     if node.val > key:
        #         res += node.val
        #     if node.left:
        #         res = getNewVal(node.left, key, res)
        #     if node.right:
        #         res = getNewVal(node.right, key, res)
        #     return res
        self.all_nodes = []
        def dfs0(node):
            self.all_nodes.append(node.val)
            if node.left:
                dfs0(node.left)
            if node.right:
                dfs0(node.right)
        dfs0(root)
        self.all_nodes.sort()
        def getNewVal(key):
            idx = self.all_nodes.index(key)
            return sum(self.all_nodes[idx+1:])
        def dfs(node):
            node.new_val = node.val + getNewVal(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)

        def dfs2(node):
            # print(node.new_val)
            node.val = node.new_val
            if node.left:
                dfs2(node.left)
            if node.right:
                dfs2(node.right)
        dfs2(root)
        return root
