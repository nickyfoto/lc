#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#
# https://leetcode.com/problems/counting-bits/description/
#
# algorithms
# Medium (64.81%)
# Total Accepted:    177.8K
# Total Submissions: 272.8K
# Testcase Example:  '2'
#
# Given a non negative integer number num. For every numbers i in the range 0 ≤
# i ≤ num calculate the number of 1's in their binary representation and return
# them as an array.
# 
# Example 1:
# 
# 
# Input: 2
# Output: [0,1,1]
# 
# Example 2:
# 
# 
# Input: 5
# Output: [0,1,1,2,1,2]
# 
# 
# Follow up:
# 
# 
# It is very easy to come up with a solution with run time
# O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a
# single pass?
# Space complexity should be O(n).
# Can you do it like a boss? Do it without using any builtin function like
# __builtin_popcount in c++ or in any other language.
# 
#
class Solution:
    # def countBits(self, num: int) -> List[int]:
    def countBits(self, num):
              #0, 1
        res = [0, 1]
        if num == 0:
            return [0]
        if num == 1:
            return res
        def isPowerof2(i):
            while i > 1:
                i, r = divmod(i, 2)
                if r == 1:
                    return False
            return True
        # print(isPowerof2(2))
        # print(isPowerof2(4))
        # print(isPowerof2(6))
        for i in range(2, num+1):
            if isPowerof2(i):
                res.append(1)
                p = i
            else:
                res.append(1+res[i-p])
        return res
# s = Solution()
# num = 2
# print(s.countBits(num))
# num = 5
# print(s.countBits(num))