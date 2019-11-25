#
# @lc app=leetcode id=1028 lang=python3
#
# [1028] Recover a Tree From Preorder Traversal
#
# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/description/
#
# algorithms
# Hard (69.42%)
# Total Accepted:    10.7K
# Total Submissions: 15.5K
# Testcase Example:  '"1-2--3--4-5--6--7"'
#
# We run a preorder depth first search on the root of a binary tree.
# 
# At each node in this traversal, we output D dashes (where D is the depth of
# this node), then we output the value of this node.  (If the depth of a node
# is D, the depth of its immediate child is D+1.  The depth of the root node is
# 0.)
# 
# If a node has only one child, that child is guaranteed to be the left child.
# 
# Given the output S of this traversal, recover the tree and return its
# root.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: "1-2--3--4-5--6--7"
# Output: [1,2,5,3,4,6,7]
# 
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: "1-2--3---4-5--6---7"
# Output: [1,2,5,3,null,6,null,4,null,7]
# 
# 
# 
# 
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: "1-401--349---90--88"
# Output: [1,401,null,349,88,90]
# 
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the original tree is between 1 and 1000.
# Each node will have a value between 1 and 10^9.
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
    # def recoverFromPreorder(self, S: str) -> TreeNode:
    def recoverFromPreorder(self, S: str):
        if not S:
            return None

        D = 0
        l = []
        s = list(S)
        # print(s)

        def build(node, l, level):
            if not node:
                if l:
                    if l[0] != '-':

                        n = ""
                        while l and l[0] != '-':
                            n += l.pop(0)
                        node = TreeNode(int(n))
                        l, node.left = build(node.left, l, level+1)
                        l, node.right = build(node.right, l, level+1)
                        return l, node
                    else:
                        # print('here', node, l, D)
                        c = 0
                        while l[0] == '-':
                            l.pop(0)
                            c += 1
                        # print('c=', c)
                        if c == level:
                            # print('here')

                            n = ""
                            while l and l[0] != '-':
                                n += l.pop(0)
                            node = TreeNode(int(n))

                            
                            # print(node.val, 'D=', D, 'c=', c, l)
                            l, node.left = build(node.left, l, level+1)
                            l, node.right = build(node.right, l, level+1)
                            return l, node
                        else:
                            for i in range(c):
                                l.insert(0, '-')
                            # print(node, l, D)
                            return l, None
                            # todo
                else:
                    # print(node, level)
                    return l, None
                    # todo
            else:
                todo





        l, root = build(None, s, 0)

        # print(root)

        return root

from tn import buildRoot, TreeNode

s = Solution()
S = "1-2--3--4-5--6--7"
print(s.recoverFromPreorder(S))

S = "1-2--3---4-5--6---7"
print(s.recoverFromPreorder(S))


S = "1-401--349---90--88"
print(s.recoverFromPreorder(S))

