#
# @lc app=leetcode id=203 lang=python3
#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (35.86%)
# Total Accepted:    231.9K
# Total Submissions: 644.8K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Remove all elements from a linked list of integers that have value val.
# 
# Example:
# 
# 
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def removeElements(self, head: ListNode, val: int) -> ListNode:
    def removeElements(self, head, val):
        # if not head:
            # return None
        while head and head.val == val:
            head = head.next
        if not head:
            return None
        n = head
        while n and n.next:
            # print(n.val)
            while n.next.val == val:
                if n.next.next:
                    n.next = n.next.next
                else:
                    n.next = None
                    break
            # else:
            n = n.next
        return head


