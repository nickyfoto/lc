#
# @lc app=leetcode id=225 lang=python3
#
# [225] Implement Stack using Queues
#
# https://leetcode.com/problems/implement-stack-using-queues/description/
#
# algorithms
# Easy (39.46%)
# Total Accepted:    132K
# Total Submissions: 333.6K
# Testcase Example:  '["MyStack","push","push","top","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# Implement the following operations of a stack using queues.
# 
# 
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# empty() -- Return whether the stack is empty.
# 
# 
# Example:
# 
# 
# MyStack stack = new MyStack();
# 
# stack.push(1);
# stack.push(2);  
# stack.top();   // returns 2
# stack.pop();   // returns 2
# stack.empty(); // returns false
# 
# Notes:
# 
# 
# You must use only standard operations of a queue -- which means only push to
# back, peek/pop from front, size, and is empty operations are valid.
# Depending on your language, queue may not be supported natively. You may
# simulate a queue by using a list or deque (double-ended queue), as long as
# you use only standard operations of a queue.
# You may assume that all operations are valid (for example, no pop or top
# operations will be called on an empty stack).
# 
# 
#

class MyQueue:
    def __init__(self):
        # print('ok')
        self.q = []
    def push(self, x):
        self.q.append(x)

    def pop(self):
        return self.q.pop(0)

    def size(self):
        # print(self.q)
        return len(self.q)

    def empty(self):
        if self.size() == 0:
            return True
        return False

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = MyQueue()
        # print(dir(self.stack))
        # print('here')
    # def push(self, x: int) -> None:
    def push(self, x):
        """
        Push element x onto stack.
        """
        temp = []
        while self.stack.size() > 0:
            temp.append(self.stack.pop())
        self.stack.push(x)
        for i in temp:
            self.stack.push(i)

    # def pop(self) -> int:
    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.stack.pop()

    # def top(self) -> int:
    def top(self):
        """
        Get the top element.
        """
        temp = []
        while self.stack.size() > 0:
            temp.append(self.stack.pop())
        # print(temp)
        res = temp[0]
        for i in temp:
            self.stack.push(i)
        return res

    # def empty(self) -> bool:
    def empty(self):
        """
        Returns whether the stack is empty.
        """
        return self.stack.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(1)
# obj.push(2)
# print(obj.top()) # 2
# print(obj.pop()) # 2
# print(obj.empty()) # false
