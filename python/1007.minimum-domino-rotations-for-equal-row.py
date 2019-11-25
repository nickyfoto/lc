#
# @lc app=leetcode id=1007 lang=python3
#
# [1007] Minimum Domino Rotations For Equal Row
#
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/description/
#
# algorithms
# Medium (50.72%)
# Total Accepted:    16.1K
# Total Submissions: 31.7K
# Testcase Example:  '[2,1,2,4,2,2]\n[5,2,6,2,3,2]'
#
# In a row of dominoes, A[i] and B[i] represent the top and bottom halves of
# the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on
# each half of the tile.)
# 
# We may rotate the i-th domino, so that A[i] and B[i] swap values.
# 
# Return the minimum number of rotations so that all the values in A are the
# same, or all the values in B are the same.
# 
# If it cannot be done, return -1.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
# Output: 2
# Explanation: 
# The first figure represents the dominoes as given by A and B: before we do
# any rotations.
# If we rotate the second and fourth dominoes, we can make every value in the
# top row equal to 2, as indicated by the second figure.
# 
# 
# Example 2:
# 
# 
# Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
# Output: -1
# Explanation: 
# In this case, it is not possible to rotate the dominoes to make one row of
# values equal.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A[i], B[i] <= 6
# 2 <= A.length == B.length <= 20000
# 
# 
#
class Solution:
    # def minDominoRotations(self, A: List[int], B: List[int]) -> int:
    def minDominoRotations(self, A, B) -> int:
        n = len(A)
        

        def dict_indices(A):
            d = {}
            for i in range(n):
                if A[i] not in d:
                    d[A[i]] = [i]
                else:
                    d[A[i]].append(i)
            return d
        da = dict_indices(A)
        db = dict_indices(B)
        # print(da)
        # print(db)

        la = sorted(list(da.keys()), key = lambda x: len(da[x]), reverse=True)
        lb = sorted(list(db.keys()), key = lambda x: len(db[x]), reverse=True)

        # print(la)
        # print(lb)

        for i in la:
            for j in lb:
                if len(da[i]) >= len(db[j]):
                    # print('here', da[i], db[j])
                    # counter_part = [B[idx] == i for idx in range(n) if idx not in da[i]]
                    # if all(counter_part):
                        # return len(counter_part)
                    for idx in set(range(0,n)) - set(da[i]):
                        # print(idx)
                        if B[idx] != i:
                            break
                    else:
                        return n - len(da[i])
                else:
                    # counter_part = [A[idx] == j for idx in range(n) if idx not in db[j]]
                    # if all(counter_part):
                        # return len(counter_part)
                    for idx in set(range(0,n)) - set(db[j]):
                        # print(idx)
                        if A[idx] != j:
                            break
                    else:
                        return n - len(db[j])
        return -1


# s = Solution()
# A = [2,1,2,4,2,2]
# B = [5,2,6,2,3,2]
# print(s.minDominoRotations(A, B))




# A = [3,5,1,2,3]
# B = [3,6,3,3,4]
# print(s.minDominoRotations(A, B))



# A = [2]
# B = [2]
# print(s.minDominoRotations(A, B))







