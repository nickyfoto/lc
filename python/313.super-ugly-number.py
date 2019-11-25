#
# @lc app=leetcode id=313 lang=python3
#
# [313] Super Ugly Number
#
# https://leetcode.com/problems/super-ugly-number/description/
#
# algorithms
# Medium (42.59%)
# Total Accepted:    65.3K
# Total Submissions: 153.3K
# Testcase Example:  '12\n[2,7,13,19]'
#
# Write a program to find the nth super ugly number.
# 
# Super ugly numbers are positive numbers whose all prime factors are in the
# given prime list primes of size k.
# 
# Example:
# 
# 
# Input: n = 12, primes = [2,7,13,19]
# Output: 32 
# Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first
# 12 
# ⁠            super ugly numbers given primes = [2,7,13,19] of size 4.
# 
# Note:
# 
# 
# 1 is a super ugly number for any given primes.
# The given numbers in primes are in ascending order.
# 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
# The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
# 
# 
#



import bisect
from queue import PriorityQueue
from collections import defaultdict, Counter
import heapq
import math
from operator import mul
from functools import reduce
from itertools import count
from pprint import pprint
# from functools import lru_cache
class Solution:
    # def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
    def nthSuperUglyNumber2(self, n: int, primes) -> int:

        l = [1]
        d = defaultdict(lambda: False)
        d[1] = True
        def recur(n):
            if n == 1:
                return 1
            else:
                last = recur(n-1)
                for p in primes:
                    num = p*last
                    if num > l[-1]:
                        l.append(num)
                        d[num] = True
                    else:
                        if not d[num]:
                            bisect.insort_left(l, num)
                            d[num] = True
                    # break
                # print(l)
                return l[n-1]
        return recur(n)



    def nthSuperUglyNumber1(self, n: int, primes) -> int:

        pq = []
        d = defaultdict(lambda: False)
        heapq.heappush(pq, 1)
        d[1] = True
        for i in range(0, n):
            num = heapq.nsmallest(i+1, pq)[-1]
            for p in primes:
                r = p*num
                if not d[r]:
                    # print(pq)
                    heapq.heappush(pq, r)
                    d[r] = True
        # print(sorted(pq))
        return heapq.nsmallest(n, pq)[-1]



    def nthSuperUglyNumber(self, n: int, primes) -> int:
        pq = []
        d = defaultdict(lambda: False)
        pq = [1]
        d[1] = True
        for i in range(0, n):
            for p in primes:
                r = p*pq[i]
                if not d[r]:
                    if r > pq[-1]:
                        pq.append(r)
                    else:
                        bisect.insort_left(pq, r)
                    d[r] = True
        return pq[n-1]



        

        # for i in range(1,13):
            # print(next(hq2(i)))
        # print(next(hq2(12)))


        # return hq2(n)


    def nthSuperUglyNumber3(self, n: int, primes) -> int:
        base = primes[0]
        m = list(map(lambda x: math.log(x, base), primes))
        # print('m=', m)
        l = list(zip(m, range(len(primes))))
        template = []

        # pq = PriorityQueue()
        pq = []
        # heapq.heappush(pq, 1)


        for v,k in l:
            t = [0]*len(primes)
            t[k]=1
            template.append(t)
            heapq.heappush(pq, (v,t))            

        # print(template)



        def get_new_kv(l):
            # print('get_new_kv')
            i = -1
            me = values[i]
            k = ks[i]
            # print(values, me)
            # print(ks)
            temp = []
            while me + values[i-1]>me:
                temp.append((me + values[i-1],[a+b for a,b in zip(k, ks[i-1])]))
                i -= 1
            # print('temp=', temp)
            for v,k in temp:
                heapq.heappush(pq, (v,k))
            # print(sorted(pq))

        l = [1]
        c = 1
        values = [0]
        ks = []


        multiples_of_primes = []

        def add_to_multiples_of_primes(start):
            for i in range(len(m)):
                multiples_of_primes.append((start*m[i], [t*start for t in template[i]]))

        ct = count(2)
        # print(pq)
        while c < n:
            if pq:
                v, k = heapq.heappop(pq)
            else:
                # print('here', multiples_of_primes)
                v, k = multiples_of_primes.pop(0)


            temp_v = v

            if not multiples_of_primes:
                add_to_multiples_of_primes(next(ct))

            while multiples_of_primes[0][0] < temp_v:
                sv, sk = multiples_of_primes.pop(0)
                # print('here', sv, si)
                # print(len(multiples_of_primes))
                if not multiples_of_primes:
                    add_to_multiples_of_primes(next(ct))
                values.append(sv)
                ks.append(sk)
                item = reduce(mul, (p**i for p, i in zip(primes, sk) if i != 0))
                l.append(item)
                c += 1
                get_new_kv(l)
                temp_v = sv
            if c == n:
                # print('here')
                break
            # print('l=', l,c)
            values.append(v)
            ks.append(k)
            item = reduce(mul, (p**i for p, i in zip(primes, k) if i != 0))
            if item > l[-1]:
                l.append(item)
                c += 1
                get_new_kv(l)
        # print('l=', l)
        return l[-1]



    def nthSuperUglyNumber2(self, n: int, primes) -> int:


        debug = False
        # debug = True


        table = [[0]*len(primes) for _ in range(n)]
        
        table[0] = [1]*len(primes)

        def fill(r, c):    
            val = primes[c] * l[r-1]
            max_col[c] = val, r, c
            return val

        # pprint(table)
        c = 1
        
        max_col = list(zip(primes, [0]*len(primes), range(len(primes))))
        # print(max_col)
        l = [1]
        


        pq = PriorityQueue()

        for i, v in enumerate(primes):
            pq.put((v, i))



        # pq.put((0, primes[0]))



        mx = primes[0]
        cr, cl = 0, 0







        while c < n:
            # current row, current col

            
            
            mx, cl = pq.get()
            cr = max_col[cl][1]

            if debug:
                # print('max_col=', max_col)
                print('cr=', cr, 'cl=', cl, 'mx=', mx)
                # print('      pk=', pk, 'pv=', pv)


            if cl == 0:

                # if primes[cl] * table[cr][cl] <= mx:
                if primes[cl] * table[cr][cl] == mx:
                    if debug:
                        print('cr=', cr, 'cl=', cl)
                        print(primes[cl] * table[cr][cl], mx, primes[cl] * table[cr][cl] == mx)
                    cr += 1
                    table[cr][cl] = primes[cl] * table[cr-1][cl]
                    max_col[cl] = table[cr][cl], cr, cl

                    if table[cr][cl] > l[-1]:
                        if debug:
                            print(table[cr][cl], 'added to l')
                        l.append(table[cr][cl])
                        c += 1



            else:

                if cl < len(primes)-1:
                
                    # if primes[cl] * l[cr] <= mx:
                    if primes[cl] * l[cr] == mx:
                        if debug:
                            print('cr=', cr, 'cl=', cl)
                            print(primes[cl] * l[cr], mx, primes[cl] * l[cr] == mx)

                        cr += 1
                        table[cr][cl] = fill(cr,cl)
                        if table[cr][cl] > l[-1]:
                            if debug:
                                print(table[cr][cl], 'added to l')
                            l.append(table[cr][cl])
                            c += 1

                else:
                    if debug:
                        print('last column')

                    cr += 1
                    table[cr][cl] = fill(cr,cl)
                    if table[cr][cl] > l[-1]:
                        if debug: print(table[cr][cl], 'added to l')
                        l.append(table[cr][cl])
                        c += 1
                    

            # if debug: pprint(table)

            if cl == 0:
                mx = max_col[cl][0] * primes[0]
            else:
                mx = primes[cl] * l[max_col[cl][1]]
            # print('mx=', mx, max_col[cl])

            pq.put((mx, cl))
            
            

            if debug:
                print(l,c)
                print("="*30)


        return l[-1]

    def nthSuperUglyNumber_final(self, n: int, primes) -> int:
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

s = Solution()


import time

start = time.time()
# print("hello")

n = 12
primes = [2,7,13,19]
print(s.nthSuperUglyNumber(n, primes)==32)


n = 100000
# n = 300
primes = [7,19,29,37,41,47,53,59,61,79,83,89,101,103,109,127,131,137,139,157,167,179,181,199,211,229,233,239,241,251]
a = s.nthSuperUglyNumber(n, primes)
print(a)
# b = s.nthSuperUglyNumber2(n, primes)
# print(a == 1092889481)
# print(b)
# print(a==b)






# print()
n = 35
primes = [2,3,11,13,17,23,29,31,37,47]
# print(s.nthSuperUglyNumber(n, primes) == 62) # 62



n = 4
primes = [2,3,5]
print(s.nthSuperUglyNumber(n, primes) == 4)


n = 3
primes = [2]
print(s.nthSuperUglyNumber(n, primes) == 4)



end = time.time()
print(end - start)











        
