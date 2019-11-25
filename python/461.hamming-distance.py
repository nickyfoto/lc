#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#
# https://leetcode.com/problems/hamming-distance/description/
#
# algorithms
# Easy (70.22%)
# Total Accepted:    237.3K
# Total Submissions: 337.5K
# Testcase Example:  '1\n4'
#
# The Hamming distance between two integers is the number of positions at which
# the corresponding bits are different.
# 
# Given two integers x and y, calculate the Hamming distance.
# 
# Note:
# 0 ≤ x, y < 231.
# 
# 
# Example:
# 
# Input: x = 1, y = 4
# 
# Output: 2
# 
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
# ⁠      ↑   ↑
# 
# The above arrows point to positions where the corresponding bits are
# different.
# 
# 
#
class Solution:
    # def hammingDistance(self, x: int, y: int) -> int:
    def hammingDistance(self, x, y):
        count = 0
        for i in bin(x ^ y)[2:]:
            if i == '1':
                count += 1
        return count
        # print(1 ^ 4)


# s = Solution()
# x = 1
# y = 4
# print(s.hammingDistance(x, y))
        
