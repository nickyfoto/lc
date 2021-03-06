#
# @lc app=leetcode id=1302 lang=python3
#
# [1302] Deepest Leaves Sum
#
# https://leetcode.com/problems/deepest-leaves-sum/description/
#
# algorithms
# Medium (85.27%)
# Likes:    94
# Dislikes: 11
# Total Accepted:    8.1K
# Total Submissions: 9.5K
# Testcase Example:  '[1,2,3,4,5,null,6,7,null,null,null,null,8]'
#
# Given a binary tree, return the sum of values of its deepest leaves.
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is between 1 and 10^4.
# The value of nodes is between 1 and 100.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# from lcpy import TreeNode
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        res = 0
        q = [[root]]

        def is_not_leaf(node):
            return node.left is not None or node.right is not None

        while q:
            nodes = q.pop(0)
            l = []
            deepest_level = True
            for node in nodes:
                # print(node.val, 'here', is_not_leaf(node))
                if is_not_leaf(node):
                    deepest_level = False
                    res = 0
                    if node.left:
                        l.append(node.left)
                    if node.right:
                        l.append(node.right)
                else:
                    if deepest_level:
                        res += node.val
                    else:
                        res = 0
            if l:
                q.append(l)
        return res
# @lc code=end
