#
# @lc app=leetcode id=92 lang=python3
#
# [92] Reverse Linked List II
#
# https://leetcode.com/problems/reverse-linked-list-ii/description/
#
# algorithms
# Medium (37.07%)
# Likes:    1761
# Dislikes: 117
# Total Accepted:    237K
# Total Submissions: 639.3K
# Testcase Example:  '[1,2,3,4,5]\n2\n4'
#
# Reverse a linked list from position m to n. Do it in one-pass.
# 
# Note: 1 ≤ m ≤ n ≤ length of list.
# 
# Example:
# 
# 
# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
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
    # def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
    def reverseBetween_me(self, head, m, n):
        
        if m == n:
            return head

        def append(node1, node2):
            head = node1
            while node1.next:
                node1 = node1.next
            node1.next = node2
            return head

        def reverse(head, k):
            prev = None
            curr = head
            i = 0
            while i < k:
                temp = curr.next
                curr.next = prev
                prev, curr = curr, temp
                i += 1
            if temp:
                return append(prev, temp)
            return prev

        if m == 1:
            return reverse(head, n)
        node = head
        i = 1
        while i < m - 1:
            node = node.next
            i += 1
        node.next = reverse(node.next, n - m + 1)
        return head

    def reverseBetween(self, head, m, n):
        if not head:
            return None
        curr, prev = head, None
        while m > 1:
            prev = curr
            curr = curr.next
            m, n = m - 1, n - 1
        tail, con = curr, prev
        while n:
            temp = curr.next
            curr.next = prev
            prev, curr = curr, temp
            n -= 1
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = curr
        return head
# @lc code=end
