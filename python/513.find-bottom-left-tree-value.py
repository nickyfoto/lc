#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#
# https://leetcode.com/problems/find-bottom-left-tree-value/description/
#
# algorithms
# Medium (59.08%)
# Total Accepted:    77.5K
# Total Submissions: 131.3K
# Testcase Example:  '[2,1,3]'
#
# 
# Given a binary tree, find the leftmost value in the last row of the tree. 
# 
# 
# Example 1:
# 
# Input:
# 
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# 
# Output:
# 1
# 
# 
# 
# ⁠ Example 2: 
# 
# Input:
# 
# ⁠       1
# ⁠      / \
# ⁠     2   3
# ⁠    /   / \
# ⁠   4   5   6
# ⁠      /
# ⁠     7
# 
# Output:
# 7
# 
# 
# 
# Note:
# You may assume the tree (i.e., the given root node) is not NULL.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def findBottomLeftValue(self, root: TreeNode) -> int:
    def findBottomLeftValue(self, root):
        # def bfs(node):
        q = [[root]]
        qq = [[root.val]]
        while q:
            l = q.pop(0)
            # print(n.val)
            n_temp = []
            val_temp = []
            for n in l:
                if n.left:
                    # q.append(n.left)
                    n_temp.append(n.left)
                    val_temp.append(n.left.val)
                if n.right:
                    # q.append(n.right)
                    n_temp.append(n.right)
                    val_temp.append(n.right.val)
            if n_temp:
                q.append(n_temp)
                qq.append(val_temp)
        # print(qq)
        return qq[-1][0]