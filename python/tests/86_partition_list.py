#
# @lc app=leetcode id=86 lang=python3
#
# [86] Partition List
#
# https://leetcode.com/problems/partition-list/description/
#
# algorithms
# Medium (39.71%)
# Likes:    984
# Dislikes: 257
# Total Accepted:    194.7K
# Total Submissions: 490.2K
# Testcase Example:  '[1,4,3,2,5,2]\n3'
#
# Given a linked list and a value x, partition it such that all nodes less than
# x come before nodes greater than or equal to x.
# 
# You should preserve the original relative order of the nodes in each of the
# two partitions.
# 
# Example:
# 
# 
# Input: head = 1->4->3->2->5->2, x = 3
# Output: 1->2->2->4->3->5
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def partition(self, head: ListNode, x: int) -> ListNode:
    def partition(self, head, x):
        """
        construct two linked list, one for value < x
                             the other for value >= x
        before_head points to the head of the first linkedlist
        before points to the end of the first linkedlist
        after_head points to the head of the second linkedlist
        after points to the end of the second linkedlist

        if node's val < x:
            append node to end of first linkedlist by 
                before.next = head
                before = before.next
        else:
            append node to end of second linkedlist by
                after.next = head
                after = after.next
        finally connect the two by
            before.next = after_head.next
        """
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
        after.next = None
        before.next = after_head.next
        return before_head.next
# @lc code=end
