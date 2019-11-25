#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#
# https://leetcode.com/problems/split-linked-list-in-parts/description/
#
# algorithms
# Medium (49.71%)
# Total Accepted:    32.2K
# Total Submissions: 64.8K
# Testcase Example:  '[1,2,3,4]\n5'
#
# Given a (singly) linked list with head node root, write a function to split
# the linked list into k consecutive linked list "parts".
# 
# The length of each part should be as equal as possible: no two parts should
# have a size differing by more than 1.  This may lead to some parts being
# null.
# 
# The parts should be in order of occurrence in the input list, and parts
# occurring earlier should always have a size greater than or equal parts
# occurring later.
# 
# Return a List of ListNode's representing the linked list parts that are
# formed.
# 
# 
# Examples
# 1->2->3->4, k = 5 // 5 equal parts
# [ [1], 
# [2],
# [3],
# [4],
# null ]
# 
# Example 1:
# 
# Input: 
# root = [1, 2, 3], k = 5
# Output: [[1],[2],[3],[],[]]
# Explanation:
# The input and each element of the output are ListNodes, not arrays.
# For example, the input root has root.val = 1, root.next.val = 2,
# \root.next.next.val = 3, and root.next.next.next = null.
# The first element output[0] has output[0].val = 1, output[0].next = null.
# The last element output[4] is null, but it's string representation as a
# ListNode is [].
# 
# 
# 
# Example 2:
# 
# Input: 
# root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
# Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
# Explanation:
# The input has been split into consecutive parts with size difference at most
# 1, and earlier parts are a larger size than the later parts.
# 
# 
# 
# Note:
# The length of root will be in the range [0, 1000].
# Each value of a node in the input will be an integer in the range [0, 999].
# k will be an integer in the range [1, 50].
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
    def splitListToParts(self, root, k: int):


        def length(root):
            n = 0
            while root:
                n += 1
                root = root.next
            return n

        # print(length(root))
        # print(root)
        l = length(root)


      


        if k >= l:
            n = 0
            res = []
            node = root
            while n < k:
                if node:
                    x = node.next
                    node.next = None
                    res.append(node)
                    node = x
                    n += 1
                else:
                    res.append(None)
                    n += 1
        else:
            quo, r = divmod(l, k)
            res = [None] * k
            res[0] = root
            n = 0
            while n < k:
                node = res[n]
                if r:
                    part_length = quo + 1
                    r -= 1
                else:
                    part_length = quo
                i = 0
                while i < part_length-1:
                    i += 1
                    node = node.next
                n += 1
                if node.next:
                    res[n] = node.next
                    node.next = None
                # print('here', node, res[0], res[1], res[2])
        # for node in res:
        #     print(node, end=',')
        # print()

        return res


# s = Solution()
# from linked_list import buildHead

# root = [1, 2, 3]
# head = buildHead(root)
# k = 5
# print(s.splitListToParts(head, k))



# root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# head = buildHead(root)
# k = 3
# print(s.splitListToParts(head, k))











        
