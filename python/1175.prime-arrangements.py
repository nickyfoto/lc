#
# @lc app=leetcode id=1175 lang=python3
#
# [1175] Prime Arrangements
#
# https://leetcode.com/problems/prime-arrangements/description/
#
# algorithms
# Easy (50.74%)
# Total Accepted:    3.3K
# Total Submissions: 6.5K
# Testcase Example:  '5'
#
# Return the number of permutations of 1 to n so that prime numbers are at
# prime indices (1-indexed.)
# 
# (Recall that an integer is prime if and only if it is greater than 1, and
# cannot be written as a product of two positive integers both smaller than
# it.)
# 
# Since the answer may be large, return the answer modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: n = 5
# Output: 12
# Explanation: For example [1,2,5,4,3] is a valid permutation, but [5,2,3,4,1]
# is not because the prime number 5 is at index 1.
# 
# 
# Example 2:
# 
# 
# Input: n = 100
# Output: 682289015
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 100
# 
# 
#



class Solution:
    def countPrimes(self, n):
        count = 0
        import math
        if n < 3:
            return 0
        if n == 3:
            return 1
        else:
            count = 0
            def gen_primes():
                D = {}
                q = 2
                while True:
                    if q not in D:
                        yield q
                        D[q * q] = [q]
                    else:
                        for p in D[q]:
                            D.setdefault(p + q, []).append(p)
                        del D[q]
                    q += 1
            for i in gen_primes():
                if i < n:
                    count += 1
                else:
                    break
        return count
    def numPrimeArrangements(self, n: int) -> int:
        # print(self.countPrimes(n))

        def factorial(start, end):
            res = start
            for i in range(start+1, end+1):
                res *= i
            return res

        # print(factorial(5,6))
        # print(factorial(2,1))
        n_prime = self.countPrimes(n+1)
        # print(n_prime)
        p = factorial(1, n_prime)
        # print(n_prime, p)
        if n_prime >= n - n_prime:
            return (p * factorial(1, n-n_prime)) % (10**9 + 7) 
        else:
            # print(p, n_prime+1, n-n_prime, factorial(n_prime+1, n-n_prime))
            # print(p * factorial(n_prime+1, n-n_prime) == factorial(1, n-n_prime))
            return (p * p * factorial(n_prime+1, n-n_prime)) % (10**9 + 7) 
            # return (p * factorial(1, n-n_prime)) % (10**9 + 7) 
        # print(factorial(2,3))

    # def numPrimeArrangements(self, n: int) -> int:
    #     cnt = 1                                                     # number of primes, first prime is 2.
    #     for i in range(3, n + 1, 2):                                # only odd number could be a prime, if i > 2.
    #         factor = 3
    #         while factor * factor <= i:
    #             if i % factor == 0:
    #                 break 
    #             factor += 2    
    #         else:
    #             cnt += 1      
    #     print(cnt)  
    #     ans = 1
    #     for i in range(1, cnt + 1):                                # (number of primes)!
    #         ans *= i        
    #     for i in range(1, n - cnt + 1):                            # (number of non-primes)!
    #         ans *= i
    #     return ans % (10**9 + 7)
# s = Solution()
# print(s.numPrimeArrangements(5))
# print(s.numPrimeArrangements(2))
# # print(s.numPrimeArrangements(10))
# print(s.numPrimeArrangements(100)) # 682289015













