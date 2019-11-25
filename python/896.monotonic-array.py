#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#
# https://leetcode.com/problems/monotonic-array/description/
#
# algorithms
# Easy (55.32%)
# Total Accepted:    47.2K
# Total Submissions: 85.2K
# Testcase Example:  '[1,2,2,3]'
#
# An array is monotonic if it is either monotone increasing or monotone
# decreasing.
# 
# An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array
# A is monotone decreasing if for all i <= j, A[i] >= A[j].
# 
# Return true if and only if the given array A is monotonic.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,2,3]
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: [6,5,4,4]
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# Input: [1,3,2]
# Output: false
# 
# 
# 
# Example 4:
# 
# 
# Input: [1,2,4,5]
# Output: true
# 
# 
# 
# Example 5:
# 
# 
# Input: [1,1,1]
# Output: true
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 50000
# -100000 <= A[i] <= 100000
# 
# 
# 
# 
# 
# 
# 
#
class Solution:
    # def isMonotonic(self, A: List[int]) -> bool:
    def isMonotonic(self, A):
        n = len(A)
        if n == 1:
            return True

        def checkIncrease(A):
            i = 0
            while i < n - 1:
                if A[i+1] < A[i]:
                    return False
                i += 1
            return True
        def checkDecrease(A):
            i = 0
            while i < n - 1:
                if A[i+1] > A[i]:
                    return False
                i += 1
            return True

        i = 1
        first = A[0]
        while i < n and A[i] == first:
            i += 1
        if i == n:
            return True
        if A[i] > first:
            return checkIncrease(A)
        else:
            return checkDecrease(A)
        # print('i=', i, A[i])
        

# s = Solution()
# A = [1,2,2,3]
# print(s.isMonotonic(A))
# A = [6,5,4,4]
# print(s.isMonotonic(A))
# A = [1,3,2]
# print(s.isMonotonic(A))
# A = [1,2,4,5]
# print(s.isMonotonic(A))
# A = [1,1,1]
# print(s.isMonotonic(A))
