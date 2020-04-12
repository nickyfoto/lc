#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
# https://leetcode.com/problems/path-sum/description/
#
# algorithms
# Easy (37.91%)
# Total Accepted:    326K
# Total Submissions: 856K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
#
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given the below binary tree and sum = 22,
# 
# 
# ⁠     5
# ⁠    / \
# ⁠   4   8
# ⁠  /   / \
# ⁠ 11  13  4
# ⁠/  \      \
# 7    2      1
# 
# 
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    def hasPathSum(self, root, _sum):
        if not root:
            return False
        # self.target = sum
        self.stack = [[root, []]]

        def dfs(node, path):
            path.append(node.val)
            if not node.left and not node.right:
                if sum(path) == _sum:
                    return True
                # self.stack.append([node, path])
            else:
                if node.right:
                    self.stack.append([node.right, path])
                if node.left:
                    self.stack.append([node.left, path])

        while self.stack:
            node, path = tuple(self.stack.pop())
            # print(path)
            # if not node.left and not node.right and sum(path) == _sum:
                # print(sum(path))
                # return True
            if dfs(node, path.copy()):
                return True

        return False


    def hasPathSum(self, root, sum):
        if not root: return False
        sum -= root.val
        if not root.left and not root.right:
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)





















        
