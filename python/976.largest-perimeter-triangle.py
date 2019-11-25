#
# @lc app=leetcode id=976 lang=python3
#
# [976] Largest Perimeter Triangle
#
# https://leetcode.com/problems/largest-perimeter-triangle/description/
#
# algorithms
# Easy (56.98%)
# Total Accepted:    14.7K
# Total Submissions: 25.8K
# Testcase Example:  '[2,1,2]'
#
# Given an array A of positive lengths, return the largest perimeter of a
# triangle with non-zero area, formed from 3 of these lengths.
# 
# If it is impossible to form any triangle of non-zero area, return 0.
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
# Input: [2,1,2]
# Output: 5
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,2,1]
# Output: 0
# 
# 
# 
# Example 3:
# 
# 
# Input: [3,2,3,4]
# Output: 10
# 
# 
# 
# Example 4:
# 
# 
# Input: [3,6,2,3]
# Output: 8
# 
# 
# 
# 
# Note:
# 
# 
# 3 <= A.length <= 10000
# 1 <= A[i] <= 10^6
# 
# 
# 
# 
# 
#
class Solution:
    # def largestPerimeter(self, A: List[int]) -> int:
    def largestPerimeter(self, A):
        if len(A) < 3:
            return 0
        A.sort(reverse=True)
        n = len(A)
        i = 0
        while i + 2 < n:
            if A[i+1] + A[i+2] > A[i]:
                return sum(A[i:i+3])
            i += 1
        return 0

# s = Solution()


# A = [2,1,2]
# # Output: 5
# print(s.largestPerimeter(A))



# A = [1,2,1]
# # Output: 0
# print(s.largestPerimeter(A))


# A = [3,2,3,4]
# # Output: 10
# print(s.largestPerimeter(A))



# A = [3,6,2,3]
# # Output: 8
# print(s.largestPerimeter(A))








