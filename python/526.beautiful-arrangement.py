#
# @lc app=leetcode id=526 lang=python3
#
# [526] Beautiful Arrangement
#
# https://leetcode.com/problems/beautiful-arrangement/description/
#
# algorithms
# Medium (55.82%)
# Total Accepted:    41.7K
# Total Submissions: 74.7K
# Testcase Example:  '2'
#
# Suppose you have N integers from 1 to N. We define a beautiful arrangement as
# an array that is constructed by these N numbers successfully if one of the
# following is true for the ith position (1 <= i <= N) in this array:
# 
# 
# The number at the ith position is divisible by i.
# i is divisible by the number at the ith position.
# 
# 
# 
# 
# Now given N, how many beautiful arrangements can you construct?
# 
# Example 1:
# 
# 
# Input: 2
# Output: 2
# Explanation: 
# 
# The first beautiful arrangement is [1, 2]:
# 
# Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
# 
# Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
# 
# The second beautiful arrangement is [2, 1]:
# 
# Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
# 
# Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
# 
# 
# 
# 
# Note:
# 
# 
# N is a positive integer and will not exceed 15.
# 
# 
# 
# 
from itertools import permutations 
class Solution:
    def countArrangement(self, N: int) -> int:
        
        def f(a):
            # print(a)
            for i in range(1, len(a)+1):
                if not (a[i-1] % i == 0 or i % a[i-1] == 0):
                    return False
            return True
        res = list(filter(f, permutations(range(1,N+1))))
        print(len(res))

        ct = 0
        # ct = []



        stack = []
        nums = {k:True for k in range(1, N+1)}
        
        stack = [([], nums)]
        # print(stack)
        while stack:
            pos, a_nums = stack.pop()
            p = len(pos) + 1
            for n in a_nums:
                if n % p == 0 or p % n == 0:
                    num_cp = a_nums.copy()
                    del num_cp[n]
                    pos_cp = pos.copy()
                    pos_cp.append(n)
                    if len(pos_cp) == N:
                        # self.ct.append(pos_cp)
                        ct += 1
                    else:
                        stack.append((pos_cp, num_cp))
                        # break
        
        # print(len(self.ct))
        return ct




        
        # print('res', self.ct)
        # i is divisible by the number at the ith position


s = Solution()
N = 2
print(s.countArrangement(N))

N = 4
print(s.countArrangement(N))



import time

start = time.time()

# print(list(permutations(range(1,5))))
end = time.time()
# print(end - start)













