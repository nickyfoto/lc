#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#
# https://leetcode.com/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (41.78%)
# Total Accepted:    107K
# Total Submissions: 255.3K
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
# 
# Given two non-empty binary trees s and t, check whether tree t has exactly
# the same structure and node values with a subtree of s. A subtree of s is a
# tree consists of a node in s and all of this node's descendants. The tree s
# could also be considered as a subtree of itself.
# 
# 
# Example 1:
# 
# Given tree s:
# 
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# 
# Given tree t:
# 
# ⁠  4 
# ⁠ / \
# ⁠1   2
# 
# Return true, because t has the same structure and node values with a subtree
# of s.
# 
# 
# Example 2:
# 
# Given tree s:
# 
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# ⁠   /
# ⁠  0
# 
# Given tree t:
# 
# ⁠  4
# ⁠ / \
# ⁠1   2
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
    def equal(self, s, t):
        if not s and not t:
            return True
        elif not s and t:
            return False
        elif not t and s:
            return False
        elif self.isLeaf(s) and self.isLeaf(t):
            return s.val == t.val
        else:
            if self.isLeaf(s) and not self.isLeaf(t):
                return False
            elif not self.isLeaf(s) and self.isLeaf(t):
                return False
            else:
                if s.val != t.val:
                    return False
                else:
                    return self.equal(s.left, t.left) and self.equal(s.right, t.right)
    
    def isLeaf(self, node):
        return not node.left and not node.right

    # def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
    def isSubtree(self, s, t):
        
        
        def dfs(node, t):
            if self.equal(node, t):
                return True
            elif self.isLeaf(node) and self.isLeaf(t):
                return node.val == t.val
            else:
                if self.isLeaf(node) and not self.isLeaf(t):
                    return False
                elif node.left and node.right:
                    return dfs(node.left, t) or dfs(node.right, t)
                elif node.left and not node.right:
                    return dfs(node.left, t)
                else:
                    # print('here', node.val)
                    return dfs(node.right, t)
        # print(dfs(s, t))
        return dfs(s, t)

# null = None
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# def buildRoot(l):
#     root = TreeNode(l.pop(0))
#     temp = [root]
#     while temp:
#         # print(temp)
#         node = temp.pop(0)
#         if l:
#             p = l.pop(0)
#             if p == null:
#                 node.left = p
#             else:
#                 node.left = TreeNode(p)
#                 temp.append(node.left)
#         if l:
#             p = l.pop(0)
#             if p == null:
#                 node.right = p
#             else:
#                 node.right = TreeNode(p)
#                 temp.append(node.right)
#     return root

# l = [1,2,3]
# s = buildRoot(l)
# l = [1,2]
# t = buildRoot(l)
# S = Solution()
# print(S.isSubtree(s, t)== False)
# l = [1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,null,1,2]
# s = buildRoot(l)
# l = [1,null,1,null,1,null,1,null,1,null,1,2]
# t = buildRoot(l)
# print(S.isSubtree(s, t) == True)
