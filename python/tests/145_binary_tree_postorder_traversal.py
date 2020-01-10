#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (51.72%)
# Likes:    1282
# Dislikes: 66
# Total Accepted:    317.6K
# Total Submissions: 614.2K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the postorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [3,2,1]
# 
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def postorderTraversal(self, root: TreeNode) -> List[int]:
    def postorderTraversal(self, root):
        res = []
        def dfs(node):
            if node:
                dfs(node.left)
                dfs(node.right)
                res.append(node.val)
                # print(node.val)
            # print(res)
        dfs(root)
        return res
# @lc code=end
