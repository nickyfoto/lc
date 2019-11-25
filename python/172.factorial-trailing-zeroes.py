#
# @lc app=leetcode id=172 lang=python3
#
# [172] Factorial Trailing Zeroes
#
# https://leetcode.com/problems/factorial-trailing-zeroes/description/
#
# algorithms
# Easy (37.32%)
# Total Accepted:    155.8K
# Total Submissions: 417K
# Testcase Example:  '3'
#
# Given an integer n, return the number of trailing zeroes in n!.
# 
# Example 1:
# 
# 
# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# 
# Example 2:
# 
# 
# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# 
# Note: Your solution should be in logarithmic time complexity.
# 
#
class Solution:
    # def trailingZeroes(self, n: int) -> int:
    """
    def trailingZeroes(self, n):
        i = 1
        f = 1
        count = 0
        Trail = 100000
        while i < n:
            # print(f, i)
            i += 1
            f *= i
            # print('f=', f, 'i=', i)
            d, r = divmod(f, 10)
            if r == 0:
                # count how many 0 d have
                w = 1
                # if d % 10 == 0:
                    # print('here d=', d)
                while d % 10**w == 0:
                    w += 1
                    # d = d // 10
                    # print('new d=', d)
                if w == 1:
                    # print('w=', w)
                    count += w
                    # f = d % 10
                    f = d % Trail

                    # f = r
                else:
                    # print('d=', d)
                    # print('w=', w)
                    count += w
                    # f = (d // 10**(w-1)) % 10
                    f = (d // 10**(w-1)) % Trail
                    # print('f=', f)
                    # f = d % 10**(w)
                # if d % 10 != 0:
                #     print('if d=', d)
                #     count += 1
                #     f = d % 10
                # else:
                    # print('d=', d)
            else:
                # f = r
                f = f % Trail
            
            # print(f, i)
        # print(count)
        return count
    """
    def trailingZeroes(self, n):
        count = 0
        i = 1
        while n >= 5**i:
            count += n // 5**i
            i += 1
        return count