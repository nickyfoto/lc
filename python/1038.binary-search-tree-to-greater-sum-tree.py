#
# @lc app=leetcode id=1038 lang=python3
#
# [1038] Binary Search Tree to Greater Sum Tree
#
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/
#
# algorithms
# Medium (78.52%)
# Total Accepted:    17.8K
# Total Submissions: 22.7K
# Testcase Example:  '[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]'
#
# Given the root of a binary search tree with distinct values, modify it so
# that every node has a new value equal to the sum of the values of the
# original tree that are greater than or equal to node.val.
# 
# As a reminder, a binary search tree is a tree that satisfies these
# constraints:
# 
# 
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the tree is between 1 and 100.
# Each node will have value between 0 and 100.
# The given tree is a binary search tree.
# 
# 
# 
# 
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
    # def bstToGst(self, root: TreeNode) -> TreeNode:
    def bstToGst(self, root):

        def isLeaf(node):
            return not node.left and not node.right
        
        def dfs_right(node):
            if node:
                print(node.val)
                dfs_right(node.right)
                dfs_right(node.left)

        

        def dfs_update(node, right_max):
            if node:
                # print(node.val)
                if isLeaf(node):
                    node.val += right_max
                    return node
                else:
                    if node.right:
                        # print(node.val)
                        right_max = dfs_update(node.right, right_max).val
                        # print('node.val=', node.val, 'right_max =', right_max)
                    node.val += right_max
                    right_max = node.val
                    if node.left:
                        if isLeaf(node.left):
                            node.left.val += node.val
                            return node.left
                        else:
                            # print('here', node.val)
                            return dfs_update(node.left, right_max)
                    else:
                        return node
                       
        dfs_update(root, 0)
        
        # dfs_right(root)
        # print(root)
        return root


        




# from tn import buildRoot, null
# l = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
# l = [3,2,4,1]
# root = buildRoot(l)
# # # print(root)
# s = Solution()
# print(s.bstToGst(root))