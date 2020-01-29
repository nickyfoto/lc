#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (34.76%)
# Likes:    2541
# Dislikes: 187
# Total Accepted:    514.7K
# Total Submissions: 1.5M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# Given a linked list, remove the n-th node from the end of list and return its
# head.
# 
# Example:
# 
# 
# Given linked list: 1->2->3->4->5, and n = 2.
# 
# After removing the second node from the end, the linked list becomes
# 1->2->3->5.
# 
# 
# Note:
# 
# Given n will always be valid.
# 
# Follow up:
# 
# Could you do this in one pass?
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    def removeNthFromEnd_me(self, head, n):
        # print(head is None)
        # print(head)
        lst = []
        node = head
        while node:
            lst.append(node)
            node = node.next
        
        if n == 1:
            if len(lst) == 1:
                return None
            lst[-2].next = None
        else:
            if n == len(lst):
                return head.next
            lst[-(n+1)].next = lst[-(n-1)]
        # print(head)
        return head
    
    def removeNthFromEnd(self, head, n):
        if n == 1 and not head.next:
            return None
                
        i = 0
        r = head
        while r.next and i < n:
            r = r.next
            i += 1
        
        if not r.next and i < n:
            while i < n:
                head = head.next
                i += 1
            # print('here', head)
            return head
        
        l = head
        while r.next:
            r = r.next
            l = l.next
        if l.next:
            l.next = l.next.next
        else:
            l.next = None
        # print(head)  
        return head


# @lc code=end
