#
# @lc app=leetcode id=61 lang=python3
#
# [61] Rotate List
#
# https://leetcode.com/problems/rotate-list/description/
#
# algorithms
# Medium (28.79%)
# Likes:    877
# Dislikes: 945
# Total Accepted:    237.6K
# Total Submissions: 825.2K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, rotate the list to the right by k places, where k is
# non-negative.
# 
# Example 1:
# 
# 
# Input: 1->2->3->4->5->NULL, k = 2
# Output: 4->5->1->2->3->NULL
# Explanation:
# rotate 1 steps to the right: 5->1->2->3->4->NULL
# rotate 2 steps to the right: 4->5->1->2->3->NULL
# 
# 
# Example 2:
# 
# 
# Input: 0->1->2->NULL, k = 4
# Output: 2->0->1->NULL
# Explanation:
# rotate 1 steps to the right: 2->0->1->NULL
# rotate 2 steps to the right: 1->2->0->NULL
# rotate 3 steps to the right: 0->1->2->NULL
# rotate 4 steps to the right: 2->0->1->NULL
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
    # def rotateRight(self, head: ListNode, k: int) -> ListNode:
    def rotateRight(self, head, k):
        if not head:
            return None
        length = 1
        tail = head
        node = head
        while tail.next:
            tail = tail.next
            length += 1
        i = length - k % length
        while i > 1:
            i -= 1
            node = node.next
        
        tail.next = head
        head = node.next
        node.next = None
        return head

    def rotateRight_me(self, head, k):
        # print(head)
        if k == 0:
            return head
        if not head:
            return None
        if not head.next:
            return head
        node = head
        node.prev = None
        length = 1
        while node.next:
            node.next.prev = node
            node = node.next
            length += 1
        tail = node
        # print('ctn=', ctn)
        # print('tail', tail)
        # print('head', head)
        i = 0
        while i < k % length:
            head.prev = tail
            tail.next = head
            tail.prev.next = None
            head = tail
            tail = tail.prev
            i += 1
        # print('new_tail', new_tail)
        # print('head=', head)
        # print('head.prev=', head.prev)
        # print('tail=', tail)
        return head
# @lc code=end
