#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#
# https://leetcode.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (46.32%)
# Total Accepted:    356K
# Total Submissions: 768K
# Testcase Example:  '[1,2,3,4]'
#
# Given a linked list, swap every two adjacent nodes and return its head.
# 
# You may not modify the values in the list's nodes, only nodes itself may be
# changed.
# 
# 
# 
# Example:
# 
# 
# Given 1->2->3->4, you should return the list as 2->1->4->3.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def swapPairs(self, head: ListNode) -> ListNode:
    def swapPairs(self, head):


        def recur(node):
            if node:
                if node.next:
                    my_next = node.next
                    node.next = recur(my_next.next)
                    my_next.next = node
                    return my_next
                else:
                    return node

        return recur(head)




# s = Solution()
# from linked_list import buildHead
# l = [1,2,3,4]
# head = buildHead(l)
# print(s.swapPairs(head))


# l = [1,2,3,4,5]
# head = buildHead(l)
# print(s.swapPairs(head))

# l = [1,2,3]
# head = buildHead(l)
# print(s.swapPairs(head))


# l = [1,2]
# head = buildHead(l)
# print(s.swapPairs(head))

# l = [1]
# head = buildHead(l)
# print(s.swapPairs(head))



# # l = []
# # head = buildHead(l)
# print(s.swapPairs(None))










                
