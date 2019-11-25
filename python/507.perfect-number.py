#
# @lc app=leetcode id=507 lang=python3
#
# [507] Perfect Number
#
# https://leetcode.com/problems/perfect-number/description/
#
# algorithms
# Easy (34.07%)
# Total Accepted:    40.3K
# Total Submissions: 117.9K
# Testcase Example:  '28'
#
# We define the Perfect Number is a positive integer that is equal to the sum
# of all its positive divisors except itself. 
# 
# Now, given an integer n, write a function that returns true when it is a
# perfect number and false when it is not.
# 
# 
# Example:
# 
# Input: 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# 
# 
# 
# Note:
# The input number n will not exceed 100,000,000. (1e8)
# 
#
class Solution:
    # def checkPerfectNumber(self, num: int) -> bool:
    
    def checkPerfectNumber(self, num):
        import math
        def is_prime(n):
            if n % 2 == 0 and n > 2: 
                return False
            return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

        total = 1
        if num < 0 or num % 2 == 1 or is_prime(num):
            return False
        i = 1
        num_copy = num
        while num % 2 == 0:
            num = num // 2
            # print(num, 2**i)
            total += num + 2**i
            i += 1
        # print('out', num, 2**i)
        # total += num + 2**(i-1)
        # print(total)
        if total == num_copy:
            return True
        return False

# s = Solution()
# num = 6
# print(s.checkPerfectNumber(num) == True)

# num = 28
# print(s.checkPerfectNumber(num) == True)

# num = 496
# print(s.checkPerfectNumber(num) == True)


# num = 8128
# print(s.checkPerfectNumber(num) == True)


# num = 1
# print(s.checkPerfectNumber(num) == False)
# num = 36
# print(s.checkPerfectNumber(num) == False)


# for i in range(20000, 40000):
#     if s.checkPerfectNumber(i):
#         print(i)

# import time

# start = time.time()
# num = 24036583
# print(s.checkPerfectNumber(num) == False)

# num = 99999991
# print(s.checkPerfectNumber(num))
# end = time.time()
# print(end - start)
