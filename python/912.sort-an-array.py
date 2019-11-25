#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#
# https://leetcode.com/problems/sort-an-array/description/
#
# algorithms
# Medium (62.90%)
# Total Accepted:    29.8K
# Total Submissions: 47.4K
# Testcase Example:  '[5,2,3,1]'
#
# Given an array of integers nums, sort the array in ascending order.
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [5,2,3,1]
# Output: [1,2,3,5]
# 
# 
# Example 2:
# 
# 
# Input: [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 10000
# -50000 <= A[i] <= 50000
# 
# 
#
import random
random.seed(1)
class Solution:
    # def sortArray(self, nums: List[int]) -> List[int]:
    def sortArray(self, nums):



        
        def Partition(A, left, right):
            pivot = A[left]
            l_idx = left
            # print(A, left, right, pivot)
            for r_idx in range(l_idx+1, right+1):
                if A[r_idx] <= pivot:
                    l_idx += 1
                    A[r_idx], A[l_idx] = A[l_idx], A[r_idx]
            A[left], A[l_idx] = A[l_idx], A[left]
            # print(A, l_idx)
            return l_idx

        def RandomizedQuickSort(A, left, right):
            if left > right:
                return
            r = random.randint(left, right)
            A[left], A[r] = A[r], A[left]
            m = Partition(A, left, right)
            RandomizedQuickSort(A, left, m - 1)
            RandomizedQuickSort(A, m+1, right)
            return A

        n = len(nums)

        return RandomizedQuickSort(nums, 0, n - 1)


s = Solution()
nums = [5,2,3,1]
# print(s.sortArray(nums))



nums = [5,1,1,2,0,0]
print(s.sortArray(nums))

































        
