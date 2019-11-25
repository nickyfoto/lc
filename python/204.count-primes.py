#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (28.73%)
# Total Accepted:    235.3K
# Total Submissions: 813K
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
# 
# Example:
# 
# 
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# 
# 
#
class Solution:
    # def countPrimes(self, n: int) -> int:
    # def countPrimes(self, n):
    #     count = 0
    #     import math
    #     def is_prime(n):
    #         for i in range(3, int(math.sqrt(n)) + 1, 2):
    #             if n % i == 0:
    #                 return False
    #         return True
    #     if n < 3:
    #         return 0
    #     if n == 3:
    #         return 1
    #     else:
    #         count = 1
    #         for i in range(3, n, 2):
    #             if is_prime(i):
    #                 count += 1
    #     return count

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
                """ Generate an infinite sequence of prime numbers.
                """
                # Maps composites to primes witnessing their compositeness.
                # This is memory efficient, as the sieve is not "run forward"
                # indefinitely, but only as long as required by the current
                # number being tested.
                #
                D = {}
                
                # The running integer that's checked for primeness
                q = 2
                
                while True:
                    if q not in D:
                        # q is a new prime.
                        # Yield it and mark its first multiple that isn't
                        # already marked in previous iterations
                        # 
                        yield q
                        D[q * q] = [q]
                    else:
                        # q is composite. D[q] is the list of primes that
                        # divide it. Since we've reached q, we no longer
                        # need it in the map, but we'll mark the next 
                        # multiples of its witnesses to prepare for larger
                        # numbers
                        # 
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

    

# s = Solution()
# n = 10
# print(s.countPrimes(n))
# print(s.countPrimes(n) == s.countPrimes2(n))





# import time

# start = time.time()
# print(s.countPrimes(1500000))

# end = time.time()
# print(end - start)


