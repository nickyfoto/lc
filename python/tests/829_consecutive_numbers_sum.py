#
# @lc app=leetcode id=829 lang=python3
#
# [829] Consecutive Numbers Sum
#
# https://leetcode.com/problems/consecutive-numbers-sum/description/
#
# algorithms
# Hard (35.78%)
# Likes:    231
# Dislikes: 340
# Total Accepted:    17K
# Total Submissions: 47.4K
# Testcase Example:  '5'
#
# Given a positive integer N, how many ways can we write it as a sum of
# consecutive positive integers?
# 
# Example 1:
# 
# 
# Input: 5
# Output: 2
# Explanation: 5 = 5 = 2 + 3
# 
# Example 2:
# 
# 
# Input: 9
# Output: 3
# Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
# 
# Example 3:
# 
# 
# Input: 15
# Output: 4
# Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
# 
# Note: 1 <= N <= 10 ^ 9.
# 
#

# @lc code=start
from math import sqrt
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        res = 1
        # for a in range(1, N // 2 + 1):
        #     # print('a=', a, sqrt((2*a-1)**2 + 4 * 2 * N))
        #     st = sqrt((2*a-1)**2 + 4 * 2 * N)
        #     if st - int(st) == 0:
        #         res += 1
        # return res
        for n in range(2, int(sqrt(2 * N))+1):
            if ( N - n*(n - 1)  / 2) % n == 0:
                res += 1
        return res
# @lc code=end
