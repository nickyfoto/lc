#
# @lc app=leetcode id=728 lang=python3
#
# [728] Self Dividing Numbers
#
# https://leetcode.com/problems/self-dividing-numbers/description/
#
# algorithms
# Easy (69.70%)
# Total Accepted:    76.6K
# Total Submissions: 109.5K
# Testcase Example:  '1\n22'
#
# 
# A self-dividing number is a number that is divisible by every digit it
# contains.
# 
# For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 ==
# 0, and 128 % 8 == 0.
# 
# Also, a self-dividing number is not allowed to contain the digit zero.
# 
# Given a lower and upper number bound, output a list of every possible self
# dividing number, including the bounds if possible.
# 
# Example 1:
# 
# Input: 
# left = 1, right = 22
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
# 
# 
# 
# Note:
# The boundaries of each input argument are 1 .
# 
#
class Solution:
    # def selfDividingNumbers(self, left: int, right: int) -> List[int]:
    def selfDividingNumbers(self, left, right):
        res = []
        def getNumDigits(num):
            i = 1
            while num // 10**i > 0:
                i += 1
            return i
        # print(getNumDigits(100))
        for num in range(left, right+1):
            numDigists = getNumDigits(num)
            if numDigists == 1:
                res.append(num)
            else:
                num_copy = num
                d, r = divmod(num, 10**(numDigists-1))
                while r > 0:
                    d, r = divmod(num, 10**(numDigists-1))
                    # print(num_copy, num, d, r)
                    if d == 0 or (r >= 10 and r % 10 == 0) or num_copy % d != 0:
                        break
                    num -= d * 10**(numDigists-1)
                    numDigists -= 1
                # print('here', num)
                if num == 0:
                    res.append(num_copy)
        return res

# s = Solution()
# left = 1
# right = 212
# print(s.selfDividingNumbers(left, right))




