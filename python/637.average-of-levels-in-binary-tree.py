#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
#
# https://leetcode.com/problems/average-of-levels-in-binary-tree/description/
#
# algorithms
# Easy (58.87%)
# Total Accepted:    81.3K
# Total Submissions: 137.8K
# Testcase Example:  '[3,9,20,15,7]'
#
# Given a non-empty binary tree, return the average value of the nodes on each
# level in the form of an array.
# 
# Example 1:
# 
# Input:
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# Output: [3, 14.5, 11]
# Explanation:
# The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level
# 2 is 11. Hence return [3, 14.5, 11].
# 
# 
# 
# Note:
# 
# The range of node's value is in the range of 32-bit signed integer.
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
    # def averageOfLevels(self, root: TreeNode) -> List[float]:
    def averageOfLevels(self, root: TreeNode):
        self.res = []
        self.q = [[root]]
        def bfs(nodeList):
            self.res.append(sum([n.val for n in nodeList]) / len(nodeList))
            children = []
            for n in nodeList:
                if n.left:
                    children.append(n.left)
                if n.right:
                    children.append(n.right)
            if children:
                self.q.append(children)
        while self.q:
            bfs(self.q.pop(0))
        return self.res


