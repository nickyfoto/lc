#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#
# https://leetcode.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (37.69%)
# Total Accepted:    118.5K
# Total Submissions: 314.2K
# Testcase Example:  '10'
#
# Write a program to find the n-th ugly number.
# 
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
# 
# Example:
# 
# 
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
# ugly numbers.
# 
# Note:  
# 
# 
# 1 is typically treated as an ugly number.
# n does not exceed 1690.
# 
#
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        
        def nthSuperUglyNumber(n, primes):
            lp = len(primes)
            indices = [0]*lp
            l = [1]*n
            pq = list(zip(primes, range(lp)))
            heapq.heapify(pq)
            c, mx = 1, 1
            while c < n:
                val, i = heapq.heappop(pq)
                indices[i] += 1
                if val > mx:
                    l[c] = val
                    mx = val
                    c += 1
                if i == 0:
                    val *= primes[i]
                else:
                    val = primes[i] * l[indices[i]]
                heapq.heappush(pq, (val, i))
            return l[-1]

        return nthSuperUglyNumber(n, primes=[2,3,5])

        