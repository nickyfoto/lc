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

    """
    Your runtime beats 20.82 % of python3 submissions
    Your memory usage beats 8.7 % of python3 submissions (18.1 MB)
    """
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




from bisect import insort
class KthLargest:
    """
    ✔ Your runtime beats 32.04 % of python3 submissions
    ✔ Your memory usage beats 8.7 % of python3 submissions (18 MB)
    """
    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        insort(self.nums, val)
        return self.nums[- self.k]

from heapq import heapify, heappop, heappush, heapreplace

class KthLargest:
    """
    ✔ Your runtime beats 85.36 % of python3 submissions
    ✔ Your memory usage beats 8.7 % of python3 submissions (17.5 MB)
    """
    def __init__(self, k, nums):
        self.nums = nums
        self.k = k
        heapify(self.nums)
        while len(self.nums) > k:
            heappop(self.nums)
    
    def add(self, val):
        if len(self.nums) < self.k:
            heappush(self.nums, val)
        elif val > self.nums[0]:
            heapreplace(self.nums, val)
        return self.nums[0]














