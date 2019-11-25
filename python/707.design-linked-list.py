#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#
# https://leetcode.com/problems/design-linked-list/description/
#
# algorithms
# Easy (21.84%)
# Total Accepted:    28.1K
# Total Submissions: 129.8K
# Testcase Example:  '["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]\n[[],[1],[3],[1,2],[1],[1],[1]]'
#
# Design your implementation of the linked list. You can choose to use the
# singly linked list or the doubly linked list. A node in a singly linked list
# should have two attributes: val and next. val is the value of the current
# node, and next is a pointer/reference to the next node. If you want to use
# the doubly linked list, you will need one more attribute prev to indicate the
# previous node in the linked list. Assume all nodes in the linked list are
# 0-indexed.
# 
# Implement these functions in your linked list class:
# 
# 
# get(index) : Get the value of the index-th node in the linked list. If the
# index is invalid, return -1.
# addAtHead(val) : Add a node of value val before the first element of the
# linked list. After the insertion, the new node will be the first node of the
# linked list.
# addAtTail(val) : Append a node of value val to the last element of the linked
# list.
# addAtIndex(index, val) : Add a node of value val before the index-th node in
# the linked list. If index equals to the length of linked list, the node will
# be appended to the end of linked list. If index is greater than the length,
# the node will not be inserted.
# deleteAtIndex(index) : Delete the index-th node in the linked list, if the
# index is valid.
# 
# 
# Example:
# 
# 
# MyLinkedList linkedList = new MyLinkedList();
# linkedList.addAtHead(1);
# linkedList.addAtTail(3);
# linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
# linkedList.get(1);            // returns 2
# linkedList.deleteAtIndex(1);  // now the linked list is 1->3
# linkedList.get(1);            // returns 3
# 
# 
# Note:
# 
# 
# All values will be in the range of [1, 1000].
# The number of operations will be in the range of [1, 1000].
# Please do not use the built-in LinkedList library.
# 
# 
#
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.length = 0
    # def get(self, index: int) -> int:

    def _get_node(self, index):
        # print('index=', index)
        pointer = 0
        n = self.head
        while pointer != index:
            n = n.next
            pointer += 1
        return n

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        # if not self.head:
            # return -1
        if index > self.length - 1:
            return -1
        if index < 0:
            if index == -1 and self.length == 1:
                return self.get(0)
            else:
                return -1
        return self._get_node(index).val

    # def addAtHead(self, val: int) -> None:
    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        if not self.head:
            self.head = Node(val)
            self.length = 1
        else:
            n = Node(val)
            n.next = self.head
            self.head = n
            self.length += 1

    # def addAtTail(self, val: int) -> None:
    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        """
        if not self.head:
            self.addAtHead(val)
        else:
            # print(self.length)
            self.addAtIndex(self.length, val)

    def __str__(self):
        n = self.head
        res = []
        while n:
            res.append(n.val)
            n = n.next
        return str(res)

    # def addAtIndex(self, index: int, val: int) -> None:
    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            return self.addAtHead(val)
        if index > self.length:
            return
        if index < 0:
            if index == -1 and not self.head:
                self.addAtHead(val)
                return
            else:
                return
        n = self._get_node(index-1)
        temp = n.next
        new = Node(val)
        new.next = temp
        n.next = new
        self.length += 1
    # def deleteAtIndex(self, index: int) -> None:
    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        # print('length=', self.length, index)
        if index > self.length - 1:
            return
        if index < 0:
            if index == -1 and self.length == 1:
                self.head = None
                return
            else:
                return
        if index == 0:
            self.head = self.head.next
            self.length -= 1
            return
        pre = self._get_node(index-1)
        n = pre.next
        if not n.next:
            pre.next = None
        else:
            pre.next = n.next
        self.length -= 1
        
# MyLinkedList linkedList = new MyLinkedList();
# linkedList.addAtHead(1);
# linkedList.addAtTail(3);
# linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
# linkedList.get(1);            // returns 2
# linkedList.deleteAtIndex(1);  // now the linked list is 1->3
# linkedList.get(1);            // returns 3

# Your MyLinkedList object will be instantiated and called as such:



# obj = MyLinkedList()
# obj.addAtHead(1)
# obj.addAtTail(3)
# obj.addAtIndex(1, 2)
# print(obj.get(1))
# obj.deleteAtIndex(1)
# print(obj.get(1))
# print(obj)


# obj.addAtHead(1)
# obj.addAtIndex(1, 2)
# print(obj.get(1))
# print(obj.get(0))
# print(obj.get(2))
# print(obj)

# print(obj.get(0))
# obj.addAtIndex(1, 2)
# print(obj.get(0))
# print(obj.get(1))
# obj.addAtIndex(0, 1)
# print(obj.get(0))
# print(obj.get(1))
# print(obj)




# obj.addAtHead(38)
# obj.addAtHead(45)
# obj.deleteAtIndex(2)

# obj.addAtIndex(-1, 0)
# print(obj.get(0))
# obj.deleteAtIndex(-1)

# print(obj)