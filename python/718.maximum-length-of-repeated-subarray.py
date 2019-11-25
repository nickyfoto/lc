#
# @lc app=leetcode id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (47.30%)
# Total Accepted:    40.8K
# Total Submissions: 86.1K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# Given two integer arrays A and B, return the maximum length of an subarray
# that appears in both arrays.
# 
# Example 1:
# 
# 
# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation: 
# The repeated subarray with maximum length is [3, 2, 1].
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100
# 
# 
# 
# 
#
class Solution:
    # def findLength(self, A: List[int], B: List[int]) -> int:
    def findLength(self, A, B):

        L = [[x] * len(A) for x in [0]*len(B)]


        for r in range(len(B)):
            for c in range(len(A)):
                # print(L[r][c])
                if A[c] == B[r]:
                    if r == 0 or c == 0:
                        L[r][c] = 1
                    else:
                        L[r][c] = 1 + L[r-1][c-1]
        # print(L)
        return max([max(r) for r in L])


# s = Solution()


# A = [1,2,3,2,1]
# B = [3,2,1,4,7]
# print(s.findLength(A, B))





# A = [1]
# B = [1,2,3]
# print(s.findLength(A, B))




































        
