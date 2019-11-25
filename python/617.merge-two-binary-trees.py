#
# @lc app=leetcode id=617 lang=python3
#
# [617] Merge Two Binary Trees
#
# https://leetcode.com/problems/merge-two-binary-trees/description/
#
# algorithms
# Easy (69.83%)
# Total Accepted:    174.5K
# Total Submissions: 249K
# Testcase Example:  '[1,3,2,5]\n[2,1,3,null,4,null,7]'
#
# Given two binary trees and imagine that when you put one of them to cover the
# other, some nodes of the two trees are overlapped while the others are not.
# 
# You need to merge them into a new binary tree. The merge rule is that if two
# nodes overlap, then sum node values up as the new value of the merged node.
# Otherwise, the NOT null node will be used as the node of new tree.
# 
# Example 1:
# 
# 
# Input: 
# Tree 1                     Tree 2                  
# ⁠         1                         2                             
# ⁠        / \                       / \                            
# ⁠       3   2                     1   3                        
# ⁠      /                           \   \                      
# ⁠     5                             4   7                  
# Output: 
# Merged tree:
# 3
# / \
# 4   5
# / \   \ 
# 5   4   7
# 
# 
# 
# 
# Note: The merging process must start from the root nodes of both trees.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
    def mergeTrees(self, t1, t2):
        if not t1:
            return t2
        if not t2:
            return t1
        def isLeaf(node):
            return not node.right and not node.left
        def merge(n1, n2):
            if isLeaf(n2):
                n1.val += n2.val
                return n1, None
            # print(isLeaf(n2))
            if n1.right and n2.right:
                if isLeaf(n2.right):
                    n1.right.val += n2.right.val
                    n2.right = None
                else:
                    n1.right, _ = merge(n1.right, n2.right)
            if n1.left and n2.left:
                if isLeaf(n2.left):
                    n1.left.val += n2.left.val
                    n2.left = None
                else:
                    n1.left, _ = merge(n1.left, n2.left)
            if not n1.right and n2.right:
                n1.right = n2.right
                n2.right = None
            if not n1.left and n2.left:
                n1.left = n2.left
                n2.left = None
            # print(n2.val, n2.left, n2.right)
            # print(isLeaf(n2))

            return n1, n2
        n1, n2 = merge(t1, t2)
        # print(n2.val, n2.left, n2.right)
        while n2:
            n1, n2 = merge(n1, n2)
        return n1
























        
