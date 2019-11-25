#
# @lc app=leetcode id=932 lang=python3
#
# [932] Beautiful Array
#
# https://leetcode.com/problems/beautiful-array/description/
#
# algorithms
# Medium (53.94%)
# Total Accepted:    6.7K
# Total Submissions: 12.5K
# Testcase Example:  '4'
#
# For some fixed N, an array A is beautiful if it is a permutation of the
# integers 1, 2, ..., N, such that:
# 
# For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] +
# A[j].
# 
# Given N, return any beautiful array A.  (It is guaranteed that one
# exists.)
# 
# 
# 
# Example 1:
# 
# 
# Input: 4
# Output: [2,1,4,3]
# 
# 
# 
# Example 2:
# 
# 
# Input: 5
# Output: [3,1,2,5,4]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 1000
# 
# 
# 
# 
# 
#
class Solution:
    # def beautifulArray(self, N: int) -> List[int]:
    def beautifulArray(self, N):
        if N < 3:
            return list(range(1,N+1))
        a = {k:None for k in range(1, N+1)}
        stack = [([], a)]
        # print(a)


        def can_be_added(arr, a, av):
            print('here', arr, a, av)
            for i in range(len(arr)):
                if 2 * a - arr[i] in av:
                    print('False')
                    return False
                for j in range(i+1, len(arr)):
                    if arr[j] * 2 == a + arr[i]:
                        return False
            # print('True')
            return True



        while stack:
            # print(stack)
            arr, av = stack.pop()
            if not arr:
                for a in av:
                    arr_cp = arr.copy()
                    arr_cp.append(a)
                    av_cp = av.copy()
                    del av_cp[a]
                    stack.append((arr_cp, av_cp))

            else:
                # print(arr, av)
                for a in av:
                    if can_be_added(arr, a, av):
                        arr_cp = arr.copy()
                        arr_cp.append(a)
                        print('here', arr_cp)
                        if len(arr_cp) == N:
                            # print(stack)
                            return arr_cp
                        else:
                            av_cp = av.copy()
                            del av_cp[a]
                            stack.append((arr_cp, av_cp))
                            


        # return res
s = Solution()

# print(s.beautifulArray(1))
# print(s.beautifulArray(2))
# print(s.beautifulArray(3))
print(s.beautifulArray(4))
print(s.beautifulArray(10))
# print(s.beautifulArray(2))
# print(s.beautifulArray(8))
# print(s.beautifulArray(10))



























        
