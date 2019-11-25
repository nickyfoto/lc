#
# @lc app=leetcode id=565 lang=python3
#
# [565] Array Nesting
#
# https://leetcode.com/problems/array-nesting/description/
#
# algorithms
# Medium (53.60%)
# Total Accepted:    40.7K
# Total Submissions: 75.9K
# Testcase Example:  '[5,4,0,3,1,6,2]'
#
# A zero-indexed array A of length N contains all integers from 0 to N-1. Find
# and return the longest length of set S, where S[i] = {A[i], A[A[i]],
# A[A[A[i]]], ... } subjected to the rule below.
# 
# Suppose the first element in S starts with the selection of element A[i] of
# index = i, the next element in S should be A[A[i]], and then A[A[A[i]]]… By
# that analogy, we stop adding right before a duplicate element occurs in
# S.
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [5,4,0,3,1,6,2]
# Output: 4
# Explanation: 
# A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.
# 
# One of the longest S[K]:
# S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
# 
# 
# 
# 
# Note:
# 
# 
# N is an integer within the range [1, 20,000].
# The elements of A are all distinct.
# Each element of A is an integer within the range [0, N-1].
# 
# 
#
class Solution:
    # def arrayNesting(self, nums: List[int]) -> int:
    def arrayNesting(self, nums):

        A = nums
        n = len(A)
        # L = [1]*n
        idx = 0
        max_d = {}
        mx = 0
        element_other_than_max_d = {}
        while idx < n:
            if A[idx] not in max_d and A[idx] not in element_other_than_max_d:
                d = { A[idx]: 1 }
                i = idx
                # print('i=', i, A[A[i]], A[i])
                while A[A[i]] not in d and A[A[i]] not in element_other_than_max_d:
                    d[A[A[i]]] = 1
                    i = A[i]
                # print(idx, d)
                ld = len(d)
                if ld > mx:
                    mx, max_d = ld, d
                
                element_other_than_max_d.update(d)
                # print(element_other_than_max_d)
                d = {}
            # else:
            idx += 1
        # print(L)

        return mx









































        
