#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#
# https://leetcode.com/problems/min-stack/description/
#
# algorithms
# Easy (37.29%)
# Total Accepted:    311.5K
# Total Submissions: 832.1K
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]'
#
# Design a stack that supports push, pop, top, and retrieving the minimum
# element in constant time.
# 
# 
# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
# 
# 
# 
# 
# Example:
# 
# 
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> Returns -3.
# minStack.pop();
# minStack.top();      --> Returns 0.
# minStack.getMin();   --> Returns -2.
# 
# 
# 
# 
#
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        if not self.stack:
            self.stack.append((x, x))
        else:
            # find prev min
            self.stack.append((x, min(x, self.stack[-1][1])))
    
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    # def top(self) -> int:
    def top(self):
        if self.stack:
            return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]





# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(2147483646)
# obj.push(2147483646)
# obj.push(2147483647)
# print(obj.top())
# obj.pop()
# print(obj.getMin())
# obj.pop()
# print(obj.getMin())
# obj.pop()
# obj.push(2147483647)
# print(obj.top())
# print(obj.getMin())
# param_3 = obj.top()
# param_4 = obj.getMin()


# print('[null,null,null,null,2147483647,null,2147483646,null,2147483646,null,null,2147483647,2147483646,null,-2147483648,-2147483648,null,2147483647]'=='[null,null,null,null,2147483647,null,2147483646,null,2147483646,null,null,2147483647,2147483647,null,-2147483648,-2147483648,null,2147483647]')
