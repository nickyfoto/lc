#
# @lc app=leetcode id=889 lang=python3
#
# [889] Construct Binary Tree from Preorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/
#
# algorithms
# Medium (61.98%)
# Total Accepted:    20.9K
# Total Submissions: 33.7K
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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
    def constructFromPrePost2(self, pre, post):


        pre_copy = pre.copy()
        post_copy = post.copy()
        # root = buildRoot([1,2,3,4,5,6,7])
        # print('my_root=', root)

        my_pre, my_post = [], []

        def dfs(node):
            if node:
                my_pre.append(node.val)
                dfs(node.left)
                dfs(node.right)
                my_post.append(node.val)
        # dfs(root)
        # print('my_pre=', my_pre)
        # print('my_post=', my_post)
        # my_pre, my_post = [], []
        
        # root = TreeNode(pre.pop(0))
        # post.pop()
        q = []
        
        def build_dfs(pre, post, child):
            if pre and post:
                # print('input=', pre, post, child)
                if not child:
                    node = TreeNode(pre.pop(0))
                    post.pop()
                    pre, post, node.left = build_dfs(pre, post, 'left')
                    # print(pre, post, q)
                    while q and post[0] == q[0]:
                        post.pop(0)
                        q.pop(0)

                    pre, post, node.right = build_dfs(pre, post, 'right')
                    return pre, post, node
                else:
                    if child == 'left':
                        # print(pre, post)
                        if pre[0] == post[-1]:
                            node = TreeNode(pre.pop(0))
                            
                            post.pop()
                            pre, post, node.left = build_dfs(pre, post, 'left')
                            pre, post, node.right = build_dfs(pre, post, 'right')
                            return pre, post, node

                        elif pre[0] != post[0]:
                            node = TreeNode(pre.pop(0))
                            q.append(node.val)
                            print('here', node.val, pre, post)
                            pre, post, node.left = build_dfs(pre, post, 'left')
                            if pre and post and pre[0] == post[0]:
                                pre, post, node.right = build_dfs(pre, post, 'right')
                            return pre, post, node
                        else:
                            node = TreeNode(pre.pop(0))
                            post.pop(0)
                            return pre, post, node
                    elif child == 'right':
                        # print(pre, post, q)
                        if pre[0] != post[0]:
                            node = TreeNode(post.pop())
                            pre.pop(0)
                            pre, post, node.left = build_dfs(pre, post, 'left')
                            pre, post, node.right = build_dfs(pre, post, 'right')
                            return pre, post, node
                        else:
                            node = TreeNode(pre.pop(0))
                            post.pop(0)
                            return pre, post, node
            else:
                return pre, post, None

                        
        pre, post, root = build_dfs(pre, post, child=None)

        dfs(root)
        print('my_pre=', my_pre == pre_copy)
        print('my_post=', my_post == post_copy)

        return root



    def constructFromPrePost(self, pre, post):
        if not pre: 
            return None
        root = TreeNode(pre[0])
        if len(pre) == 1: 
            return root

        L = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:L+1], post[:L])
        root.right = self.constructFromPrePost(pre[L+1:], post[L:-1])
        return root


from tn import buildRoot, TreeNode
s = Solution()
pre = [1,2,4,5,3,6,7]
post = [4,5,2,6,7,3,1]
# print(s.constructFromPrePost(pre, post))






# pre = [2,1,3]
# post = [3,1,2]
# print(s.constructFromPrePost(pre, post))











        
