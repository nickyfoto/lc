#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (43.53%)
# Total Accepted:    261K
# Total Submissions: 599.3K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its zigzag level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [20,9],
# ⁠ [15,7]
# ]
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
    # def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        level = 0
        q = [[root]]
        res = []
        while q:
            nodes = q.pop(0)
            if level % 2 == 0:
                res.append([n.val for n in nodes])
            else:
                res.append([n.val for n in nodes][::-1])
            level += 1
            new_nodes = []
            for n in nodes:
                if n.left:
                    new_nodes.append(n.left)
                if n.right:
                    new_nodes.append(n.right)
            if new_nodes:
                q.append(new_nodes)

        return res



s = Solution()
from tn import null, buildRoot
l = [3,9,20,null,null,15,7]
root = buildRoot(l)
print(s.zigzagLevelOrder(root))


