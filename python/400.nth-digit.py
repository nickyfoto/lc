#
# @lc app=leetcode id=400 lang=python3
#
# [400] Nth Digit
#
# https://leetcode.com/problems/nth-digit/description/
#
# algorithms
# Easy (30.22%)
# Total Accepted:    47.4K
# Total Submissions: 156.4K
# Testcase Example:  '3'
#
# Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8,
# 9, 10, 11, ... 
# 
# Note:
# n is positive and will fit within the range of a 32-bit signed integer (n <
# 231).
# 
# 
# Example 1:
# 
# Input:
# 3
# 
# Output:
# 3
# 
# 
# 
# Example 2:
# 
# Input:
# 11
# 
# Output:
# 0
# 
# Explanation:
# The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0,
# which is part of the number 10.
# 
# 
#
class Solution:
    # def findNthDigit(self, n: int) -> int:
    def findNthDigit(self, n, debug=False):
        # for i in range(6):
        i = 0
        while True:
            limit = 9 * (i+1) * 10**i
            print('limit=', limit) if debug else None
            if n <= limit:
                print('i=', i) if debug else None
                w = i
                order = n
                while w >= 0:
                    # print('w=', w, int(9 * w * 10**(w-1)))
                    order -= int(9 * w * 10**(w-1))
                    w -= 1

                # order = int(n - )
                print('order', order) if debug else None
                d, v = divmod(order, i+1)
                print('d=', d, 'v=', v) if debug else None
                print('i=', i) if debug else None
                start = int(10**i- 1)
                print('start', start) if debug else None
                if v:
                    number = start + d + 1
                else:
                    number = start + d
                print('number', number) if debug else None
                if v == 0:
                    res = int(str(number)[-1])
                else:
                    res = int(str(number)[v-1])
                print('res', res) if debug else None
                return res
            i += 1

































        
