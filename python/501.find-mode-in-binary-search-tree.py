#
# @lc app=leetcode id=501 lang=python3
#
# [501] Find Mode in Binary Search Tree
#
# https://leetcode.com/problems/find-mode-in-binary-search-tree/description/
#
# algorithms
# Easy (39.60%)
# Total Accepted:    59.5K
# Total Submissions: 149.6K
# Testcase Example:  '[1,null,2,2]'
#
# Given a binary search tree (BST) with duplicates, find all the mode(s) (the
# most frequently occurred element) in the given BST.
# 
# Assume a BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys less than or equal
# to the node's key.
# The right subtree of a node contains only nodes with keys greater than or
# equal to the node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# 
# For example:
# Given BST [1,null,2,2],
# 
# 
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  2
# 
# 
# 
# 
# return [2].
# 
# Note: If a tree has more than one mode, you can return them in any order.
# 
# Follow up: Could you do that without using any extra space? (Assume that the
# implicit stack space incurred due to recursion does not count).
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# a = [1,1,1,2,2,2,3,3,3,4]
from collections import Counter
# c = Counter(a)
# print(c.most_common(1))

class Solution:
    # def findMode(self, root: TreeNode) -> List[int]:
    def findMode(self, root):
        if not root:
            return []
        self.l = []
        def dfs(node):
            self.l.append(node.val)
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
        dfs(root)
        # self.l.sort()
        # print(self.l)
        c = Counter(self.l).most_common() 
        return [x[0] for x in c if x[1] == c[0][1]]
        # n = len(self.l)
        # if n % 2 == 0:
        #     return self.l[n//2-1:n//2+1]
        # else:
        #     return [self.l[n//2]]


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
# null = None
# s = Solution()
# l = [1,null,2,2]
# root = buildRoot(l)
# print(s.findMode(root))



# a = [1,1,1,2,2,2,3,3,3,4]
# from collections import Counter
# c = Counter(a)
# print(c.most_common(1))