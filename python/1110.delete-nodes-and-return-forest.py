#
# @lc app=leetcode id=1110 lang=python3
#
# [1110] Delete Nodes And Return Forest
#
# https://leetcode.com/problems/delete-nodes-and-return-forest/description/
#
# algorithms
# Medium (63.14%)
# Total Accepted:    10.5K
# Total Submissions: 16.6K
# Testcase Example:  '[1,2,3,4,5,6,7]\n[3,5]'
#
# Given the root of a binary tree, each node in the tree has a distinct value.
# 
# After deleting all nodes with a value in to_delete, we are left with a forest
# (a disjoint union of trees).
# 
# Return the roots of the trees in the remaining forest.  You may return the
# result in any order.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the given tree is at most 1000.
# Each node has a distinct value between 1 and 1000.
# to_delete.length <= 1000
# to_delete contains distinct values between 1 and 1000.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
    def delNodes2(self, root, to_delete):
        
        def isLeaf(node):
            return not node.left and not node.right
        
        def delete(node, v):
            if node.val == v:
                if node.left:
                    forest.append(node.left)
                if node.right:
                    forest.append(node.right)
                return True, None
            else:
                if isLeaf(node):
                    return False, node
                deleted = False
                if node.left:
                    deleted, node.left = delete(node.left, v)
                if not deleted:
                    if node.right:
                        deleted, node.right = delete(node.right, v)
                # forest.append(node)
                return deleted, node
        

        forest = [root]
        while to_delete:
            v = to_delete.pop(0)
            deleted = False
            while not deleted:
                node = forest.pop(0)
                deleted, node = delete(node, v)
                if node:
                    forest.append(node)
        
        # for f in forest:
        #     print(f)
                # break
        return forest


    def delNodes(self, root, to_delete):

        # dfs(root)

        forest = []
        def delete(node):    
            if node.val in to_delete:
                if node.left:
                    l = delete(node.left)
                    if l:
                        forest.append(l)
                if node.right:
                    r = delete(node.right)
                    if r:
                        forest.append(r)
                return None
            else:
                if node.left:
                    node.left = delete(node.left)
                if node.right:
                    node.right = delete(node.right)
                return node
        
        root = delete(root)
        if root:
            forest.insert(0, root)
        # for f in forest:
            # print(f)
        return forest

# s = Solution()
# from tn import TreeNode, buildRoot, null
# root = [1,2,3,4,5,6,7]
# to_delete = [3,5]
# root = buildRoot(root)
# print(s.delNodes(root, to_delete))

# root = [1,2,4,null,3]
# to_delete = [3]
# root = buildRoot(root)
# print(s.delNodes(root, to_delete))
