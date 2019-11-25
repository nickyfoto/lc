#
# @lc app=leetcode id=1089 lang=python3
#
# [1089] Duplicate Zeros
#
# https://leetcode.com/problems/duplicate-zeros/description/
#
# algorithms
# Easy (59.05%)
# Total Accepted:    10.2K
# Total Submissions: 17.3K
# Testcase Example:  '[1,0,2,3,0,4,5,0]'
#
# Given a fixed length array arr of integers, duplicate each occurrence of
# zero, shifting the remaining elements to the right.
# 
# Note that elements beyond the length of the original array are not written.
# 
# Do the above modifications to the input array in place, do not return
# anything from your function.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,0,2,3,0,4,5,0]
# Output: null
# Explanation: After calling your function, the input array is modified to:
# [1,0,0,2,3,0,0,4]
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3]
# Output: null
# Explanation: After calling your function, the input array is modified to:
# [1,2,3]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= arr.length <= 10000
# 0 <= arr[i] <= 9
# 
#
class Solution:
    # def duplicateZeros(self, arr: List[int]) -> None:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        i = 0
        while i < n:
        # for i in range(n):
            if arr[i] == 0 and i < n-1:
                # print(arr[i+2:])
                # print(arr[i+1:n-1])
                arr[i+2:] = arr[i+1:n-1]

                arr[i+1] = 0
                # print(arr)
                i += 2
            else:
                i += 1
        # print(arr)

# s = Solution()
# arr = [1,0,2,3,0,4,5,0]
# print(s.duplicateZeros(arr))

# arr = [1,2,3]
# print(s.duplicateZeros(arr))

# arr = [1,5,2,0,6,8,0,6,0] # [1,5,2,0,0,6,8,0,0]
# print(s.duplicateZeros(arr))

















        
