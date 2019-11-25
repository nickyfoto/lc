#
# @lc app=leetcode id=978 lang=python3
#
# [978] Longest Turbulent Subarray
#
# https://leetcode.com/problems/longest-turbulent-subarray/description/
#
# algorithms
# Medium (45.63%)
# Total Accepted:    13.8K
# Total Submissions: 30.1K
# Testcase Example:  '[9,4,2,10,7,8,8,1,9]'
#
# A subarray A[i], A[i+1], ..., A[j] of A is said to be turbulent if and only
# if:
# 
# 
# For i <= k < j, A[k] > A[k+1] when k is odd, and A[k] < A[k+1] when k is
# even;
# OR, for i <= k < j, A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is
# odd.
# 
# 
# That is, the subarray is turbulent if the comparison sign flips between each
# adjacent pair of elements in the subarray.
# 
# Return the length of a maximum size turbulent subarray of A.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: (A[1] > A[2] < A[3] > A[4] < A[5])
# 
# 
# 
# Example 2:
# 
# 
# Input: [4,8,12,16]
# Output: 2
# 
# 
# 
# Example 3:
# 
# 
# Input: [100]
# Output: 1
# 
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 40000
# 0 <= A[i] <= 10^9
# 
#
class Solution:
    # def maxTurbulenceSize(self, A: List[int]) -> int:
    
    def maxTurbulenceSize2(self, A):
        n = len(A)
        l = []

        def check(i, start_with):
            res = 1
            nextBig = start_with
            while True:
                if i+1 == n:
                    break
                if nextBig:
                    if A[i+1] > A[i]:
                        res += 1
                        i += 1
                        nextBig = not nextBig
                    else:
                        break
                else:
                    if A[i+1] < A[i]:
                        res += 1
                        i += 1
                        nextBig = not nextBig
                    else:
                        break
            return res
        # def smallBig(i):
        #     if i % 2 == 0:
        #         return check(i, start_with = True)
        #     else:
        #         return check(i, start_with = False)
        # def Bigsmall(i):
        #     if i % 2 == 0:
        #         return check(i, start_with = False)
        #     else:
        #         return check(i, start_with = True)
        # smallBig(0) # 1
        # bigSmall(0) # 2
        for i in range(n):
            # sb, bs = smallBig(i), Bigsmall(i)
            sb, bs = check(i, start_with = False), check(i, start_with = True)
            print('i=', sb, bs)
            l.append(max(sb, bs))

        return max(l)

    def maxTurbulenceSize(self, A):
        n = len(A)
        l = []

        def check(i, start_with):
            res = 1
            nextBig = start_with
            while True:
                if i+1 == n:
                    break
                if nextBig:
                    if A[i+1] > A[i]:
                        res += 1
                        i += 1
                        nextBig = not nextBig
                    else:
                        break
                else:
                    if A[i+1] < A[i]:
                        res += 1
                        i += 1
                        nextBig = not nextBig
                    else:
                        break
            return res
        for i in range(n):
            # sb, bs = smallBig(i), Bigsmall(i)
            if i == 0:
                sb, bs = check(i, start_with = False), check(i, start_with = True)
                # print('i=', sb, bs)
                l.append((sb, bs))
            else:
                prev_sb, prev_bs = l[i-1]
                sb, bs = prev_bs - 1, prev_sb - 1
                if sb <= 1:
                    sb = check(i, start_with = False)
                if bs <= 1:
                    bs = check(i, start_with = True)
                l.append((sb, bs))
        # print(l)
        return max([max(i) for i in l])

# s = Solution()
# A = [9,4,2,10,7,8,8,1,9]
# print(s.maxTurbulenceSize(A))


# A = [4,8,12,16]
# print(s.maxTurbulenceSize(A))


# A = [100]
# print(s.maxTurbulenceSize(A))

# A = [2,0,2,4,2,5,0,1,2,3]
# print(s.maxTurbulenceSize(A)) #6
