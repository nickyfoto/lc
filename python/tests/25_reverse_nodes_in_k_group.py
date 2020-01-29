#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#
# https://leetcode.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (39.29%)
# Likes:    1645
# Dislikes: 327
# Total Accepted:    229.8K
# Total Submissions: 584.7K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, reverse the nodes of a linked list k at a time and
# return its modified list.
# 
# k is a positive integer and is less than or equal to the length of the linked
# list. If the number of nodes is not a multiple of k then left-out nodes in
# the end should remain as it is.
# 
# 
# 
# 
# Example:
# 
# Given this linked list: 1->2->3->4->5
# 
# For k = 2, you should return: 2->1->4->3->5
# 
# For k = 3, you should return: 3->2->1->4->5
# 
# Note:
# 
# 
# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be
# changed.
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# from lcpy import ListNode
class Solution:
    # def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
    def reverseKGroup(self, head, k):
        if not head:
            return None
        if k == 1:
            return head

        def recur(node):
            head = node
            stack = []
            i = 0
            while node and i < k:
                stack.append(node)
                node = node.next
                i += 1
            if i < k:
                return head
            rest = node
            new_head = ListNode(0)
            node = new_head
            while stack:
                n = stack.pop()
                n.next = None
                node.next = n
                node = node.next
            
            node.next = recur(rest)
            return new_head.next
        return recur(head)
        # print(h)
        # print(t)
        # print(r)
# @lc code=end
