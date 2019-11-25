#
# @lc app=leetcode id=1013 lang=python3
#
# [1013] Partition Array Into Three Parts With Equal Sum
#
# https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/description/
#
# algorithms
# Easy (55.39%)
# Total Accepted:    14.9K
# Total Submissions: 26.8K
# Testcase Example:  '[0,2,1,-6,6,-7,9,1,2,0,1]'
#
# Given an array A of integers, return true if and only if we can partition the
# array into three non-empty parts with equal sums.
# 
# Formally, we can partition the array if we can find indexes i+1 < j with
# (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1]
# + ... + A[A.length - 1])
# 
# 
# 
# Example 1:
# 
# 
# Input: [0,2,1,-6,6,-7,9,1,2,0,1]
# Output: true
# Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
# 
# 
# 
# Example 2:
# 
# 
# Input: [0,2,1,-6,6,7,9,-1,2,0,1]
# Output: false
# 
# 
# 
# Example 3:
# 
# 
# Input: [3,3,6,5,-2,2,5,1,-9,4]
# Output: true
# Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 3 <= A.length <= 50000
# -10000 <= A[i] <= 10000
# 
#
class Solution:
    # def canThreePartsEqualSum(self, A: List[int]) -> bool:
    def canThreePartsEqualSum(self, A):
        n = len(A)
        if n < 3:
            return False
        # print(sum(A))
        sa = sum(A)
        target, r = divmod(sa, 3)
        # print(target)
        if r != 0:
            return False
        count = 0
        total = A[0]
        i = 1
        while i < n:
            while total != target:
                if i == len(A):
                    return False
                total += A[i]
                i += 1
            if total == target:
                count += 1
                A = A[i:]
                if count == 3:
                    if not A or sum(A) == 0:
                        return True
                    else:
                        return False
                total = A[0]
                i = 1
        if A:
            return False




# s = Solution()
# A = [0,2,1,-6,6,-7,9,1,2,0,1]
# print(s.canThreePartsEqualSum(A))
# A = [0,2,1,-6,6,7,9,-1,2,0,1]
# print(s.canThreePartsEqualSum(A))

# A = [3,3,6,5,-2,2,5,1,-9,4]
# print(s.canThreePartsEqualSum(A))


# A = [12,-4,16,-5,9,-3,3,8,0]
# print(s.canThreePartsEqualSum(A)) # true



























        
