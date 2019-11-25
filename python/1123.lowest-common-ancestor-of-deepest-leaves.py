#
# @lc app=leetcode id=1123 lang=python3
#
# [1123] Lowest Common Ancestor of Deepest Leaves
#
# https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/description/
#
# algorithms
# Medium (64.46%)
# Total Accepted:    6.8K
# Total Submissions: 10.5K
# Testcase Example:  '[1,2,3]'
#
# Given a rooted binary tree, return the lowest common ancestor of its deepest
# leaves.
# 
# Recall that:
# 
# 
# The node of a binary tree is a leaf if and only if it has no children
# The depth of the root of the tree is 0, and if the depth of a node is d, the
# depth of each of its children is d+1.
# The lowest common ancestor of a set S of nodes is the node A with the largest
# depth such that every node in S is in the subtree with root A.
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3]
# Output: [1,2,3]
# Explanation: 
# The deepest leaves are the nodes with values 2 and 3.
# The lowest common ancestor of these leaves is the node with value 1.
# The answer returned is a TreeNode object (not an array) with serialization
# "[1,2,3]".
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2,3,4]
# Output: [4]
# 
# 
# Example 3:
# 
# 
# Input: root = [1,2,3,4,5]
# Output: [2,4,5]
# 
# 
# 
# Constraints:
# 
# 
# The given tree will have between 1 and 1000 nodes.
# Each node of the tree will have a distinct value between 1 and 1000.
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
    # def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
    def lcaDeepestLeaves(self, root):
        # self.l_depth = 0
        # self.r_depth = 0
        def isLeaf(node):
            return not node.left and not node.right
        def recur(node, depth):
            if node:
                if isLeaf(node):
                    return depth, node
                depth += 1
                if node.left and node.right:
                    l, ln = recur(node.left, depth)
                    r, rn = recur(node.right, depth)
                    if l > r:
                        return l, ln
                    elif l == r:
                        return l, node
                    else:
                        return r, rn
                elif node.left and not node.right:
                    l, ln = recur(node.left, depth)
                    return l, ln
                else:
                    r, rn = recur(node.right, depth)
                    return r, rn

        return recur(root, 0)[1]

        
# s = Solution()
# from tn import buildRoot, null
# # l = [1,2,3]
# # l = [1,2,3,4]
# # l = [1,2,3,4,5]
# # l = [1,null,2,null,3,null,4,null,5]
# root = buildRoot(l)
# print(s.lcaDeepestLeaves(root))
