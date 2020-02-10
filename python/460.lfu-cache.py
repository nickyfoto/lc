#
# @lc app=leetcode id=460 lang=python3
#
# [460] LFU Cache
#
# https://leetcode.com/problems/lfu-cache/description/
#
# algorithms
# Hard (32.21%)
# Likes:    1069
# Dislikes: 103
# Total Accepted:    59.9K
# Total Submissions: 185.9K
# Testcase Example:  '["LFUCache","put","put","get","put","get","get","put","get","get","get"]\n' +
#  '[[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]'
#
# Design and implement a data structure for Least Frequently Used (LFU) cache.
# It should support the following operations: get and put.
# 
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reaches its capacity, it should invalidate the least
# frequently used item before inserting a new item. For the purpose of this
# problem, when there is a tie (i.e., two or more keys that have the same
# frequency), the least recently used key would be evicted.
# 
# Note that the number of times an item is used is the number of calls to the
# get and put functions for that item since it was inserted. This number is set
# to zero when the item is removed.
# 
# 
# 
# Follow up:
# Could you do both operations in O(1) time complexity?
# 
# 
# 
# Example:
# 
# 
# LFUCache cache = new LFUCache( 2 /* capacity */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.get(3);       // returns 3.
# cache.put(4, 4);    // evicts key 1.
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
# 
# 
# 
# 
#

# @lc code=start
from collections import OrderedDict, defaultdict
class Node:
    def __init__(self, key, val, count):
        self.key = key
        self.val = val
        self.count = count

    def __str__(self):
        return f'[key: {self.key}, val: {self.val}, count: {self.count}]'

class LFUCache:

    def __init__(self, capacity: int):
        self.key2node = {}
        self.count2node = defaultdict(OrderedDict)
        self.capacity = capacity
        self.minCount = None

    def get(self, key: int) -> int:
        """
        How to update count?
            1. get node from key2node
            2. delete the node using the key and node.count
            3. node.count += 1
            4. put node back to count2node
            5. if count2node[minCount] is empty:
                increase minCount by 1
        """
        if key not in self.key2node:
            return -1
        node = self.key2node[key]
        del self.count2node[node.count][key]
        node.count += 1
        self.count2node[node.count][key] = node

        if not self.count2node[self.minCount]:
            self.minCount += 1
        return node.val

    def _remove(self):
        """
        when last=False, OrderedDict is FIFO
        meaning, for the nodes with the same minCount, popitem will pop
        the oldest item
        """
        k, _ = self.count2node[self.minCount].popitem(last=False)
        del self.key2node[k]
    
    def put(self, key: int, value: int) -> None:
        """
        How to add new key val?
            1. add node to count2node[1] and key2node
            2. set minCount to 1

        How to update exist key?
            1. update key2node
            2. call self.get(key) to update count
        """
        if not self.capacity:
            return
        if key in self.key2node:
            self.key2node[key].val = value
            self.get(key)
            return
        if len(self.key2node) == self.capacity:
            self._remove()
        
        self.count2node[1][key] = self.key2node[key] = Node(key, value, 1)
        self.minCount = 1
        return
        

def inspect(cache):
    print('minCount=', cache.minCount)
    for k, n in cache.key2node.items():
        print('key2node:', k, n)
    for k, n in cache.count2node.items():
        print('count2node:', k, [(key, val.__str__()) for (key, val) in n.items()])
    print()
# Your LFUCache object will be instantiated and called as such:
# capacity = 2
# cache = LFUCache(capacity)
# cache.put(1, 1)
# inspect(cache)
# cache.put(2, 2)
# inspect(cache)
# print(cache.get(1) == 1)#;       // returns 1
# inspect(cache)
# cache.put(3, 3)#;    // evicts key 2
# inspect(cache)
# print(cache.get(2) == -1)#;       // returns -1 (not found)
# cache.get(3);       // returns 3.
# cache.put(4, 4);    // evicts key 1.
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
