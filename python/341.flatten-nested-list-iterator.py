#
# @lc app=leetcode id=341 lang=python
#
# [341] Flatten Nested List Iterator
#
# https://leetcode.com/problems/flatten-nested-list-iterator/description/
#
# algorithms
# Medium (48.99%)
# Total Accepted:    122.5K
# Total Submissions: 250K
# Testcase Example:  '[[1,1],2,[1,1]]'
#
# Given a nested list of integers, implement an iterator to flatten it.
# 
# Each element is either an integer, or a list -- whose elements may also be
# integers or other lists.
# 
# Example 1:
# 
# 
# 
# Input: [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]
# Explanation: By calling next repeatedly until hasNext returns
# false, 
# the order of elements returned by next should be: [1,1,2,1,1].
# 
# 
# Example 2:
# 
# 
# Input: [1,[4,[6]]]
# Output: [1,4,6]
# Explanation: By calling next repeatedly until hasNext returns
# false, 
# the order of elements returned by next should be: [1,4,6].
# 
# 
# 
# 
#
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.l = []
        def flatten(l):
            if type(l) == list:
                for element in l:
                    if element.isInteger():
                        self.l.append(element.getInteger())
                    else:
                        flatten(element.getList())
            else:
                if l.isInteger():
                    self.l.append(l.getInteger())
                else:
                    flatten(l.getList())

        flatten(nestedList)
        # print(self.l)
    
    def next(self):
        """
        :rtype: int
        """
        # for i in self.l:
            # yield self.l[i]
        if self.hasNext():
            # print(len(self.l))
            return self.l.pop(0)

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.l:
            return True
        return False

# Your NestedIterator object will be instantiated and called as such:

# l = [1,[4,[6]]]
# l = [[1,1],2,[1,1]]
# nestedList = l
# i, v = NestedIterator(nestedList), []
# while i.hasNext():
#     v.append(i.next())
# print(v)


# print(i.hasNext())
# print(i.next())
# print(i.getL())


# def flatten(l):
#     for i in range(len(l)):
#         if type(l[i]) == list:
#             l = l[:i] + flatten(l[i]) + flatten(l[i+1:])
#     return l


# print(flatten(l))






# class NestedIterator(object):

#     def __init__(self):
#         self.l = [1,2,3]
        
    
#     def next(self):
#         for i in self.l:
#             yield self.l[i]


# n = NestedIterator()
# print(list(n.next()))















