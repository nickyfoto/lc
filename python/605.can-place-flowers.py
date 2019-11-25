#
# @lc app=leetcode id=605 lang=python3
#
# [605] Can Place Flowers
#
# https://leetcode.com/problems/can-place-flowers/description/
#
# algorithms
# Easy (30.93%)
# Total Accepted:    64.7K
# Total Submissions: 208.6K
# Testcase Example:  '[1,0,0,0,1]\n1'
#
# Suppose you have a long flowerbed in which some of the plots are planted and
# some are not. However, flowers cannot be planted in adjacent plots - they
# would compete for water and both would die.
# 
# Given a flowerbed (represented as an array containing 0 and 1, where 0 means
# empty and 1 means not empty), and a number n, return if n new flowers can be
# planted in it without violating the no-adjacent-flowers rule.
# 
# Example 1:
# 
# Input: flowerbed = [1,0,0,0,1], n = 1
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: flowerbed = [1,0,0,0,1], n = 2
# Output: False
# 
# 
# 
# Note:
# 
# The input array won't violate no-adjacent-flowers rule.
# The input array size is in the range of [1, 20000].
# n is a non-negative integer which won't exceed the input array size.
# 
# 
#
class Solution:
    # def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    def canPlaceFlowers(self, flowerbed, n):
        lf = len(flowerbed)
        count = 0
        for i in range(lf):
            # print('i=', i, flowerbed[i-1], flowerbed[i], flowerbed[i+1], i+1<n)
            # if (i == 0 and flowerbed[0] == 0 and flowerbed[i+1] == 0):
                # flowerbed[i+1] == 1
                # count
            if  (i+1 < lf and i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0) or \
                (i+1 < lf and flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0) or \
                (i == lf-1 and flowerbed[i-1] == 0 and flowerbed[i] == 0):
                flowerbed[i] = 1
                # print('here')
                count += 1

        # print(flowerbed)
        return n <= count

# s = Solution()
# flowerbed = [1,0,0,0,1]
# n = 1
# print(s.canPlaceFlowers(flowerbed, n))
# n = 2
# print(s.canPlaceFlowers(flowerbed, n))
# flowerbed = [0,0,0,0,1]
# n = 2
# print(s.canPlaceFlowers(flowerbed, n))
