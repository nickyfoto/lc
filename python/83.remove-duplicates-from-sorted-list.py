#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
#
# algorithms
# Easy (42.71%)
# Total Accepted:    336.7K
# Total Submissions: 786.7K
# Testcase Example:  '[1,1,2]'
#
# Given a sorted linked list, delete all duplicates such that each element
# appear only once.
# 
# Example 1:
# 
# 
# Input: 1->1->2
# Output: 1->2
# 
# 
# Example 2:
# 
# 
# Input: 1->1->2->3->3
# Output: 1->2->3
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def deleteDuplicates(self, head: ListNode) -> ListNode:
    def deleteDuplicates(self, head):
        if not head:
            return None
        n = head
        while n and n.next:
            if n.val == n.next.val:
                if n.next.next:
                    n.next = n.next.next
                else:
                    n.next = None
            else:
                n = n.next
        return head



