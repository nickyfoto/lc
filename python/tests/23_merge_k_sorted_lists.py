#
# @lc app=leetcode id=23 lang=python3
#
# [23] Merge k Sorted Lists
#
# https://leetcode.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (37.85%)
# Likes:    3597
# Dislikes: 228
# Total Accepted:    533.8K
# Total Submissions: 1.4M
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and
# describe its complexity.
# 
# Example:
# 
# 
# Input:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# Output: 1->1->2->3->4->4->5->6
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
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
            
        def merge2(l1, l2):
            """
            Given two sorted linked list
            merge them into one sorted list
            """
            head = ListNode(0)
            Node = head
            while l1 and l2:
                if l1.val <= l2.val:
                    Node.next = ListNode(l1.val)
                    l1 = l1.next
                else:
                    Node.next = ListNode(l2.val)
                    l2 = l2.next
                Node = Node.next
            if not l1 and l2:
                Node.next = l2
            if not l2 and l1:
                Node.next = l1
            return head.next

        while len(lists) > 2:
            l1 = lists.pop(0)
            l2 = lists.pop(0)
            m = merge2(l1, l2)
            # print(m)
            lists.append(m)
        l1, l2 = lists
        res = merge2(l1, l2)
        # print(res)
        return res
# @lc code=end
