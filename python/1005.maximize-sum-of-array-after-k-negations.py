#
# @lc app=leetcode id=1005 lang=python3
#
# [1005] Maximize Sum Of Array After K Negations
#
# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/
#
# algorithms
# Easy (49.61%)
# Total Accepted:    12K
# Total Submissions: 24.1K
# Testcase Example:  '[4,2,3]\n1'
#
# Given an array A of integers, we must modify the array in the following way:
# we choose an i and replace A[i] with -A[i], and we repeat this process K
# times in total.  (We may choose the same index i multiple times.)
# 
# Return the largest possible sum of the array after modifying it in this
# way.
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [4,2,3], K = 1
# Output: 5
# Explanation: Choose indices (1,) and A becomes [4,-2,3].
# 
# 
# 
# Example 2:
# 
# 
# Input: A = [3,-1,0,2], K = 3
# Output: 6
# Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].
# 
# 
# 
# Example 3:
# 
# 
# Input: A = [2,-3,-1,5,-4], K = 2
# Output: 13
# Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 10000
# 1 <= K <= 10000
# -100 <= A[i] <= 100
# 
# 
#
class Solution:
    # def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
    def largestSumAfterKNegations(self, A, K):
        A.sort()
        num_negs = len([x for x in A if x < 0])
        # print('num_negs=', num_negs)
        if not num_negs:
            if K % 2 == 0:
                return sum(A)
            else:
                return sum(A[1:]) - A[0]
        else:
            if K <= num_negs:
                return - sum(A[:K]) + sum(A[K:])
            else:
                if 0 in A:
                    return - sum(A[:num_negs]) + sum(A[num_negs:])
                else:
                    if (K - num_negs) % 2 == 1:
                        return - sum(A[:num_negs]) + sum(A[num_negs:]) - 2 * min([abs(x) for x in A])
                    else:
                        return - sum(A[:num_negs]) + sum(A[num_negs:]) 
# s = Solution()
# A = [4,2,3]
# K = 1
# print(s.largestSumAfterKNegations(A, K) == 5)

# A = [3,-1,0,2]
# K = 3
# print(s.largestSumAfterKNegations(A, K) == 6)

# A = [2,-3,-1,5,-4]
# K = 2
# print(s.largestSumAfterKNegations(A, K) == 13)






















        
