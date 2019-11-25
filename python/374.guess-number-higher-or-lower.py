#
# @lc app=leetcode id=374 lang=python
#
# [374] Guess Number Higher or Lower
#
# https://leetcode.com/problems/guess-number-higher-or-lower/description/
#
# algorithms
# Easy (39.18%)
# Total Accepted:    106K
# Total Submissions: 269.3K
# Testcase Example:  '10\n6'
#
# We are playing the Guess Game. The game is as follows:
# 
# I pick a number from 1 to n. You have to guess which number I picked.
# 
# Every time you guess wrong, I'll tell you whether the number is higher or
# lower.
# 
# You call a pre-defined API guess(int num) which returns 3 possible results
# (-1, 1, or 0):
# 
# 
# -1 : My number is lower
# ⁠1 : My number is higher
# ⁠0 : Congrats! You got it!
# 
# 
# Example :
# 
# 
# 
# Input: n = 10, pick = 6
# Output: 6
# 
# 
# 
#
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        def bs(low, high, debug=False):
            if high - low == 1:
                if guess(low) > 0:
                    return high
                else:
                    return low
            if debug:
                print(low, high)
            
            g = low + (high-low)//2
            if debug:
                print(g)
            feed_back = guess(g)
            if feed_back > 0:
                return bs(g, high)
            elif feed_back < 0:
                # print('here')
                return bs(low, g)
            else:
                return g

        return bs(1, n)




# def guess(num):
#     if num < TARGET:
#         return 1
#     elif num > TARGET:
#         return -1
#     else:
#         return 0
# s = Solution()
# TARGET = 1
# n = 1
# print(s.guessNumber(n))

# TARGET = 50
# n = 1000
# print(s.guessNumber(n))

# TARGET = 1
# n = 2
# print(s.guessNumber(n))

# TARGET = 2
# n = 2
# print(s.guessNumber(n))

# TARGET = 3
# n = 1
# print(s.guessNumber(n))
# TARGET = 3
# n = 3
# print(s.guessNumber(n))
# TARGET = 2
# n = 3
# print(s.guessNumber(n))

