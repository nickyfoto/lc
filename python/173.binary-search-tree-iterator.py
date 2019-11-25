#
# @lc app=leetcode id=173 lang=python3
#
# [173] Binary Search Tree Iterator
#
# https://leetcode.com/problems/binary-search-tree-iterator/description/
#
# algorithms
# Medium (49.86%)
# Total Accepted:    221.2K
# Total Submissions: 442.5K
# Testcase Example:  '["BSTIterator","next","next","hasNext","next","hasNext","next","hasNext","next","hasNext"]\n[[[7,3,15,null,null,9,20]],[null],[null],[null],[null],[null],[null],[null],[null],[null]]'
#
# Implement an iterator over a binary search tree (BST). Your iterator will be
# initialized with the root node of a BST.
# 
# Calling next() will return the next smallest number in the BST.
# 
# 
# 
# 
# 
# 
# Example:
# 
# 
# 
# 
# BSTIterator iterator = new BSTIterator(root);
# iterator.next();    // return 3
# iterator.next();    // return 7
# iterator.hasNext(); // return true
# iterator.next();    // return 9
# iterator.hasNext(); // return true
# iterator.next();    // return 15
# iterator.hasNext(); // return true
# iterator.next();    // return 20
# iterator.hasNext(); // return false
# 
# 
# 
# 
# Note:
# 
# 
# next() and hasNext() should run in average O(1) time and uses O(h) memory,
# where h is the height of the tree.
# You may assume that next() call will always be valid, that is, there will be
# at least a next smallest number in the BST when next() is called.
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# from bst import TreeNode, root, root2

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.root = root

    def isLeaf(self, node):
        return not node.left and not node.right

    def _next(self, node):
        # if self.isLeaf(node):
        #     
        if not node.left:
            if node.right:
                val = node.val
                self.root = node.right
                return val
            else:
                val = node.val
                self.root = None
                return val
        # elif node.left:
        else:
            if self.isLeaf(node.left):
                val = node.left.val
                node.left = None
                return val
            else:
                if node.left.left:
                    return self._next(node.left)
                else:
                    val = node.left.val
                    node.left = node.left.right
                    return val
                

        # return self._next(node.left)
    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self._next(self.root)
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.root:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# print(obj.next())
# print(obj.next())
# print(obj.hasNext())
# print(obj.next())
# print(obj.hasNext())
# print(obj.next())
# print(obj.hasNext())
# print(obj.next())
# print(obj.hasNext())


# obj = BSTIterator(root2)
# print(obj.next())
# print(obj.next())
# print(obj.next())
# print(obj.next())