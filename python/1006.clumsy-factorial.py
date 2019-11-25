#
# @lc app=leetcode id=1006 lang=python3
#
# [1006] Clumsy Factorial
#
# https://leetcode.com/problems/clumsy-factorial/description/
#
# algorithms
# Medium (53.56%)
# Total Accepted:    8.8K
# Total Submissions: 16.3K
# Testcase Example:  '4'
#
# Normally, the factorial of a positive integer n is the product of all
# positive integers less than or equal to n.  For example, factorial(10) = 10 *
# 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.
# 
# We instead make a clumsy factorial: using the integers in decreasing order,
# we swap out the multiply operations for a fixed rotation of operations:
# multiply (*), divide (/), add (+) and subtract (-) in this order.
# 
# For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.  However,
# these operations are still applied using the usual order of operations of
# arithmetic: we do all multiplication and division steps before any addition
# or subtraction steps, and multiplication and division steps are processed
# left to right.
# 
# Additionally, the division that we use is floor division such that 10 * 9 / 8
# equals 11.  This guarantees the result is an integer.
# 
# Implement the clumsy function as defined above: given an integer N, it
# returns the clumsy factorial of N.
# 
# 
# 
# Example 1:
# 
# 
# Input: 4
# Output: 7
# Explanation: 7 = 4 * 3 / 2 + 1
# 
# 
# Example 2:
# 
# 
# Input: 10
# Output: 12
# Explanation: 12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 10000
# -2^31 <= answer <= 2^31 - 1  (The answer is guaranteed to fit within a 32-bit
# integer.)
# 
# 
#
class Solution:
    def clumsy(self, N: int) -> int:

        def four_set(n):
            if n == 0: return 0
            if n < 4: return 1
            else: return n - (n-1)*(n-2) // (n-3) + four_set(n-4)
        # print(recur(4))
        def recur(n):
            if n == 1: return 1
            if n == 2: return 2
            if n == 3: return 6
            else: return n * (n-1) // (n-2) + four_set(n-3)
        return recur(N)

s = Solution()
print(s.clumsy(2) == 2)
print(s.clumsy(3) == 6)
print(s.clumsy(4) == 7)
print(s.clumsy(5) == 7)
print(s.clumsy(6) == 8)
print(s.clumsy(7) == 6)
print(s.clumsy(8) == 9)
print(s.clumsy(9) == 11)
print(s.clumsy(10) == 12)






# c = it.cycle([1,2,3,4])

# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))
# print(next(c))













        
