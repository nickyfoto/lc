#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (32.60%)
# Likes:    6851
# Dislikes: 1769
# Total Accepted:    1.2M
# Total Submissions: 3.6M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
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
    def addTwoNumbers(self, l1, l2):

        rl1 = l1
        rl2 = l2
        head = ListNode(0)
        node = head
        extra = 0
        while rl1 or rl2:
            if not rl1:
                if extra:
                    rl1 = ListNode(extra)
                    extra = 0
                else:
                    node.val = rl2.val
                    node.next = rl2.next
                    # print("head=", head)
                    return head
            if not rl2:
                if extra:
                    rl2 = ListNode(extra)
                    extra = 0
                else:
                    # print('node=', node)
                    node.val = rl1.val
                    node.next = rl1.next
                    # print("head=", head, 'rl1=', rl1)
                    return head
            extra, r = divmod(rl1.val + rl2.val + extra, 10)
            node.val = r
            rl1 = rl1.next
            rl2 = rl2.next
            if rl1 or rl2:
                node.next = ListNode(0)
                node = node.next
        if extra:
            node.next = ListNode(extra)
        # print("head=", head)
        # r = reverse_ll(head)
        # print(r)
        return head

        # return res
# @lc code=end
