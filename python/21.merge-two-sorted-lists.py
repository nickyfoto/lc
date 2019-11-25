#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (47.54%)
# Total Accepted:    605.2K
# Total Submissions: 1.3M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
# 
# Example:
# 
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    def mergeTwoLists(self, l1, l2):
        self.l = []
        def recur(k1, k2):
            # if k1 and k2:
            #     print(k1.val, k2.val, self.l.val)
            #     if self.l.next:
            #         print('self.l.next=', self.l.next.val)
            if k1 and k2:
                if k2.val < k1.val:
                    self.l.append(k2)
                    recur(k1, k2.next)
                else:
                    self.l.append(k1)
                    recur(k1.next, k2)
            elif not k1:
                # self.l.next = k2
                while k2:
                    self.l.append(k2)
                    k2 = k2.next
            elif not k2:
                while k1:
                    self.l.append(k1)
                    k1 = k1.next
            
        recur(l1, l2)
        n = len(self.l)
        for i in range(n-1):
            if i+1 == n - 1:
                self.l[i+1].next = None
            self.l[i].next = self.l[i+1]
        if self.l:
            return self.l[0]
        return []

        
