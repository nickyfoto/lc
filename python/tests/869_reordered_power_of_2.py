#
# @lc app=leetcode id=869 lang=python3
#
# [869] Reordered Power of 2
#
# https://leetcode.com/problems/reordered-power-of-2/description/
#
# algorithms
# Medium (51.75%)
# Likes:    162
# Dislikes: 76
# Total Accepted:    11.9K
# Total Submissions: 22.9K
# Testcase Example:  '1'
#
# Starting with a positive integer N, we reorder the digits in any order
# (including the original order) such that the leading digit is not zero.
# 
# Return true if and only if we can do this in a way such that the resulting
# number is a power of 2.
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
# Input: 1
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: 10
# Output: false
# 
# 
# 
# Example 3:
# 
# 
# Input: 16
# Output: true
# 
# 
# 
# Example 4:
# 
# 
# Input: 24
# Output: false
# 
# 
# 
# Example 5:
# 
# 
# Input: 46
# Output: true
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 10^9
# 
# 
# 
# 
# 
# 
# 
#

# @lc code=start
from collections import Counter
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        """

        """
        sn = str(N)
        l = len(sn)
        nc = Counter(sn)
        i = 0
        p2 = str(2**i)
        # print(l, p2)
        while len(p2) <= l:
            if len(p2) == l and Counter(p2) == nc:
                return True
            p2 = str(2**i)
            i += 1
        return False
# @lc code=end
