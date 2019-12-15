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
# from lcpy import List, TreeNode, build_root
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:

        

        if not pre: return None
        root = TreeNode(pre[0])
        if len(pre) == 1: return root

        L = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:L+1], post[:L])
        root.right = self.constructFromPrePost(pre[L+1:], post[L:])
        return root


        # def recur_build_left(pre, post):
        #     """
            
        #     """
        #     print('build_left', pre, post)
        #     if pre and post:
        #         if pre[0] == post[0]:
        #             pr = pre.pop(0)
        #             post.pop(0)
        #             node = TreeNode(pr)
        #         else:
        #             stack = []
        #             while pre[0] != post[-1]:
        #                 stack.insert(0, post.pop())
        #             pr = pre.pop(0)
        #             post.pop()
        #             node = TreeNode(pr)
        #             if stack:
        #                 post = post + stack
        #         return pre, post, node
        #     else:
        #         return pre, post, None

        # def recur_build_right(pre, post):
        #     print('build_right', pre, post)
        #     if pre and post:
        #         if pre[-1] == post[-1]:
        #             pr = pre.pop()
        #             post.pop()
        #             node = TreeNode(pr)
        #             return pre, post, node
        #         else:
        #             stack = []
        #             while post[-1] != pre[-1]:
        #                 stack.append(pre.pop())
        #             pr = pre.pop()
        #             post.pop()
        #             node = TreeNode(pr)
        #             if stack:
        #                 pre = pre + stack
        #             return pre, post, node

        #     else:
        #         return pre, post, None

        # def recur_build(pre, post, node):
        #     """
        #     Given a node
        #     update its left and right node
        #     """
        #     print('pre=', pre, 'post=', post, 'node=', node)
        #     if not pre and not post:
        #         return pre, post, node
        #     else:
        #         if not node:
        #             pr = pre.pop(0)
        #             post.pop()
        #             node = TreeNode(pr)
                
        #         pre, post, node.left = recur_build_left(pre, post)
        #         pre, post, node.right = recur_build_right(pre, post)
        #         print('here', pre, post, node)
        #         if node.left:
        #             pre, post, node.left = recur_build(pre, post, node.left)
        #         if node.right:
        #             pre, post, node.right = recur_build(pre, post, node.right)
        #         # print('here2', pre, post, node)
        #         return pre, post, node

        # pre, post, node = recur_build(pre, post, node=None)
        # print('final', pre, post)
        # return node
# @lc code=end
