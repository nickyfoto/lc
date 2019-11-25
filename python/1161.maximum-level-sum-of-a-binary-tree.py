#
# @lc app=leetcode id=1161 lang=python3
#
# [1161] Maximum Level Sum of a Binary Tree
#
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/
#
# algorithms
# Medium (73.47%)
# Total Accepted:    7.4K
# Total Submissions: 10K
# Testcase Example:  '[1,7,0,7,-8,null,null]'
#
# Given the root of a binary tree, the level of its root is 1, the level of its
# children is 2, and so on.
# 
# Return the smallest level X such that the sum of all the values of nodes at
# level X is maximal.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [1,7,0,7,-8,null,null]
# Output: 2
# Explanation: 
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the given tree is between 1 and 10^4.
# -10^5 <= node.val <= 10^5
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
    # def maxLevelSum(self, root: TreeNode) -> int:
    def maxLevelSum(self, root):
        

        res = [root.val]

        q = [[root]]
        while q:
            l = q.pop(0)
            children = []
            for n in l:
                if n.left:
                    children.append(n.left)
                if n.right:
                    children.append(n.right)
            if children:
                res.append(sum([c.val for c in children]))
                q.append(children)
        
        return res.index(max(res)) + 1

        # return max_sum
























