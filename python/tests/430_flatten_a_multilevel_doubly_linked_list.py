#
# @lc app=leetcode id=430 lang=python3
#
# [430] Flatten a Multilevel Doubly Linked List
#
# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/
#
# algorithms
# Medium (44.04%)
# Total Accepted:    33.5K
# Total Submissions: 76K
# Testcase Example:  '{"$id":"1","child":null,"next":{"$id":"2","child":null,"next":{"$id":"3","child":{"$id":"7","child":null,"next":{"$id":"8","child":{"$id":"11","child":null,"next":{"$id":"12","child":null,"next":null,"prev":{"$ref":"11"},"val":12},"prev":null,"val":11},"next":{"$id":"9","child":null,"next":{"$id":"10","child":null,"next":null,"prev":{"$ref":"9"},"val":10},"prev":{"$ref":"8"},"val":9},"prev":{"$ref":"7"},"val":8},"prev":null,"val":7},"next":{"$id":"4","child":null,"next":{"$id":"5","child":null,"next":{"$id":"6","child":null,"next":null,"prev":{"$ref":"5"},"val":6},"prev":{"$ref":"4"},"val":5},"prev":{"$ref":"3"},"val":4},"prev":{"$ref":"2"},"val":3},"prev":{"$ref":"1"},"val":2},"prev":null,"val":1}'
#
# You are given a doubly linked list which in addition to the next and previous
# pointers, it could have a child pointer, which may or may not point to a
# separate doubly linked list. These child lists may have one or more children
# of their own, and so on, to produce a multilevel data structure, as shown in
# the example below.
# 
# Flatten the list so that all the nodes appear in a single-level, doubly
# linked list. You are given the head of the first level of the list.
# 
# 
# 
# Example:
# 
# 
# Input:
# ⁠1---2---3---4---5---6--NULL
# ⁠        |
# ⁠        7---8---9---10--NULL
# ⁠            |
# ⁠            11--12--NULL
# 
# Output:
# 1-2-3-7-8-11-12-9-10-4-5-6-NULL
# 
# 
# 
# 
# Explanation for the above example:
# 
# Given the following multilevel doubly linked list:
# 
# 
# 
# 
# 
# 
# We should return the following flattened doubly linked list:
# 
# 
# 
# 
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        node = head
        stack = []
        while node:
            if node.child:
                if node.next:
                    stack.append(node.next)
                node.child.prev = node
                node.next = node.child
                node.child = None
            else:
                if not node.next:
                    if stack:
                        p = stack.pop()
                        p.prev = node
                        node.next = p
            node = node.next
        return head

    def flatten(self, head: 'Node') -> 'Node':
        if not head: return head
        def recur(head, tail=None):
            """
            output head and tail of a linked list
            """
            if not head: return None, None
            if not head.next and tail: 
                head.next = tail
                tail.prev = head
                tail = None
            curr = head
            while curr and (curr.next or curr.child):
                if curr.child:
                    child = curr.child
                    child_head, child_tail = recur(child, curr.next)
                    curr.child = None
                    curr.next = child_head
                    child_head.prev = curr
                else:
                    curr = curr.next
                if not curr.next and tail:
                    curr.next = tail
                    tail.prev = curr
                    tail = None
                
            return head, curr
        
        head, _ = recur(head)
        return head

    def flatten_dfs(self, prev, curr):
        if not curr: return prev
        curr.prev = prev
        prev.next = curr
        tempNext = curr.next
        tail = self.flatten_dfs(curr, curr.child)
        curr.child = None
        return self.flatten_dfs(tail, tempNext)

    def flatten(self, head):
        if not head: return head
        dummy_head = Node(None, None, head, None)
        self.flatten_dfs(dummy_head, head)
        dummy_head.next.prev = None
        return dummy_head.next



    def flatten(self, head):
        if not head: return head
        node = head
        while node:
            if not node.child:
                node = node.next
                continue
            temp = node.child
            while temp.next:
                temp = temp.next
            temp.next = node.next
            if node.next: node.next.prev = temp
            node.next = node.child
            node.child.prev = node
            node.child = None
        return head












        
