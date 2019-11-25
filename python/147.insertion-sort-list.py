#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#
# https://leetcode.com/problems/insertion-sort-list/description/
#
# algorithms
# Medium (38.50%)
# Total Accepted:    160.5K
# Total Submissions: 416.8K
# Testcase Example:  '[4,2,1,3]'
#
# Sort a linked list using insertion sort.
# 
# 
# 
# 
# 
# A graphical example of insertion sort. The partial sorted list (black)
# initially contains only the first element in the list.
# With each iteration one element (red) is removed from the input data and
# inserted in-place into the sorted list
# 
# 
# 
# 
# 
# Algorithm of Insertion Sort:
# 
# 
# Insertion sort iterates, consuming one input element each repetition, and
# growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data,
# finds the location it belongs within the sorted list, and inserts it
# there.
# It repeats until no input elements remain.
# 
# 
# 
# Example 1:
# 
# 
# Input: 4->2->1->3
# Output: 1->2->3->4
# 
# 
# Example 2:
# 
# 
# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def insertionSortList(self, head: ListNode) -> ListNode:
    def insertionSortList(self, head):
        if not head:
            return None
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l.sort(reverse=True)
        head = ListNode(l.pop())
        node = head
        while l:
            new_node = ListNode(l.pop())
            node.next = new_node
            node = node.next
        return head

    
    def insertionSortList2(self, head):
        # print('input=', head)
        if not head:
            return None
        node = head
        node.prev = None
        while node:
            if node.next:
                node.next.prev = node
            node = node.next

        node = head
        if not head.next:
            return head
        else:
            if node.next.val < node.next.prev.val:
                head = None
            # else:

        
        while node:
            # print('here')
            if node.next:
                # print(node)
                if node.next.val < node.next.prev.val:
                    # print('checking node=', node)
                    right = node.next             
                    node.next = right.next
                    right.prev = node.prev
                    node.prev = right
                    right.next = node
                    if node.next:
                        node.next.prev = node
                    node = right

                    if not head:
                        head = node
                    else:
                        h = head
                        while h.next:
                            h = h.next
                        h.next = node
                    node = head

                while node.val <= node.next.val:
                    node = node.next
                    if not node.next:
                        node = None
                        break

                if not node:
                    break

                # print('head=', head, 'node=', node)
                if node.prev:
                    node.prev.next = None
                else:
                    head = None
                
                # print('head=', head)
        return head


    def insertionSortList(self, head):
        dummy = ListNode(0)
        prev = dummy
        while head:
            temp = head.next
            if prev.val >= head.val:
                prev = dummy
            while prev.next and prev.next.val < head.val:
                prev = prev.next
            head.next = prev.next
            prev.next = head
            head = temp
        return dummy.next

# s = Solution()
# from linked_list import build_head, ListNode

# l = [6,5,3,1,8,7,2,4]
# head = build_head(l)
# print(s.insertionSortList(head))

# l = [4,2,1,3]
# head = build_head(l)
# print(s.insertionSortList(head))

# l = [1]
# head = build_head(l)
# print(s.insertionSortList(head))

# l = [-1,5,3,4,0]
# head = build_head(l)
# print(s.insertionSortList(head))


# l = [1,1]
# head = build_head(l)
# print(s.insertionSortList(head))

































