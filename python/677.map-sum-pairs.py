#
# @lc app=leetcode id=677 lang=python3
#
# [677] Map Sum Pairs
#
# https://leetcode.com/problems/map-sum-pairs/description/
#
# algorithms
# Medium (52.13%)
# Total Accepted:    29.1K
# Total Submissions: 55.9K
# Testcase Example:  '["MapSum", "insert", "sum", "insert", "sum"]\n[[], ["apple",3], ["ap"], ["app",2], ["ap"]]'
#
# 
# Implement a MapSum class with insert, and sum methods.
# 
# 
# 
# For the method insert, you'll be given a pair of (string, integer). The
# string represents the key and the integer represents the value. If the key
# already existed, then the original key-value pair will be overridden to the
# new one.
# 
# 
# 
# For the method sum, you'll be given a string representing the prefix, and you
# need to return the sum of all the pairs' value whose key starts with the
# prefix.
# 
# 
# Example 1:
# 
# Input: insert("apple", 3), Output: Null
# Input: sum("ap"), Output: 3
# Input: insert("app", 2), Output: Null
# Input: sum("ap"), Output: 5
# 
# 
# 
#

class Node:
    def __init__(self, R):
        self.next = [None] * R
        self.val = None

class MapSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.R = 256
        self.root = None

    def put(self, x, key, val, d):
        # print('key=', key, 'd=', d, 'val=', val)
        if not x:
            x = Node(self.R)
        if d == len(key):
            x.val = val
            return x
        c = key[d]
        x.next[ord(c)] = self.put(x.next[ord(c)], key, val, d+1)
        return x

    def insert(self, key: str, val: int) -> None:
        self.root = self.put(self.root, key, val, 0)

    def _get(self, x, key, d):
        if d == len(key):
            return x
        c = key[d]
        if x:
            return self._get(x.next[ord(c)], key, d+1)
        else:
            return None
    
    def get(self, key):
        # print('get root', self.root)
        x = self._get(self.root, key, 0)
        if x:
            return x.val
        else:
            return None

    def collect(self, node, prefix, res):
        if not node:
            return
        # print('here', node.val)
        if node.val != None:
            res.append(prefix)
        for c in range(256):
            prefix += chr(c)
            self.collect(node.next[c], prefix, res)
            prefix = prefix[:-1]

    def getPrefix(self, prefix):
        res = []
        x = self._get(self.root, prefix, 0)
        # print(x)
        self.collect(x, prefix, res)
        return res
        # print(x)
    def sum(self, prefix: str) -> int:
        results = self.getPrefix(prefix)
        s = 0
        for r in results:
            s += self.get(r)
        return s

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert('apple', 3)
# obj.insert('app', 2)
# print(obj.get('apple'))
# print(obj.sum('ap'))
# print(obj.sum('bb'))
# print(obj.getPrefix('ap'))
# param_2 = obj.sum(prefix)
