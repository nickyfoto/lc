#
# @lc app=leetcode id=865 lang=python3
#
# [865] Smallest Subtree with all the Deepest Nodes
#
# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/
#
# algorithms
# Medium (57.63%)
# Total Accepted:    23.4K
# Total Submissions: 40.6K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]'
#
# Given a binary tree rooted at root, the depth of each node is the shortest
# distance to the root.
# 
# A node is deepest if it has the largest depth possible among any node in the
# entire tree.
# 
# The subtree of a node is that node, plus the set of all descendants of that
# node.
# 
# Return the node with the largest depth such that it contains all the deepest
# nodes in its subtree.
# 
# 
# 
# Example 1:
# 
# 
# Input: [3,5,1,6,2,0,8,null,null,7,4]
# Output: [2,7,4]
# Explanation:
# 
# 
# 
# We return the node with value 2, colored in yellow in the diagram.
# The nodes colored in blue are the deepest nodes of the tree.
# The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the
# given tree.
# The output "[2, 7, 4]" is a serialization of the subtree rooted at the node
# with value 2.
# Both the input and output have TreeNode type.
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the tree will be between 1 and 500.
# The values of each node are unique.
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution:
    # def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
    def subtreeWithAllDeepest(self, root):


        def bfs(root):
            root.parent = None
            q = [[root]]
            depth = 0
            while q:
                nodes = q.pop(0)
                new_nodes = []
                for node in nodes:
                    node.depth = depth
                    # print(node.val, 'depth =', node.depth, 'parent = ', node.parent)
                    # if node.parent:
                    if node.left:
                        node.left.parent = node
                        new_nodes.append(node.left)
                    if node.right:
                        node.right.parent = node
                        new_nodes.append(node.right)
                if new_nodes:
                    q.append(new_nodes)
                depth += 1
        # bfs(root)
        # self.pre = 0
        # self.post = 0
        root.parent = None
        d = defaultdict(list)
        def dfs(node, depth):
            if node:
                node.depth = depth
                # node.pre = self.pre
                # self.pre += 1
                d[depth].append(node)
                depth += 1
                # print(node.val, 'depth = ', depth)
                # print(node.val, 'depth = ', node.depth, 'parent =', node.parent)
                if node.left:
                    node.left.parent = node
                if node.right:
                    node.right.parent = node
                dfs(node.left, depth)
                dfs(node.right, depth)
                # node.post = self.post
                # self.post += 1
                # print(node.val, 'post = ', node.post)
        dfs(root, depth=0)
        # print(d)
        # print(root == root)
        nodes = d[max(d.keys())]
        if len(nodes) == 1:
            return nodes[0]
        # print(nodes)
        parents = [n.parent for n in nodes]
        while not all([p == parents[0] for p in parents]):
            parents = [n.parent for n in parents]

        # print(parents[0])
        if not parents[0]:
            return root
        return parents[0]




# s = Solution()
# from tn import buildRoot, null
# l = [3,5,1,6,2,0,8,null,null,7,4]
# root = buildRoot(l)
# print(s.subtreeWithAllDeepest(root))





# l = [1]
# root = buildRoot(l)
# print(s.subtreeWithAllDeepest(root))



# l = [0,1,3,null,2]
# root = buildRoot(l)
# print(s.subtreeWithAllDeepest(root))











        
