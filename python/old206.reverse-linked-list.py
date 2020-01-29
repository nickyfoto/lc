#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (55.04%)
# Total Accepted:    604.2K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,4,5]'
#
# Reverse a singly linked list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# 
# 
# Follow up:
# 
# A linked list can be reversed either iteratively or recursively. Could you
# implement both?
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def reverseList(self, head: ListNode) -> ListNode:
    def reverseList(self, head):
        if not head:
            return None
        l = [head]
        while head.next:
            l.insert(0, head.next)
            head = head.next
        # l.insert(0, head)
        # print([x.val for x in l])
        for i in range(len(l)):
            if i < len(l) - 1:
                l[i].next = l[i+1]
            if i == len(l) - 1:
                l[i].next = None
        # for i in range(len(l)):
        #     print(l[i].val)
        #     if l[i].next:
        #         print('val=', l[i].next.val)
        return l[0]
        # print(len(l))
                # print(i, l[i], head.next)
        #         print(i, head.next.val)
        #     if i < len(l) - 2:
        #         l[i].next = l[i+1]
        #     if i == len(l) - 1:
        #         l[i].next = None
        # print(head.next)
        # return l[0]


