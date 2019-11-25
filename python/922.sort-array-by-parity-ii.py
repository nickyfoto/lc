#
# @lc app=leetcode id=922 lang=python3
#
# [922] Sort Array By Parity II
#
# https://leetcode.com/problems/sort-array-by-parity-ii/description/
#
# algorithms
# Easy (66.92%)
# Total Accepted:    41.6K
# Total Submissions: 62.1K
# Testcase Example:  '[4,2,5,7]'
#
# Given an array A of non-negative integers, half of the integers in A are odd,
# and half of the integers are even.
# 
# Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is
# even, i is even.
# 
# You may return any answer array that satisfies this condition.
# 
# 
# 
# Example 1:
# 
# 
# Input: [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been
# accepted.
# 
# 
# 
# 
# Note:
# 
# 
# 2 <= A.length <= 20000
# A.length % 2 == 0
# 0 <= A[i] <= 1000
# 
# 
# 
# 
# 
#
class Solution:
    # def sortArrayByParityII(self, A: List[int]) -> List[int]:
    def sortArrayByParityII(self, A):
        n = len(A)
        for i in range(n):
            if i % 2 == 0 and A[i] % 2 != 0:
                # find next even number in odd position
                for o in range(i+1, n, 2):
                    if A[o] % 2 == 0:
                        A[i], A[o] = A[o], A[i]
                        break
            if i % 2 != 0 and A[i] % 2 == 0:
                # find next odd number in even postion
                for e in range(i+1, n, 2):
                    if A[e] % 2 != 0:
                        A[i], A[e] = A[e], A[i]
                        break
        return A

s = Solution()
A = [4,2,5,7]
print(s.sortArrayByParityII(A))
































        
