#
# @lc app=leetcode id=891 lang=python3
#
# [891] Sum of Subsequence Widths
#
# https://leetcode.com/problems/sum-of-subsequence-widths/description/
#
# algorithms
# Hard (30.42%)
# Likes:    161
# Dislikes: 88
# Total Accepted:    6.6K
# Total Submissions: 21.5K
# Testcase Example:  '[2,1,3]'
#
# Given an array of integers A, consider all non-empty subsequences of A.
# 
# For any sequence S, let the width of S be the difference between the maximum
# and minimum element of S.
# 
# Return the sum of the widths of all subsequences of A. 
# 
# As the answer may be very large, return the answer modulo 10^9 + 7.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [2,1,3]
# Output: 6
# Explanation:
# Subsequences are [1], [2], [3], [2,1], [2,3], [1,3], [2,1,3].
# The corresponding widths are 0, 0, 0, 1, 1, 2, 2.
# The sum of these widths is 6.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 20000
# 1 <= A[i] <= 20000
# 
# 
# 
#

# @lc code=start
# from lcpy import List
# from copy import deepcopy
# class Solution:
#     # def sumSubseqWidths(self, A: List[int]) -> int:
#     def sumSubseqWidths(self, A) -> int:
#         """
#         if length is n then there are 
#         """
#         res = 0
#         n = len(A)

#         class Subsequence:
#             """
#             record attributes of each subsequence instead of 
#             forming real subseqences
#             """
#             def __init__(self, index, arr):
#                 self.length = 1
#                 self.mx = arr
#                 self.mn = arr
#                 self.width = 0
#                 self.index = index
#                 # self.temp = [arr]

#             def update(self, arr):
#                 self.mx = max(self.mx, arr.mx)
#                 self.mn = min(self.mn, arr.mn)
#                 self.width =  self.mx - self.mn
#                 self.length += 1
#                 self.index = arr.index
#                 # self.temp.extend(arr.temp)

#             def __str__(self):
#                 return  f"width: {self.width}," \
#                         f" index: {self.index}," \
#                         f"max: {self.mx}," \
#                         f"min: {self.mn}," \
#                         f"length: {self.length}," \
#                         # f"temp: {self.temp}"



#         # print([[a] for a in A])
#         subs = [Subsequence(i, a) for i, a in enumerate(A)]
#         q = subs.copy()
#         sub = q.pop(0)
#         while sub.length <= n:
#             # print(sub)
#             res += sub.width
#             for i in range(sub.index + 1, n):
#                 sub_copy = deepcopy(sub)
#                 sub_copy.update(subs[i])
#                 q.append(sub_copy)
#             if q:
#                 sub = q.pop(0)
#             else:
#                 break
        
#         return res


class Solution:
    def sumSubseqWidths(self, A):
        MOD = 10**9 + 7
        N = len(A)
        A.sort()

        pow2 = [1]
        for i in range(1, N):
            pow2.append(pow2[-1] * 2 % MOD)
        # print(pow2)
        ans = 0
        for i, x in enumerate(A):
            ans = (ans + (pow2[i] - pow2[N-1-i]) * x) % MOD
        return ans

# @lc code=end
