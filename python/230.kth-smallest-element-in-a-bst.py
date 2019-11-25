#
# @lc app=leetcode id=230 lang=python3
#
# [230] Kth Smallest Element in a BST
#
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (53.03%)
# Total Accepted:    249.6K
# Total Submissions: 470.6K
# Testcase Example:  '[3,1,4,null,2]\n1'
#
# Given a binary search tree, write a function kthSmallest to find the kth
# smallest element in it.
# 
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
# 
# Example 1:
# 
# 
# Input: root = [3,1,4,null,2], k = 1
# ⁠  3
# ⁠ / \
# ⁠1   4
# ⁠ \
# 2
# Output: 1
# 
# Example 2:
# 
# 
# Input: root = [5,3,6,2,4,null,null,1], k = 3
# ⁠      5
# ⁠     / \
# ⁠    3   6
# ⁠   / \
# ⁠  2   4
# ⁠ /
# ⁠1
# Output: 3
# 
# 
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to
# find the kth smallest frequently? How would you optimize the kthSmallest
# routine?
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def kthSmallest(self, root: TreeNode, k: int) -> int:
    def kthSmallest(self, root, k):

        self.left = []
        self.right = []
        self.res = None
        def dfs(node):
            if node:
                if node.val < root.val:
                    self.left.append(node.val)
                elif node.val > root.val:
                    if k <= len(self.left):
                        self.res = sorted(self.left)[k-1]
                        return
                    if not self.res:
                        self.right.append(node.val)
                    
                # print(node.val, self.count)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        # print(res)
        if self.res:
            return self.res
        else:
            self.res = self.left + [root.val] + self.right
            return sorted(self.res)[k-1]
        # print(self.left, self.right)

# s = Solution()
# from tn import TreeNode, null, buildRoot
# root = [5,3,6,2,4,null,null,1]
# k = 3
# root = buildRoot(root)
# print(s.kthSmallest(root, k))


# root = [3,1,4,null,2]
# k = 1
# root = buildRoot(root)
# print(s.kthSmallest(root, k))


# root = [1]
# k = 1

# root = buildRoot(root)
# print(s.kthSmallest(root, k))













        
