#
# @lc app=leetcode id=981 lang=python3
#
# [981] Time Based Key-Value Store
#
# https://leetcode.com/problems/time-based-key-value-store/description/
#
# algorithms
# Medium (51.49%)
# Total Accepted:    22.8K
# Total Submissions: 44.2K
# Testcase Example:  '["TimeMap","set","get","get","set","get","get"]\n[[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]'
#
# Create a timebased key-value store class TimeMap, that supports two
# operations.
# 
# 1. set(string key, string value, int timestamp)
# 
# 
# Stores the key and value, along with the given timestamp.
# 
# 
# 2. get(string key, int timestamp)
# 
# 
# Returns a value such that set(key, value, timestamp_prev) was called
# previously, with timestamp_prev <= timestamp.
# If there are multiple such values, it returns the one with the largest
# timestamp_prev.
# If there are no values, it returns the empty string ("").
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: inputs = ["TimeMap","set","get","get","set","get","get"], inputs =
# [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
# Output: [null,null,"bar","bar",null,"bar2","bar2"]
# Explanation:   
# TimeMap kv;   
# kv.set("foo", "bar", 1); // store the key "foo" and value "bar" along with
# timestamp = 1   
# kv.get("foo", 1);  // output "bar"   
# kv.get("foo", 3); // output "bar" since there is no value corresponding to
# foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 ie
# "bar"   
# kv.set("foo", "bar2", 4);   
# kv.get("foo", 4); // output "bar2"   
# kv.get("foo", 5); //output "bar2"   
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: inputs = ["TimeMap","set","set","get","get","get","get","get"], inputs
# =
# [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
# Output: [null,null,null,"","high","high","low","low"]
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# All key/value strings are lowercase.
# All key/value strings have length in the range [1, 100]
# The timestamps for all TimeMap.set operations are strictly increasing.
# 1 <= timestamp <= 10^7
# TimeMap.set and TimeMap.get functions will be called a total of 120000 times
# (combined) per test case.
# 
# 
#
import bisect
class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.d:
            self.d[key] = [[value], [timestamp]]
        else:
            # timestamp is new
            idx = bisect.bisect_left(self.d[key][1], timestamp)
            # if idx >= len(self.d[key][0]):
            if idx < len(self.d[key][0]):
                if timestamp == self.d[key][1][idx]:
                # print(idx)
                    self.d[key][0][idx] = value
                    return
            
            self.d[key][1].insert(idx, timestamp)
            self.d[key][0].insert(idx, value)
            # print(self.d)

    def get(self, key: str, timestamp: int) -> str:
        if key in self.d:
            idx = bisect.bisect_left(self.d[key][1], timestamp)
            # print(idx)
            if idx >= len(self.d[key][0]):
                # print('here')
                idx = -1
                return self.d[key][0][idx]
            if timestamp < self.d[key][1][0]:
                # print(timestamp, self.d[key][1][idx])
                return ""
            if self.d[key][1][idx] == timestamp:
                return self.d[key][0][idx]
            # print(idx)
            return self.d[key][0][idx-1]

# Your TimeMap object will be instantiated and called as such:
# kv = TimeMap()
# kv.set('foo', 'a', 1)
# kv.set('foo', 'b', 1)
# kv.set('foo', 'c', 2)
# kv.set('foo', 'd', 2)
# print(kv.d)



# kv = TimeMap()
# kv.set("foo", "bar", 1)
# print(kv.get("foo", 1))
# print(kv.get("foo", 3))
# kv.set("foo", "bar2", 4)
# print(kv.get("foo", 4))
# print(kv.get("foo", 5))


# kv = TimeMap()
# kv.set('love', 'high', 10)
# kv.set('love', 'low', 20)
# # print(kv.d)
# print(kv.get("love", 5))
# print(kv.get("love", 10))
# print(kv.get("love", 15))
# print(kv.get("love", 20))
# print(kv.get("love", 25))
