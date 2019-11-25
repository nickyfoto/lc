#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#
# https://leetcode.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (51.04%)
# Total Accepted:    103.6K
# Total Submissions: 202.9K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The most significant digit comes first and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Follow up:
# What if you cannot modify the input lists? In other words, reversing the
# lists is not allowed.
# 
# 
# 
# Example:
# 
# Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 8 -> 0 -> 7
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    def addTwoNumbers(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        def add(n1, n2, extra=0):
            # n1 n2 are both single node
            quo, r = divmod(n1.val + n2.val + extra, 10)
            node = ListNode(r)            
            return quo, node

        def buildStack(l):
            s = []
            while l:
                s.append(l)
                l = l.next
            return s

        s1, s2 = buildStack(l1), buildStack(l2)
        node_stack, quo_stack = [], []



        while s1 and s2:
            if not node_stack:
                quo, node = add(s1.pop(), s2.pop())
            else:
                quo, node = add(s1.pop(), s2.pop(), quo_stack.pop())
                node.next = node_stack.pop()
            node_stack.append(node)
            quo_stack.append(quo)
        
        if s2:
            s1 = s2
        while s1:
            quo = quo_stack.pop()
            if not quo:
                s1[-1].next = node_stack.pop()
                return s1[0]
            else:
                q_node = ListNode(quo)
                next_node = node
                quo, node = add(s1.pop(), q_node)
                node.next = next_node
                quo_stack.append(quo)
                node_stack.append(node)

        if not s1 and not s2:
            quo = quo_stack.pop()
            if not quo:
                return node_stack.pop()
            else:
                node = ListNode(quo)
                node.next = node_stack.pop()
                return node

# s = Solution()
# from linked_list import buildHead, ListNode
# l1 = [7,2,4,3]
# l2 = [5,6,4]
# l1 = buildHead(l1)
# l2 = buildHead(l2)
# print(s.addTwoNumbers(l1, l2))
# l1 = [9,9,9]
# l2 = [1]
# l1 = buildHead(l1)
# l2 = buildHead(l2)
# print(s.addTwoNumbers(l1, l2))
