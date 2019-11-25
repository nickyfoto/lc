#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (42.85%)
# Total Accepted:    196.5K
# Total Submissions: 458.2K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
# Example:
# 
# 
# Given the sorted linked list: [-10,-3,0,5,9],
# 
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def sortedListToBST(self, head: ListNode) -> TreeNode:
    def sortedListToBST(self, head):
        if not head:
            return None
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l.sort()

        def build_balanced_bst(node, vals):
            mid = len(vals) // 2
            p = vals.pop(mid)
            left, right = vals[:mid], vals[mid:]
            node = TreeNode(p)
            if left:
                node.left = build_balanced_bst(node.left, left)
            if right:
                node.right = build_balanced_bst(node.right, right)
            return node
    
        return build_balanced_bst(node=None, vals=l)





s = Solution()
from linked_list import build_head
from tn import TreeNode
l = [-10,-3,0,5,9]
head =build_head(l)
print(s.sortedListToBST(head))



l = [0,1,2,3,4,5]

head =build_head(l)
print(s.sortedListToBST(head))

