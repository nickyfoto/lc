#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (58.09%)
# Total Accepted:    513.8K
# Total Submissions: 884.3K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [1,3,2]
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
    # def inorderTraversal(self, root: TreeNode) -> List[int]:
    def inorderTraversal(self, root):
        res = []
        def isLeaf(node):
            return not node.left and not node.right
        def recur(node):
            if node:
                if isLeaf(node):
                    res.append(node.val)
                    return
                if node.left:
                    recur(node.left)

                res.append(node.val)
                # print(node.val, res)
                if node.right:
                    recur(node.right)
        # recur(node.left)
        # res.append(root.val)
        recur(root)
        # print(res)
        return res

        
# from tn import buildRoot, null
# l = [1,null,2,3]
# root = buildRoot(l)
# s = Solution()
# print(s.inorderTraversal(root))
