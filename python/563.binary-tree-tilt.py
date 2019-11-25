#
# @lc app=leetcode id=563 lang=python3
#
# [563] Binary Tree Tilt
#
# https://leetcode.com/problems/binary-tree-tilt/description/
#
# algorithms
# Easy (47.03%)
# Total Accepted:    53.8K
# Total Submissions: 114.1K
# Testcase Example:  '[1,2,3]'
#
# Given a binary tree, return the tilt of the whole tree.
# 
# The tilt of a tree node is defined as the absolute difference between the sum
# of all left subtree node values and the sum of all right subtree node values.
# Null node has tilt 0.
# 
# The tilt of the whole tree is defined as the sum of all nodes' tilt.
# 
# Example:
# 
# Input: 
# ⁠        1
# ⁠      /   \
# ⁠     2     3
# Output: 1
# Explanation: 
# Tilt of node 2 : 0
# Tilt of node 3 : 0
# Tilt of node 1 : |2-3| = 1
# Tilt of binary tree : 0 + 0 + 1 = 1
# 
# 
# 
# Note:
# 
# The sum of node values in any subtree won't exceed the range of 32-bit
# integer. 
# All the tilt values won't exceed the range of 32-bit integer.
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
    # def findTilt(self, root: TreeNode) -> int:
    """
    def findTilt(self, root):
        if not root:
            return 0
        def isLeaf(node):
            return not node.left and not node.right
    
        def getSum(node, res=0):
            if not node:
                return 0
            if isLeaf(node):
                return node.val
            res += node.val    
            if node.right:
                res += getSum(node.right)
            if node.left:
                res += getSum(node.left)
            return res
            
        # print(getSum(root))
        def buildTilt(node):
            node.tilt = abs(getSum(node.left) - getSum(node.right))
            if node.left:
                buildTilt(node.left)
            if node.right:
                buildTilt(node.right)
        buildTilt(root)
        self.res = 0
        def dfs(node):
            self.res += node.tilt
            # print(node.tilt)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        return self.res
    """
    def findTilt(self, root):
        self.res = 0

        def traverse(node):
            if not node:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            self.res += abs(left-right)
            return left+right+node.val
        traverse(root)
        return self.res















        
