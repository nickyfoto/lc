#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
# https://leetcode.com/problems/powx-n/description/
#
# algorithms
# Medium (29.03%)
# Likes:    1146
# Dislikes: 2609
# Total Accepted:    403.4K
# Total Submissions: 1.4M
# Testcase Example:  '2.00000\n10'
#
# Implement pow(x, n), which calculates x raised to the power n (x^n).
# 
# Example 1:
# 
# 
# Input: 2.00000, 10
# Output: 1024.00000
# 
# 
# Example 2:
# 
# 
# Input: 2.10000, 3
# Output: 9.26100
# 
# 
# Example 3:
# 
# 
# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
# 
# 
# Note:
# 
# 
# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
# 
# 
#

# @lc code=start
class Solution:
    # def myPow(self, x: float, n: int) -> float:
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1.0 / x
        return self.myPow(x * x, n // 2) if n % 2 == 0 else x * self.myPow(x * x, n // 2)

    def myPow_me(self, x, n):
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n < 0:
            return self.myPow(1./x, -n)
        r = 1
        old_n = n
        old_x = x
        while n // 2 > 0:
            x *= x
            n //= 2
            r <<= 1
        x *= self.myPow(old_x, old_n - r)
        return x
# @lc code=end
