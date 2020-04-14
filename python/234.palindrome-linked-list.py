#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (36.22%)
# Total Accepted:    269.2K
# Total Submissions: 740.7K
# Testcase Example:  '[1,2]'
#
# Given a singly linked list, determine if it is a palindrome.
# 
# Example 1:
# 
# 
# Input: 1->2
# Output: false
# 
# Example 2:
# 
# 
# Input: 1->2->2->1
# Output: true
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def isPalindrome(self, head: ListNode) -> bool:
    def isPalindrome(self, head):
        """
        O(1) space is too complicated
        """
        if not head:
            return True
        # n = 0
        head
        l = [head.val]
        while head.next:
            # n += 1
            l.append(head.next.val)
            head = head.next
        # print(l)
        for i in range(len(l) // 2):
            if l[i] != l[-(i+1)]:
                return False
        return True



