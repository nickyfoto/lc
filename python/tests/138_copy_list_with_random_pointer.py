#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (32.16%)
# Likes:    2464
# Dislikes: 570
# Total Accepted:    340.3K
# Total Submissions: 1.1M
# Testcase Example:  '[[7,null],[13,0],[11,4],[10,2],[1,0]]\r'
#
# A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.
# 
# Return a deep copy of the list.
# 
# The Linked List is represented in the input/output as a list of n nodes. Each
# node is represented as a pair of [val, random_index] where:
# 
# 
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) where random
# pointer points to, or null if it does not point to any node.
# 
# 
# 
# Example 1:
# 
# 
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 
# 
# Example 2:
# 
# 
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
# 
# 
# Example 4:
# 
# 
# Input: head = []
# Output: []
# Explanation: Given linked list is empty (null pointer), so return null.
# 
# 
# 
# Constraints:
# 
# 
# -10000 <= Node.val <= 10000
# Node.random is null or pointing to a node in the linked list.
# Number of Nodes will not exceed 1000.
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    # def copyRandomList(self, head: 'Node') -> 'Node':

    def copyRandomList(self, head):
        if not head:
            return None

        node = head
        d = {}
        while node:
            d[node] = Node(node.val)
            node = node.next

        node = head
        while node:
            d[node].next = d.get(node.next)
            d[node].random = d.get(node.random)
            node = node.next
        return d[head]

    def copyRandomList_forum(self, head):
        """
        not understand
        """
        node = head
        while node:
            copy = Node(node.val)
            copy.next = node.next
            node.next = copy
            node = copy.next

        # Set each copy's .random
        node = head
        while node:
            if node.random:
                node.next.random = node.random.next
            else:
                node.next.random = node.random
            node = node.next.next

        # Separate the copied list from the original, (re)setting every .next
        node = head
        if head:
            copy = head_copy = head.next
        else:
            copy = head_copy = head
        while node:
            node.next = node = copy.next
            if node:
                copy.next = copy = node.next
            else:
                copy.next = copy = node

        return head_copy

    def copyRandomList_me(self, head):
        if not head:
            return None
        new_head = Node(head.val)
        node = new_head

        random_references = [head.random]
        ordered_references = [head]
        new_node_references = [new_head]
        while head.next:
            random_references.append(head.next.random)
            ordered_references.append(head.next)
            new_next = Node(head.next.val)
            node.next = new_next
            head = head.next
            node = node.next
            new_node_references.append(node)
        # print([n for n in random_references])
        # print([n for n in ordered_references])
        for i in range(len(new_node_references)):
            try:
                idx = ordered_references.index(random_references[i])
            except ValueError:
                idx = None
            # print('i=', i, 'idx=', idx)
            if idx is not None:
                new_node_references[i].random = new_node_references[idx]
            else:
                new_node_references[i].random = None

        return new_head
# @lc code=end
