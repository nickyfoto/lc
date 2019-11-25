#
# @lc app=leetcode id=703 lang=python3
#
# [703] Kth Largest Element in a Stream
#
# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/
#
# algorithms
# Easy (46.50%)
# Total Accepted:    34.6K
# Total Submissions: 74.3K
# Testcase Example:  '["KthLargest","add","add","add","add","add"]\n[[3,[4,5,8,2]],[3],[5],[10],[9],[4]]'
#
# Design a class to find the kth largest element in a stream. Note that it is
# the kth largest element in the sorted order, not the kth distinct element.
# 
# Your KthLargest class will have a constructor which accepts an integer k and
# an integer array nums, which contains initial elements from the stream. For
# each call to the method KthLargest.add, return the element representing the
# kth largest element in the stream.
# 
# Example:
# 
# 
# int k = 3;
# int[] arr = [4,5,8,2];
# KthLargest kthLargest = new KthLargest(3, arr);
# kthLargest.add(3);   // returns 4
# kthLargest.add(5);   // returns 5
# kthLargest.add(10);  // returns 5
# kthLargest.add(9);   // returns 8
# kthLargest.add(4);   // returns 8
# 
# 
# Note: 
# You may assume that nums' length ≥ k-1 and k ≥ 1.
# 
#

class MinPQ:
    """docstring for MaxPQ"""
    def __init__(self):
        self.pq = [0]
        self.length = 0

    def swim(self, k):
        # print("self.pq=", self.pq)
        # print('k=', k)
        while k > 1 and self.pq[k//2] > self.pq[k]:
            self.pq[k//2], self.pq[k] = self.pq[k], self.pq[k//2]
            k = k // 2
        # print("after swim self.pq=", self.pq)

    def sink(self, k):
        while 2 * k <= self.length:
            j = 2 * k
            if j < self.length and self.pq[j] > self.pq[j+1]:
                j += 1
            if self.pq[k] <= self.pq[j]:
                break
            self.pq[k], self.pq[j] = self.pq[j], self.pq[k]
            k = j

    def min(self):
        return self.pq[1]

    def delMin(self):
        m = self.pq[1]
        self.pq[-1], self.pq[1] = self.pq[1], self.pq[-1]
        self.pq = self.pq[:-1]
        self.length -= 1
        self.sink(1)
        return m

    def add(self, num):
        self.pq.append(num)
        self.length += 1
        self.swim(self.length)
        # print(self.pq)

    def getLength(self):
        return self.length

    def __str__(self):
        return str(self.pq)

class KthLargest:

    # def __init__(self, k: int, nums: List[int]):
    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        self.pq = MinPQ()
        for n in self.nums:
            self.pq.add(n)
    # def add(self, val: int) -> int:
    def add(self, val):
        self.pq.add(val)
        while self.pq.getLength() > self.k: 
            self.pq.delMin()
        return self.pq.min()


"""
class KthLargest:

    # def __init__(self, k: int, nums: List[int]):
    def __init__(self, k, nums):
        self.k = k
        self.nums = sorted(nums)[- self.k:]

    # def add(self, val: int) -> int:
    def add(self, val):
        if len(self.nums) < self.k:
            self.nums.append(val)
            self.nums.sort()
            return self.nums[0]
        kth = self.nums[0]
        if val <= kth:
            return kth
        elif val > kth:
            # for i in range(self.k):
            i = 0
            while i < self.k and self.nums[i] < val:
                i += 1
            # print('here', i)
            self.nums.insert(i, val)
            self.nums = self.nums[1:]
            # print('here', self.nums)
            return self.nums[0]
"""

# Your KthLargest object will be instantiated and called as such:
# k = 3
# nums = [4,5,8,2]
# obj = KthLargest(k, nums)
# print(obj.add(3))
# print(obj.add(5))
# print(obj.add(10))
# print(obj.add(9))
# print(obj.add(4))


# k = 1
# nums = []
# obj = KthLargest(k, nums)
# print(obj.add(-3))
# print(obj.add(-2))


# k = 2
# nums = [0]
# obj = KthLargest(k, nums)
# print(obj.add(-1))



# k = 3
# nums = [5, -1]
# obj = KthLargest(k, nums)
# print(obj.add(2))
















