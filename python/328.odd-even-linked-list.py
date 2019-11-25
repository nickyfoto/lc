#
# @lc app=leetcode id=328 lang=python3
#
# [328] Odd Even Linked List
#
# https://leetcode.com/problems/odd-even-linked-list/description/
#
# algorithms
# Medium (50.19%)
# Total Accepted:    165.6K
# Total Submissions: 329.1K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given a singly linked list, group all odd nodes together followed by the even
# nodes. Please note here we are talking about the node number and not the
# value in the nodes.
# 
# You should try to do it in place. The program should run in O(1) space
# complexity and O(nodes) time complexity.
# 
# Example 1:
# 
# 
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
# 
# 
# Example 2:
# 
# 
# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL
# 
# 
# Note:
# 
# 
# The relative order inside both the even and odd groups should remain as it
# was in the input.
# The first node is considered odd, the second node even and so on ...
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def oddEvenList(self, head: ListNode) -> ListNode:
    def oddEvenList(self, head):
        if not head:
            return None
        
        # print(head)
        node = head
        isOdd = True
        self.even = None
        while node:
            node.isOdd = isOdd
            isOdd = not isOdd
            node = node.next
            

        def removeEven(node, tail):
            # print(node)
            if not tail:
                self.even = ListNode(node.val)
                return node.next, self.even
            else:
                tail.next = ListNode(node.val)
                return node.next, tail.next


        node = head
        while node:
            nx = node.next
            if not nx:
                break
            # print(node, nx)
            while not nx.isOdd:
                if not self.even:
                    nx, tail = removeEven(nx, self.even)
                else:
                    nx, tail = removeEven(nx, tail)
                # print(nx)
                if not nx:
                    break
            node.next = nx
            if node.next:
                node = node.next
        
        # print('node', node)
        
        node.next = self.even

        
        return head







# from linked_list import buildHead, ListNode
# s = Solution()

# l = list(range(1, 6))
# head = buildHead(l)
# print(s.oddEvenList(head))

# l = [2,1,3,5,6,4,7]
# head = buildHead(l)
# print(s.oddEvenList(head))


# l = [1,2,3,4,5,6,7,8]

# head = buildHead(l)
# print(s.oddEvenList(head))


        
