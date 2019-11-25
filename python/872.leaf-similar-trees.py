#
# @lc app=leetcode id=872 lang=python3
#
# [872] Leaf-Similar Trees
#
# https://leetcode.com/problems/leaf-similar-trees/description/
#
# algorithms
# Easy (63.33%)
# Total Accepted:    46.5K
# Total Submissions: 73.3K
# Testcase Example:  '[3,5,1,6,2,9,8,null,null,7,4]\n[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]'
#
# Consider all the leaves of a binary tree.  From left to right order, the
# values of those leaves form a leaf value sequence.
# 
# 
# 
# For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9,
# 8).
# 
# Two binary trees are considered leaf-similar if their leaf value sequence is
# the same.
# 
# Return true if and only if the two given trees with head nodes root1 and
# root2 are leaf-similar.
# 
# 
# 
# Note:
# 
# 
# Both of the given trees will have between 1 and 100 nodes.
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
    # def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
    def leafSimilar(self, root1, root2):
        
        # self.q = []
        # def dfs(node):
        #     if not node.left and not node.right:
        #         self.q.append(node.val)
        #     else:
        #         if node.left:
        #             l = dfs(node.left)
        #             if l:
        #                 self.q.append(l)
        #         if node.right:
        #             r = dfs(node.right)
        #             if r:
        #                 self.q.append(r)
        # dfs(root2)
        # print(self.q)


        
        stack1 = [root1]
        stack2 = [root2]
        def dfs(node, stack):
            if not node.left and not node.right:
                return node.val
            else:
                if node.right:
                    stack.insert(0, node.right)
                if node.left:
                    stack.insert(0, node.left)
        q1 = []
        q2 = []
        while stack1 or stack2:
            if stack1:
                l1 = dfs(stack1.pop(0), stack1)
                if l1:
                    q1.append(l1)
            if stack2:
                l2 = dfs(stack2.pop(0), stack2)
                if l2:
                    q2.append(l2)
            if q1 and q2 and len(q1) == len(q2):
                if q1[-1] != q2[-1]:
                    return False
        if q1 != q2:
            return False
        return True
        
































        
