#
# @lc app=leetcode id=919 lang=python3
#
# [919] Complete Binary Tree Inserter
#
# https://leetcode.com/problems/complete-binary-tree-inserter/description/
#
# algorithms
# Medium (55.67%)
# Total Accepted:    11.1K
# Total Submissions: 20K
# Testcase Example:  '["CBTInserter","insert","get_root"]\n[[[1]],[2],[]]'
#
# A complete binary tree is a binary tree in which every level, except possibly
# the last, is completely filled, and all nodes are as far left as possible.
# 
# Write a data structure CBTInserter that is initialized with a complete binary
# tree and supports the following operations:
# 
# 
# CBTInserter(TreeNode root) initializes the data structure on a given tree
# with head node root;
# CBTInserter.insert(int v) will insert a TreeNode into the tree with value
# node.val = v so that the tree remains complete, and returns the value of the
# parent of the inserted TreeNode;
# CBTInserter.get_root() will return the head node of the tree.
# 
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
# Output: [null,1,[1,2]]
# 
# 
# 
# Example 2:
# 
# 
# Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs =
# [[[1,2,3,4,5,6]],[7],[8],[]]
# Output: [null,3,4,[1,2,3,4,5,6,7,8]]
# 
# 
# 
# 
# 
# Note:
# 
# 
# The initial given tree is complete and contains between 1 and 1000 nodes.
# CBTInserter.insert is called at most 10000 times per test case.
# Every value of a given or inserted node is between 0 and 5000.
# 
# 
# 
# 
# 
# 
# 
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

class CBTInserter:

    # def __init__(self, root: TreeNode):
    def __init__(self, root):
        self.root = root

    def _insert(self, nodes, v):
        next_nodes = []
        for node in nodes:
            if not node.left:
                node.left = TreeNode(v)
                return node
            elif not node.right:
                node.right = TreeNode(v)
                return node
            else:
                next_nodes.append(node.left)
                next_nodes.append(node.right)
        return self._insert(next_nodes, v)

    def insert(self, v: int) -> int:
        return self._insert([self.root], v).val
        # if inserted:
            # return parent.val

    # def get_root(self) -> TreeNode:
    def get_root(self):
        return self.root

# from tn import TreeNode, buildRoot
# # Your CBTInserter object will be instantiated and called as such:
# l = [1]
# root = buildRoot(l)
# obj = CBTInserter(root)
# v = 2
# param_1 = obj.insert(v)
# print(param_1 == 1) # 1
# param_2 = obj.get_root()
# print(param_2)


# l = [1,2,3,4,5,6]

# root = buildRoot(l)
# obj = CBTInserter(root)

# v = 7
# param_1 = obj.insert(v)
# print(param_1 == 3) # 3

# v = 8
# param_1 = obj.insert(v)
# print(param_1 == 4)


# param_2 = obj.get_root()
# print(param_2)


