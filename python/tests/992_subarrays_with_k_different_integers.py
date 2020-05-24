#
# @lc app=leetcode id=992 lang=python3
#
# [992] Subarrays with K Different Integers
#
# https://leetcode.com/problems/subarrays-with-k-different-integers/description/
#
# algorithms
# Hard (46.91%)
# Likes:    860
# Dislikes: 18
# Total Accepted:    24.3K
# Total Submissions: 51.3K
# Testcase Example:  '[1,2,1,2,3]\n2'
#
# Given an array A of positive integers, call a (contiguous, not necessarily
# distinct) subarray of A good if the number of different integers in that
# subarray is exactly K.
# 
# (For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)
# 
# Return the number of good subarrays of A.
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [1,2,1,2,3], K = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2],
# [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
# 
# 
# Example 2:
# 
# 
# Input: A = [1,2,1,3,4], K = 3
# Output: 3
# Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3],
# [2,1,3], [1,3,4].
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 20000
# 1 <= A[i] <= A.length
# 1 <= K <= A.length
# 
#

# @lc code=start
from collections import Counter
class Solution:
    def subarraysWithKDistinct(self, A, K):
        window1 = Counter()
        window2 = Counter()
        res = l1 = l2 = 0
        for i, a in enumerate(A):
            window1[a] += 1
            window2[a] += 1
            while len(window1) > K:
                window1[A[l1]] -= 1
                if window1[A[l1]] == 0:
                    del window1[A[l1]]
                l1 += 1
            while len(window2) >= K:
                window2[A[l2]] -= 1
                if window2[A[l2]] == 0:
                    del window2[A[l2]]
                l2 += 1
            res += l2 - l1
        return res
# @lc code=end
