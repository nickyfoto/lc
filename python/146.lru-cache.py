#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Medium (29.69%)
# Likes:    4498
# Dislikes: 193
# Total Accepted:    428.1K
# Total Submissions: 1.4M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
#  '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design and implement a data structure for Least Recently Used (LRU) cache. It
# should support the following operations: get and put.
# 
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently
# used item before inserting a new item.
# 
# The cache is initialized with a positive capacity.
# 
# Follow up:
# Could you do both operations in O(1) time complexity?
# 
# Example:
# 
# 
# LRUCache cache = new LRUCache( 2 /* capacity */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
# 
# 
# 
# 
#

# @lc code=start
from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache:
            v = self.cache[key]
            self.cache.move_to_end(key)
            return v
        return -1

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            oldest = next(iter(self.cache))
            del self.cache[oldest]


# Your LRUCache object will be instantiated and called as such:
# capacity = 2
# cache = LRUCache(capacity)
# cache.put(1, 1)
# print('counter=', cache.counter)
# cache.put(2, 2)
# print('counter=', cache.counter)
# print(cache.get(1) == 1)#       // returns 1
# print('counter=', cache.counter, cache.cache)
# cache.put(3, 3)#;    #// evicts key 2
# print('counter=', cache.counter, cache.cache)
# print(cache.get(2) == -1) #       // returns -1 (not found)
# print('counter=', cache.counter, cache.cache)
# cache.put(4, 4)#;    // evicts key 1
# print('counter=', cache.counter, cache.cache)
# print(cache.get(1) ==  -1)#;       // returns -1 (not found)
# print(cache.get(3) == 3)#;       // returns 3
# print(cache.get(4) == 4)#;       // returns 4
# print('counter=', cache.counter, cache.cache)
# @lc code=end

# capacity = 3
# cache = LRUCache(capacity)
# for i in range(1,5):
#     cache.put(i, i)
# print(cache.get(4) == 4)
# print(cache.cache)
# print(cache.get(3) == 3)
# print(cache.cache)
# print(cache.get(2) == 2)
# print(cache.cache)
# print(cache.get(1) == -1)
# print(cache.cache)
# cache.put(5,5)
# print(cache.cache)
# print(cache.get(1) == -1)
# print(cache.cache)
# print(cache.get(2) == 2)
# print(cache.cache)
# print(cache.get(3) == 3)
# print(cache.cache)