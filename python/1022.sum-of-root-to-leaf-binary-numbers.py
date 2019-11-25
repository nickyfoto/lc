#
# @lc app=leetcode id=1022 lang=python3
#
# [1022] Sum of Root To Leaf Binary Numbers
#
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/
#
# algorithms
# Easy (54.95%)
# Total Accepted:    12.9K
# Total Submissions: 23K
# Testcase Example:  '[1,0,1,0,1,0,1]'
#
# Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path
# represents a binary number starting with the most significant bit.  For
# example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent
# 01101 in binary, which is 13.
# 
# For all leaves in the tree, consider the numbers represented by the path from
# the root to that leaf.
# 
# Return the sum of these numbers.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the tree is between 1 and 1000.
# node.val is 0 or 1.
# The answer will not exceed 2^31 - 1.
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
    # def sumRootToLeaf(self, root: TreeNode) -> int:
    def sumRootToLeaf(self, root):
        l = self.binaryTreePaths(root)
        return sum(map(lambda x: int(x, 2), l))
    def binaryTreePaths(self, root):
        if not root:
            return []
        self.stack = [[root, []]]
        self.res = []
        def dfs(node, path):
            path.append(str(node.val))
            if not node.left and not node.right:
                self.res.append("".join(path))
            else:
                if node.right:
                    self.stack.append([node.right, path])
                if node.left:
                    self.stack.append([node.left, path])
                    
        while self.stack:
            node, path = tuple(self.stack.pop())
            dfs(node, path.copy())
        return self.res        



