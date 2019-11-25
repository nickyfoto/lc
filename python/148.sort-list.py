#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#
# https://leetcode.com/problems/sort-list/description/
#
# algorithms
# Medium (37.43%)
# Total Accepted:    208.2K
# Total Submissions: 556.1K
# Testcase Example:  '[4,2,1,3]'
#
# Sort a linked list in O(n log n) time using constant space complexity.
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
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def sortList(self, head: ListNode) -> ListNode:
    def sortList(self, head):
        



s = Solution()
from linked_list import build_head, ListNode

l = [6,5,3,1,8,7,2,4]
head = build_head(l)
print(s.sortList(head))

l = [4,2,1,3]
head = build_head(l)
print(s.sortList(head))

l = [-1,5,3,4,0]
head = build_head(l)
print(s.sortList(head))









