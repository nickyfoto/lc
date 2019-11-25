#
# @lc app=leetcode id=525 lang=python3
#
# [525] Contiguous Array
#
# https://leetcode.com/problems/contiguous-array/description/
#
# algorithms
# Medium (42.47%)
# Total Accepted:    37.9K
# Total Submissions: 89.2K
# Testcase Example:  '[0,1]'
#
# Given a binary array, find the maximum length of a contiguous subarray with
# equal number of 0 and 1. 
# 
# 
# Example 1:
# 
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0
# and 1.
# 
# 
# 
# Example 2:
# 
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal
# number of 0 and 1.
# 
# 
# 
# Note:
# The length of the given binary array will not exceed 50,000.
# 
#
class Solution:
    # def findMaxLength(self, nums: List[int]) -> int:
    def findMaxLength(self, nums):
        n = len(nums)
        # print(n)
        # 1. maxLength, if no, -1
        # 2. start, if no, -1
        # 3. number of 0s - number of 1s
        L = [(0, -1, 0)]
        d = {0: 0}
        for i in range(n):
            prev = L[-1][2]
            if nums[i] == 0:
                diff = prev + 1
            else:
                diff = prev - 1
            # print("i=", i)
            # print("diff=", diff)
            item = (0, -1, diff)
            if i == 0:
                L.append(item)
                d[diff] = i+1
            else:
                # L[1] = item
                if diff not in d:
                    d[diff] = i+1
                    # L.append(item)
                else:
                    item = (i - d[diff] + 1, d[diff], diff)
                L.append(item)

        #     print("L", L)
        #     print(d)
        # print(d)
            # else:
                # d[diff].append(i)
            # else:
            #     for j in range(i):
            #         # print("i=", i, "j=", j, diff)
            #         if L[j][2] == diff:
            #             item = (i-j+1, j, diff)
            #             # print(nums[j:i+1])
            #             # print("break")
            #             # assert nums[j:i+1].count(0) == nums[j:i+1].count(1)
            #             break
                # L.append(item)
                # L[i+1] = item
            # print("L", L)
        # print(L)
        # for i in range(1, n+1):
        #     print(nums[i-1], L[i])
        # L.sort()
        # print(L[-1])
        return max(x[0] for x in L)
        # return L[-1][0]
                
        
# import time
# start = time.time()

# s = Solution()
# a1 = [0, 1] # 2
# print(s.findMaxLength(a1))
# a2 = [0, 1, 0] # 2
# print(s.findMaxLength(a2))

# a3 = [0,1,1] # 2
# print(s.findMaxLength(a3))

# a4 = [0,1,0,1] #4
# print(s.findMaxLength(a4))

# a5 = [1,1,1,1,1,1,1,1] # 0
# print(s.findMaxLength(a5))

# a7 = [0,1,0,1,1,1,0,0] # 8
# print(s.findMaxLength(a7))

# a8 = [1,0,1,0,1,1,1,0,0,1] # 8
# print(s.findMaxLength(a8))

# a6 = [0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1]
# print(s.findMaxLength(a6)) # 68

# a7 = [1,0,1,0,1,1,0,0,1,0,0,0,1,0,0,0,1,1,0,1,1,0,1,0,0,1,0,0,1,1,0,0,1,1,1,0,0,1,1,0,0,0,1,1,0,1,1,0,1,1,1,0,1,1,1,0,1,0,1,1,0,0,0,1,0,1,1,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,0,0,1,1,0,0,1,0,0,0,0,1,0,1,0,0,0,0]
# print(s.findMaxLength(a7)) # 86


# print(s.findMaxLength(a8)) 
# end = time.time()
# print(end - start)

