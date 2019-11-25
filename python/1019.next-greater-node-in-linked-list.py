#
# @lc app=leetcode id=1019 lang=python3
#
# [1019] Next Greater Node In Linked List
#
# https://leetcode.com/problems/next-greater-node-in-linked-list/description/
#
# algorithms
# Medium (57.05%)
# Total Accepted:    17.4K
# Total Submissions: 30.5K
# Testcase Example:  '[2,1,5]'
#
# We are given a linked list with head as the first node.  Let's number the
# nodes in the list: node_1, node_2, node_3, ... etc.
# 
# Each node may have a next larger value: for node_i, next_larger(node_i) is
# the node_j.val such that j > i, node_j.val > node_i.val, and j is the
# smallest possible choice.  If such a j does not exist, the next larger value
# is 0.
# 
# Return an array of integers answer, where answer[i] =
# next_larger(node_{i+1}).
# 
# Note that in the example inputs (not outputs) below, arrays such as [2,1,5]
# represent the serialization of a linked list with a head node value of 2,
# second node value of 1, and third node value of 5.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [2,1,5]
# Output: [5,5,0]
# 
# 
# 
# Example 2:
# 
# 
# Input: [2,7,4,3,5]
# Output: [7,0,5,5,0]
# 
# 
# 
# Example 3:
# 
# 
# Input: [1,7,5,1,9,2,5,1]
# Output: [7,9,9,9,0,5,0,0]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= node.val <= 10^9 for each node in the linked list.
# The given list has length in the range [0, 10000].
# 
# 
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def nextLargerNodes(self, head: ListNode) -> List[int]:
    def nextLargerNodes2(self, head):
        # print(head)
        
        l = []
        current = head
        while current.next:
            n = current            
            while n.next:
                if n.next.val > current.val:
                    l.append(n.next.val)
                    break
                n = n.next
            if not n.next:
                # print('here', largest)
                l.append(0)
            current = current.next
        # print('final', current.val)
        # print(l)
        l.append(0)
        return l

    def nextLargerNode1(self, head):
        s = [head.val]
        while head.next:
            s.append(head.next.val)
            head = head.next
        # print('s=', s)
        ss = sorted(range(len(s)), key=lambda k: s[k])
        # print(ss)
        res = []
        max_rank = len(s) - 1
        i = 0
        while i < len(s) - 1:
            rank = ss.index(i)
            print(s[i], rank, max_rank)
            if rank == max_rank:
                print('use rank')
                max_rank -= 1
                res.append(0)
                i += 1
            else:
                idx = i
                # print(s[i])
                while idx+1<len(s) and s[idx+1] <= s[i]:
                    # print('   while', s[i], idx)
                    idx += 1
                if idx+1 == len(s):
                    res.append(0)
                    # print(res)
                    # max_rank -= 1
                else:
                    res.append(s[idx+1])
                    # print(res)
                i += 1
        res.append(0)
        return res

    def to_list(self, head):
        s = [head.val]
        while head.next:
            s.append(head.next.val)
            head = head.next
        n = len(s)
        ss = sorted(range(n), key=lambda k: s[k])
        ssd = dict(zip(ss, range(n)))
        return s, ssd
    

    def nextLargerNodes(self, head):
        s, ssd = self.to_list(head)
        res = []
        max_rank = len(s) - 1
        i = 0
        while i < len(s) - 1:
            # rank = ss.index(i)
            rank = ssd[i]
            val = s[i]
            # print('i=', i, 'rank=', rank, 's[i]=', s[i], 'max_rank=', max_rank)
            count = 1
            while i+1<len(s)-1 and s[i+1] == val:
                rank += 1
                i += 1
                count += 1
                # print('i=', i, 'rank=', rank, 's[i]=', s[i], 'count=', count, 'max_rank=', max_rank)
            # print('i=', i, 'count=', count)
            if rank == max_rank:
                # print('update rank')
                max_rank -= count
                for g in range(count):
                    res.append(0)
                i += 1
                # print('i=', i, 'rank=', rank, 's[i]=', s[i], 'count=', count, 'max_rank=', max_rank)

            else:
                # print('else i=', i, 'rank=', rank, 's[i]=', s[i], 'count=', count, 'max_rank=', max_rank, res)
                idx = i
                while idx+1<len(s) and s[idx+1] <= s[i]:
                    idx += 1
                if idx+1 == len(s):
                    for g in range(count):
                        res.append(0)
                    # print('i=', i)
                else:
                    for g in range(count):
                        res.append(s[idx+1])
                        # print('i=',i, res)
                i += 1
        res.append(0)
        return res


    def nextLargerNodes4(self, head):
        res, stack = [], []
        while head:
            while stack and stack[-1][1] < head.val:
                res[stack.pop()[0]] = head.val
            stack.append((len(res), head.val))
            res.append(0)
            print(stack, res)
            head = head.next
        return res


import time

start = time.time()
s = Solution()
from linked_list import head
# print(s.nextLargerNodes2(head), 'correct')
# print(s.nextLargerNodes(head) == s.nextLargerNodes2(head))
print(s.nextLargerNodes4(head))
        
end = time.time()
print(end - start)


