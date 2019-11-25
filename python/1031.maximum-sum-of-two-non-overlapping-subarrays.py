#
# @lc app=leetcode id=1031 lang=python3
#
# [1031] Maximum Sum of Two Non-Overlapping Subarrays
#
# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/description/
#
# algorithms
# Medium (55.02%)
# Total Accepted:    8.1K
# Total Submissions: 14.8K
# Testcase Example:  '[0,6,5,2,2,5,1,9,4]\n1\n2'
#
# Given an array A of non-negative integers, return the maximum sum of elements
# in two non-overlapping (contiguous) subarrays, which have lengths L and M.
# (For clarification, the L-length subarray could occur before or after the
# M-length subarray.)
# 
# Formally, return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1])
# + (A[j] + A[j+1] + ... + A[j+M-1]) and either:
# 
# 
# 0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
# 0 <= j < j + M - 1 < i < i + L - 1 < A.length.
# 
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
# Input: A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
# Output: 20
# Explanation: One choice of subarrays is [9] with length 1, and [6,5] with
# length 2.
# 
# 
# 
# Example 2:
# 
# 
# Input: A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
# Output: 29
# Explanation: One choice of subarrays is [3,8,1] with length 3, and [8,9] with
# length 2.
# 
# 
# 
# Example 3:
# 
# 
# Input: A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
# Output: 31
# Explanation: One choice of subarrays is [5,6,0,9] with length 4, and [3,8]
# with length 3.
# 
# 
# 
# 
# Note:
# 
# 
# L >= 1
# M >= 1
# L + M <= A.length <= 1000
# 0 <= A[i] <= 1000
# 
# 
# 
# 
# 
#
class Solution:
    # def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
    def maxSumTwoNoOverlap(self, A, L: int, M: int) -> int:


        def prefix_sum(arr, size):
            # print(arr)
            n = len(arr)
            mx = sum(arr[:size])
            s = mx
            # mx_idx = 0
            for i in range(n-size):
                # print(arr[i:i+size])
                # print(arr[i+size])
                s = s - arr[i] + arr[i+size]
                if s > mx:
                    mx = s
                    # mx_idx = i+1
            # print(arr, mx)
            return mx#, mx_idx
                # print(s)

        def recur(A, L, M):

            n = len(A)
            mx = sum(A[:L]) + prefix_sum(A[L:], M)
            s = sum(A[:L])
            for i in range(n-L):
                # print(A[i:i+L])
                s = s - A[i] + A[i+L]

                # print(s)
                m = prefix_sum(A[i+L+1:], M)
                mx = max(mx, s + m)
            return mx


        # print()
        


        # for i in range(n-L+1):
            # print(sum(A[i:i+L]))
        # def recur(A, L, M):
        #     l, l_idx = prefix_sum(A, L)
        #     m1, _ = prefix_sum(A[:l_idx], M)
        #     m2, _ = prefix_sum(A[l_idx+L:], M)
        #         # print(m, m_idx)
        #     return l + max(m1, m2)
        res1 = recur(A, L, M)
        res2 = recur(A, M, L)
        # print(res1, res2)
        return max(res1, res2)

# s = Solution()
# A = [0,6,5,2,2,5,1,9,4]
# L = 1
# M = 2
# print(s.maxSumTwoNoOverlap(A, L, M))


# A = [3,8,1,3,2,1,8,9,0]
# L = 3
# M = 2
# print(s.maxSumTwoNoOverlap(A, L, M))


# A = [2,1,5,6,0,9,5,0,3,8]
# L = 4
# M = 3
# print(s.maxSumTwoNoOverlap(A, L, M))



# A = [8,20,6,2,20,17,6,3,20,8,12]
# L = 5
# M = 4
# print(s.maxSumTwoNoOverlap(A, L, M)) # 108





















        
