#
# @lc app=leetcode id=1027 lang=python3
#
# [1027] Longest Arithmetic Sequence
#
# https://leetcode.com/problems/longest-arithmetic-sequence/description/
#
# algorithms
# Medium (50.80%)
# Total Accepted:    17.1K
# Total Submissions: 33.7K
# Testcase Example:  '[3,6,9,12]'
#
# Given an array A of integers, return the length of the longest arithmetic
# subsequence in A.
# 
# Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0
# <= i_1 < i_2 < ... < i_k <= A.length - 1, and that a sequence B is arithmetic
# if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).
# 
# 
# 
# Example 1:
# 
# 
# Input: [3,6,9,12]
# Output: 4
# Explanation: 
# The whole array is an arithmetic sequence with steps of length = 3.
# 
# 
# 
# Example 2:
# 
# 
# Input: [9,4,7,2,10]
# Output: 3
# Explanation: 
# The longest arithmetic subsequence is [4,7,10].
# 
# 
# 
# Example 3:
# 
# 
# Input: [20,1,15,3,10,5,8]
# Output: 4
# Explanation: 
# The longest arithmetic subsequence is [20,15,10,5].
# 
# 
# 
# 
# 
# Note:
# 
# 
# 2 <= A.length <= 2000
# 0 <= A[i] <= 10000
# 
# 
#
class Solution:
    # def longestArithSeqLength(self, A: List[int]) -> int:
    def longestArithSeqLength(self, A) -> int:

        n = len(A)
        # val = {diff: length with this diff}
        vals = [{} for i in range(n)]
        mx = 2
        for i in range(n):
            for j in range(i):
                d = vals[j]
                diff = A[i] - A[j]
                if diff not in d:
                    vals[i][diff] = 2
                else:
                    vals[i][diff] = d[diff] + 1
                    mx = max(d[diff]+1, mx)
        return mx
        # return max([max(val.values()) for val in vals if val])

s = Solution()

A = [3,6,9,12]
print(s.longestArithSeqLength(A) == 4)


A = [9,4,7,2,10]
print(s.longestArithSeqLength(A) == 3)


A = [20,1,15,3,10,5,8]
print(s.longestArithSeqLength(A) == 4)















        
