#
# @lc app=leetcode id=889 lang=python3
#
# [889] Construct Binary Tree from Preorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/
#
# algorithms
# Medium (63.24%)
# Likes:    548
# Dislikes: 36
# Total Accepted:    24.6K
# Total Submissions: 38.9K
# Testcase Example:  '[1,2,4,5,3,6,7]\n[4,5,2,6,7,3,1]'
#
# Return any binary tree that matches the given preorder and postorder
# traversals.
# 
# Values in the traversals pre and post are distinct positive integers.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= pre.length == post.length <= 30
# pre[] and post[] are both permutations of 1, 2, ..., pre.length.
# It is guaranteed an answer exists. If there exists multiple answers, you can
# return any of them.
# 
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
from lcpy import List, TreeNode
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        pass
# @lc code=end
