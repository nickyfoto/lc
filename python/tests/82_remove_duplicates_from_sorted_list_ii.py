#
# @lc app=leetcode id=82 lang=python3
#
# [82] Remove Duplicates from Sorted List II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (35.27%)
# Likes:    1268
# Dislikes: 98
# Total Accepted:    223.2K
# Total Submissions: 632.6K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# Given a sorted linked list, delete all nodes that have duplicate numbers,
# leaving only distinct numbers from the original list.
# 
# Example 1:
# 
# 
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
# 
# 
# Example 2:
# 
# 
# Input: 1->1->1->2->3
# Output: 2->3
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
    # def deleteDuplicates(self, head: ListNode) -> ListNode:
    def deleteDuplicates(self, head):
        if not head: return None 
        if not head.next: return head
        node = head
        while node.next:
            node.next.prev = node
            node = node.next
        head.prev = ListNode(-1)
        head.prev.next = head
        node = head.prev.next
        while node.next:
            if node.val != node.next.val:
                node = node.next
            else:
                p = node.prev
                r_val = node.val
                while node and node.val == r_val:
                    node = node.next
                if not node:
                    p.next = node
                    return head.prev.next
                p.next = node
                node.prev = p
        return head.prev.next

    # def deleteDuplicates_slow(self, head):
    #     """
    #     too slow
    #     """
    #     if not head: return None 
    #     if not head.next: return head
    #     if head.val == head.next.val:
    #         while head.next and head.val == head.next.val:
    #             head = head.next
    #         head = self.deleteDuplicates(head.next)
    #     if head:
    #         head.next = self.deleteDuplicates(head.next)
    #     return head

# @lc code=end
