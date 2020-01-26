#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (56.71%)
# Total Accepted:    417K
# Total Submissions: 735.1K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# 
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#
class Solution:
    # def permute(self, nums: List[int]) -> List[List[int]]:
    def permute2(self, nums):
        from itertools import permutations
        r = []
        for p in permutations(nums):
            r.append(list(p))
        print(len(r))
        # print(r)
    def permute3(self, nums):
        def product(*args, repeat=1):
            # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
            # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
            pools = [tuple(pool) for pool in args] * repeat
            # print('here', pools)
            result = [[]]
            for pool in pools:
                result = [x+[y] for x in result for y in pool]
                # print('result', result)
            for prod in result:
                yield tuple(prod)
        # print(list(product(nums, repeat=len(nums))))
        # print([(x,y) for x in nums for y in nums])
        def permutations(iterable, r=None):
            pool = tuple(iterable)
            n = len(pool)
            r = n if r is None else r
            for indices in product(range(n), repeat=r):
                if len(set(indices)) == r:
                    yield [pool[i] for i in indices]
        res = list(permutations(nums))
        return res

    def permute(self, nums):
        def permutations(iterable, r=None):
            # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
            # permutations(range(3)) --> 012 021 102 120 201 210
            pool = tuple(iterable)
            n = len(pool)
            r = n if r is None else r
            if r > n:
                return
            indices = list(range(n))
            cycles = list(range(n, n-r, -1))
            yield tuple(pool[i] for i in indices[:r])
            while n:
                # print('cycles=', cycles)
                for i in reversed(range(r)):
                    # print('i=', i)
                    cycles[i] -= 1
                    if cycles[i] == 0:
                        indices[i:] = indices[i+1:] + indices[i:i+1]
                        cycles[i] = n - i
                    else:
                        j = cycles[i]
                        indices[i], indices[-j] = indices[-j], indices[i]
                        yield tuple(pool[i] for i in indices[:r])
                        break
                # https://stackoverflow.com/questions/9979970/why-does-python-use-else-after-for-and-while-loops
                else:
                    return
        # print(list(permutations(nums, r=2)))
        return list(permutations(nums))
        

s = Solution()
nums = [1, 2, 3, 4]
# print(s.permute(nums))


def printArr(a, n): 
    for i in range(n): 
        print(a[i],end=" ") 
    print() 
  
# Generating permutation using Heap Algorithm 
def heapPermutation(a, size, n): 
    # print('here', a, size)
    # if size becomes 1 then prints the obtained 
    # permutation 
    if (size == 1): 
        # print('return')
        printArr(a, n) 
        return
  
    for i in range(size):
        # print('for', a, 'i/size', i, '/', size)
        # print('before heap a=', a, 'size=,', size,'i=', i)
        print()
        heapPermutation(a,size-1,n); 
  
        # print('here, a=', a, 'size=', size, 'i=', i)
        # if size is odd, swap first and last 
        # element 
        # else If size is even, swap ith and last element 
        if size % 2 == 1: 
            # print('size is odd, swap 0 with size-1', size-1)
            a[0], a[size-1] = a[size-1],a[0] 
        else: 
            # print('aa')
            # print('size is even, swap i=', i, 'with size-1=', size-1)
            a[i], a[size-1] = a[size-1],a[i] 
  
# Driver code 
a = [1, 2, 3, 4] 
n = len(a) 
# heapPermutation(a, n, n) 

# This code is contributed by ankush_953 

# from timefunc import timeit
# @timeit
def perm(nums):
    if len(nums) == 1:
        return [nums]
    else:
        l = []
        for i in range(len(nums)):
            # l.append()
            arr = nums[:i] + nums[i+1:]
            for ele in perm(arr):
                l.append(ele + [nums[i]])
        return l
def perm2(nums):
    def recur(nums, size):
        print('size=', size)
        if size == 1: 
        # print('return')
            print(nums) 
            return
  
        for i in range(size):
            recur(nums,size-1)
    recur(nums, len(nums))
print(perm2([1,2,3]))


from time import time
start = time()
# print()
# a = perm(list(range(9)))
# ma = map(tuple, a)
# print(set(ma) == set(s.permute(range(9))))
# s.permute(list(range(9)))
end = time()
print(end - start)






















