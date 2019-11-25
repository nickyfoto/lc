#
# @lc app=leetcode id=941 lang=python3
#
# [941] Valid Mountain Array
#
# https://leetcode.com/problems/valid-mountain-array/description/
#
# algorithms
# Easy (35.39%)
# Total Accepted:    22.2K
# Total Submissions: 62.8K
# Testcase Example:  '[2,1]'
#
# Given an array A of integers, return true if and only if it is a valid
# mountain array.
# 
# Recall that A is a mountain array if and only if:
# 
# 
# A.length >= 3
# There exists some i with 0 < i < A.length - 1 such that:
# 
# A[0] < A[1] < ... A[i-1] < A[i] 
# A[i] > A[i+1] > ... > A[A.length - 1]
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [2,1]
# Output: false
# 
# 
# 
# Example 2:
# 
# 
# Input: [3,5,5]
# Output: false
# 
# 
# 
# Example 3:
# 
# 
# Input: [0,3,2,1]
# Output: true
# 
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= A.length <= 10000
# 0 <= A[i] <= 10000 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
#
class Solution:
    # def validMountainArray(self, A: List[int]) -> bool:
    def validMountainArray(self, A):
        n = len(A)
        if n < 3:
            return False
        m = max(A)
        m_idx = A.index(m)
        if m_idx == 0 or m_idx == n-1:
            return False
        for i in range(m_idx):
            if A[i] >= A[i+1]:
                return False
        for i in range(m_idx, n):
            if i + 1 < n and A[i] <= A[i+1]:
                return False
        return True

# s = Solution()
# A = [0,3,2,1]
# print(s.validMountainArray(A))
# A = [3,5,5]
# print(s.validMountainArray(A))