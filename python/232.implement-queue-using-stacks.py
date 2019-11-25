#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#
# https://leetcode.com/problems/implement-queue-using-stacks/description/
#
# algorithms
# Easy (43.52%)
# Total Accepted:    152.7K
# Total Submissions: 349.9K
# Testcase Example:  '["MyQueue","push","push","peek","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# Implement the following operations of a queue using stacks.
# 
# 
# push(x) -- Push element x to the back of queue.
# pop() -- Removes the element from in front of queue.
# peek() -- Get the front element.
# empty() -- Return whether the queue is empty.
# 
# 
# Example:
# 
# 
# MyQueue queue = new MyQueue();
# 
# queue.push(1);
# queue.push(2);  
# queue.peek();  // returns 1
# queue.pop();   // returns 1
# queue.empty(); // returns false
# 
# Notes:
# 
# 
# You must use only standard operations of a stack -- which means only push to
# top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, stack may not be supported natively. You may
# simulate a stack by using a list or deque (double-ended queue), as long as
# you use only standard operations of a stack.
# You may assume that all operations are valid (for example, no pop or peek
# operations will be called on an empty queue).
# 
# 
#

class Stack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.insert(0, x)

    def pop(self):
        return self.stack.pop(0)

    def peek(self):
        return self.stack[0]

    def size(self):
        return len(self.stack)

    def empty(self):
        """
        Returns whether the queue is empty.
        """
        if self.size() == 0:
            return True
        return False

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = Stack()
        # print(self.q.stack)
    # def push(self, x: int) -> None:
    def push(self, x):
        """
        Push element x to the back of queue.
        """
        self.q.push(x)

    # def pop(self) -> int:
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        """
        stack = []
        while self.q.size() > 1:
            stack.insert(0, self.q.pop())
        res = self.q.pop()
        for i in stack:
            self.q.push(i)
        return res

    # def peek(self) -> int:
    def peek(self):
        """
        Get the front element.
        """
        stack = []
        while self.q.size() > 0:
            stack.insert(0, self.q.pop())
        res = stack[0]
        for i in stack:
            # print('i=', i)
            self.q.push(i)
        return res

    # def empty(self) -> bool:
    def empty(self):
        """
        Returns whether the queue is empty.
        """
        if self.q.size() == 0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# queue = MyQueue()

# queue.push(1);
# queue.push(2);  
# print(queue.peek()) #  // returns 1
# print(queue.pop()) #   // returns 1
# print(queue.empty()) # // returns false

# queue = MyQueue()

# queue.push(1)
# queue.push(2)  
# queue.push(3)  
# # print(queue.peek()) #  // returns 1
# print(queue.pop()) #   // returns 1
# print(queue.pop()) #   // returns 2
# print(queue.pop()) #   // returns 3
# print(queue.empty()) # // returns True

