#
# @lc app=leetcode id=965 lang=python3
#
# [965] Univalued Binary Tree
#
# https://leetcode.com/problems/univalued-binary-tree/description/
#
# algorithms
# Easy (66.90%)
# Total Accepted:    36.1K
# Total Submissions: 53.9K
# Testcase Example:  '[1,1,1,1,1,null,1]'
#
# A binary tree is univalued if every node in the tree has the same value.
# 
# Return true if and only if the given tree is univalued.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,1,1,1,1,null,1]
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: [2,2,2,5,2]
# Output: false
# 
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the given tree will be in the range [1, 100].
# Each node's value will be an integer in the range [0, 99].
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
    # def isUnivalTree(self, root: TreeNode) -> bool:
    def isUnivalTree(self, root):
        self.q = [root]
        self.value = root.val
        def recur(node):
            if node.val != self.value:
                return False
            else:
                if node.right:
                    self.q.insert(0, node.right)
                if node.left:
                    self.q.insert(0, node.left)
        while self.q:
            res = recur(self.q.pop(0))
            if res != None:
                if res == False:
                    return False
        return True


























