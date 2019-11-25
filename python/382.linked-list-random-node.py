#
# @lc app=leetcode id=382 lang=python3
#
# [382] Linked List Random Node
#
# https://leetcode.com/problems/linked-list-random-node/description/
#
# algorithms
# Medium (49.78%)
# Total Accepted:    56.5K
# Total Submissions: 113.5K
# Testcase Example:  '["Solution","getRandom"]\n[[[1,2,3]],[]]'
#
# Given a singly linked list, return a random node's value from the linked
# list. Each node must have the same probability of being chosen.
# 
# Follow up:
# What if the linked list is extremely large and its length is unknown to you?
# Could you solve this efficiently without using extra space?
# 
# 
# Example:
# 
# // Init a singly linked list [1,2,3].
# ListNode head = new ListNode(1);
# head.next = new ListNode(2);
# head.next.next = new ListNode(3);
# Solution solution = new Solution(head);
# 
# // getRandom() should return either 1, 2, or 3 randomly. Each element should
# have equal probability of returning.
# solution.getRandom();
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from random import randint
class Solution:

    def __init__(self, head):
        self.head = head
        self.n = 1
        self.reach_end = False
    def getRandom(self) -> int:
        i = 0
        while True:
            # print('r=', r)
            node = self.head
            if not self.reach_end:
                r = randint(0, self.n) 
                if r == i:
                    # print('r == 0')
                    # print('self.reach_end=', self.reach_end)
                    # print('self.n=', self.n)
                    return node.val
                else:
                    while node.next and i < r:
                        i += 1
                        if i == self.n:
                            self.n += 1
                        node = node.next
                    if not node.next:
                        self.reach_end = True
                    # print('self.reach_end=', self.reach_end)
                    # print('self.n=', self.n)
                    # print('i=', i)
                    return node.val
                    
            else:
                r = randint(0, self.n-1) 
                # print('self.reach_end=', self.reach_end)
                # print('self.n=', self.n)
                # print('r=', r)
                while node.next and i < r:
                    i += 1
                    node = node.next
                return node.val

    # def __init__(self, head):
    #     self.head = head

    # def getRandom(self) -> int:
    #     node = self.head
    #     i = 0
    #     while True:
    #         if randint(0, i+1) == i:
    #             return node.val
    #         if node.next:
    #             i += 1
    #             node = node.next


    # def getRandom(self):
    #     i = 0
    #     node = self.head
    #     while True:
    #         r = randint(0, i+1)
    #         print('r=', r)
    #         print('i=', i)
    #         count = 0
    #         while node.next and count < r:
    #             count += 1
    #             node = node.next
    #             i += 1
    #         return node.val

    # def __init__(self, head: ListNode):
    # def __init__(self, head):
    #     """
    #     @param head The linked list's head.
    #     Note that the head is guaranteed to be not null, so it contains at least one node.
    #     """
    #     self.head = head
    #     self.n = self._get_length()
    #     # print(self.n)

    # def _get_length(self):
    #     n = 0
    #     node = self.head
    #     while node:
    #         n += 1
    #         node = node.next
    #     return n

    # def get(self, idx):
    #     count = 0
    #     node = self.head
    #     while count < idx:
    #         count += 1
    #         node = node.next
    #     # print(count)
    #     return node.val

    # def getRandom(self) -> int:
    #     """
    #     Returns a random node's value.
    #     """
    #     return self.get(randint(0, self.n-1))
    #     # print(self.get(0))
    #     # print(self.get(1))
    #     # print(self.get(2))
    #     # print(self.get(3))


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

# from linked_list import buildHead
# from collections import Counter
# l = [1,2,3]
# l = [1,2]
# l = [1]
# l = [randint(1,3) ifor range(1000)]
# head = buildHead(l)
# s = Solution(head)
# a = [s.getRandom() for i in range(100000)]
# print(Counter(a))
# print(s.getRandom()== None)
# for i in range(20):
#     print(s.getRandom())
#     print('=='*20)
# print(s.getRandom())



