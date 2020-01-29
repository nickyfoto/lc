#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# https://leetcode.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (59.12%)
# Likes:    3440
# Dislikes: 78
# Total Accepted:    804.8K
# Total Submissions: 1.4M
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

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# from lcpy import ListNode
class Solution:
    # def reverseList(self, head: ListNode) -> ListNode:
    def reverseList_me(self, head):
        stack = []
        while head:
            stack.append(head)
            head = head.next
        new_head = ListNode(0)
        node = new_head
        while stack:
            n = stack.pop()
            n.next = None
            node.next = n
            node = node.next
        # print(new_head.next)
        return new_head.next

    def reverseList_iter(self, head):
        """
        todo
        """
        prev  = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
        # print(prev)
        return prev

    def reverseList(self, head):
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p
# @lc code=end
