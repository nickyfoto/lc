#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (46.18%)
# Total Accepted:    231.8K
# Total Submissions: 500.4K
# Testcase Example:  '[1,2,3,null,5]'
#
# Given a binary tree, return all root-to-leaf paths.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# 
# Input:
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# Output: ["1->2->5", "1->3"]
# 
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def binaryTreePaths(self, root: TreeNode) -> List[str]:
    def binaryTreePaths(self, root):
        if not root:
            return []
        self.stack = [[root, []]]
        self.res = []
        def dfs(node, path):
            # if not node:
                # return
            path.append(str(node.val))
            if not node.left and not node.right:
                # print(node.val, path)
                self.res.append("->".join(path))
                # print(self.res)
                # path = []
            else:
                if node.right:
                    self.stack.append([node.right, path])
                if node.left:
                    self.stack.append([node.left, path])
                    
        while self.stack:
            # print(self.stack)
            # for s in self.stack:
                # print(s[0].val, s[1])
            node, path = tuple(self.stack.pop())
            dfs(node, path.copy())
            # self.res.append(dfs(node, path))
        # dfs(root, [root.val], [root.val])
        # print(self.res)
        return self.res
        
