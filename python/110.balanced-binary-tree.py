#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
# https://leetcode.com/problems/balanced-binary-tree/description/
#
# algorithms
# Easy (41.11%)
# Total Accepted:    331K
# Total Submissions: 803K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, determine if it is height-balanced.
# 
# For this problem, a height-balanced binary tree is defined as:
# 
# 
# a binary tree in which the depth of the two subtrees of every node never
# differ by more than 1.
# 
# 
# Example 1:
# 
# Given the following tree [3,9,20,null,null,15,7]:
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# Return true.
# 
# Example 2:
# 
# Given the following tree [1,2,2,3,3,null,null,4,4]:
# 
# 
# ⁠      1
# ⁠     / \
# ⁠    2   2
# ⁠   / \
# ⁠  3   3
# ⁠ / \
# ⁠4   4
# 
# 
# Return false.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def isBalanced(self, root: TreeNode) -> bool:
    """
    def isLeaf(self, node):
        if not node.left and not node.right:
            return True
        return False

    def hasGrandChild(self, node):
        if self.isLeaf(node):
            return False
        if node.left:
            if not self.isLeaf(node.left):
                return True
        if node.right:
            if not self.isLeaf(node.right):
                
                return True
        

    def isBalanced(self, root):
        if not root or self.isLeaf(root):
            return True

        def recur(node):
            print(node.val)
            if self.isLeaf(node):
                return True
            elif node.left and not node.right:
                if not self.isLeaf(node.left):
                    return False
                else:
                    return True
            elif node.right and not node.left:
                if not self.isLeaf(node.right):
                    return False
                else:
                    return True
            else:
                if self.isLeaf(node.right) and self.hasGrandChild(node.left):
                    return False
                elif self.isLeaf(node.left) and self.hasGrandChild(node.right):
                    return False
                else:
                    self.stack.append(node.right)
                    self.stack.append(node.left)
                    return True
                    

       
        
        self.stack = [root]
        while self.stack:
            if not recur(self.stack.pop()):
                return False
        return True
    """
    def isBalanced(self, root):
        def dfsHeight(node):
            if not node:
                return 0
        
            leftHeight = dfsHeight(node.left)
            if leftHeight == -1:
                return -1
            rightHeight = dfsHeight(node.right)
            if rightHeight == -1:
                return -1
        
            if abs(leftHeight - rightHeight) > 1:
                return -1
            return max(leftHeight, rightHeight) + 1
    

        return dfsHeight(root) != -1
        # recur(root)
       






# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# t = TreeNode(1)
# t.level = 10
# print(t.level)




























        
