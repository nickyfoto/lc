#
# @lc app=leetcode id=236 lang=python3
#
# [236] Lowest Common Ancestor of a Binary Tree
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#
# algorithms
# Medium (42.53%)
# Likes:    3115
# Dislikes: 164
# Total Accepted:    412.6K
# Total Submissions: 953.4K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
# in the tree.
# 
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has both p
# and q as descendants (where we allow a node to be a descendant of itself).”
# 
# Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# 
# 
# Example 2:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant
# of itself according to the LCA definition.
# 
# 
# 
# 
# Note:
# 
# 
# All of the nodes' values will be unique.
# p and q are different and both values will exist in the binary tree.
# 
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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        ✔ Your runtime beats 23.52 % of python3 submissions
        ✔ Your memory usage beats 5.55 % of python3 submissions (29.1 MB)
        """
        self.preorder = 0
        found = set()
        post = []
        def dfs(node):
            if node:
                self.preorder += 1
                if node is p:
                    found.add(node)
                if node is q:
                    found.add(node)
                
                node.preorder = self.preorder
                dfs(node.left)
                dfs(node.right)
                node.postorder = len(post) + 1
                post.append(node)
        
        dfs(root)
        
        mn_preorder = [f.preorder for f in found]
        mx_postorder = [f.postorder for f in found]
        
        for node in post:
            if node.preorder <= min(mn_preorder) and node.postorder >= max(mx_postorder):
                return node

    def lowestCommonAncestor(self, root, p, q):
        """
        @ stefan
        ✔ Your runtime beats 6.8 % of python3 submissions
        ✔ Your memory usage beats 5.55 % of python3 submissions (39.1 MB)
        """
        if root in (None, p, q): return root
        l, r = (self.lowestCommonAncestor(subtree, p, q) for subtree in (root.left, root.right))
        return root if l and r else l or r


    def lowestCommonAncestor(self, root, p, q):
        """
        official answer
        """
        def recur(node):
            if not node: return False
            left = recur(node.left)
            right = recur(node.right)
            mid = node == p or node == q
            if mid + left + right >= 2:
                self.ans = node
            return mid or left or right
        self.ans = None
        recur(root)
        return self.ans

# @lc code=end
