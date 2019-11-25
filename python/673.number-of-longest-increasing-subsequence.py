#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#
# https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/
#
# algorithms
# Medium (33.35%)
# Total Accepted:    29.1K
# Total Submissions: 87.1K
# Testcase Example:  '[1,3,5,4,7]'
#
# 
# Given an unsorted array of integers, find the number of longest increasing
# subsequence.
# 
# 
# Example 1:
# 
# Input: [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1,
# 3, 5, 7].
# 
# 
# 
# Example 2:
# 
# Input: [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence is 1,
# and there are 5 subsequences' length is 1, so output 5.
# 
# 
# 
# Note:
# Length of the given array will be not exceed 2000 and the answer is
# guaranteed to be fit in 32-bit signed int.
# 
#
class Solution:
    # def findNumberOfLIS(self, nums: List[int]) -> int:
    def LIS(self, a):
        """Longest Increasing Subsequences"""
        L = [1] * len(a)
        for i in range(len(a)):
            for j in range(i):
                if a[j] < a[i]:
                    if L[i] < 1+L[j]:
                        L[i] = 1 + L[j]
        print(L)
        return max(L)

    def findNumberOfLIS(self, nums):
        
        if not nums:
            return 0
        N = len(nums)
        if N <= 1: return N
        lengths = [1] * N #lengths[i] = longest ending in nums[i]
        counts = [1] * N #count[i] = number of longest ending in nums[i]
        # # self.LIS(nums)
        for j, num in enumerate(nums):
            print("current index", j, "current value", num)
            for i in range(j):
                print("previous index", i, "previous value", nums[i])
                if nums[i] < nums[j]:
                    print(nums[i], "<", nums[j])
                    if lengths[i] >= lengths[j]:
                        print("lengths", lengths)
                        print("lengths[i]", lengths[i], ">=", "lengths[j]", lengths[j])
                        lengths[j] = 1 + lengths[i]
                        print("updated lengths", lengths)
                        # count does not increase based on prev counts because 
                        # current element is > prev, although lengths[current] increases
                        # number of LIS remains the same
                        counts[j] = counts[i] 
                        print("updated counts", counts)
                    elif lengths[i] + 1 == lengths[j]:
                        print("lengths[i] + 1", lengths[i]+1, "==", "lengths[j]", lengths[j])
                        # here we update current counts = counts[current] + counts[prev]
                        # because before meeting this prev element, current already have counts[current]
                        # as number of LIS, but not including this prev element
                        # since current element is right after this prev element
                        # (because lengths[i] + 1 == lengths[j])
                        # therefore counts[current] should be updated to
                        # counts[current(without prev)] + counts[prev]
                        counts[j] += counts[i]
                        print("updated counts", counts)
            print("finish updating", j)
        #         # print(lengths)
        print(counts)
        print(lengths)
        print(self.LIS(nums))
        longest = max(lengths)
        print(longest)
        return sum(c for i, c in enumerate(counts) if lengths[i] == longest)


# default lengths (LIS) = 0
# default counts = 1
# iterate throught nums
# if previous num is less than current num
# if is possible we update lengths and counts
# update lengths and count when
#   if lengths[previous] >= lengths[current]
#       lengths[current] = length[previous] + 1
#       counts[current] = counts[previous]
#   elif lengths[previous] + 1 == lengths[current]
#       counts[current] += counts[previous]



s = Solution()

a1 = [1,3,5,4,7] # 2 because 
print(s.findNumberOfLIS(a1))
# a2 = [2,2,2,2,2] # 5
# print(s.findNumberOfLIS(a2))
# a3 = [1,2,4,3,5,4,7,2] #3
# print(s.findNumberOfLIS(a3))
# a4 = [3,1,2] #1
# print(s.findNumberOfLIS(a4))

# a5 = [1,1,1,2,2,2,3,3,3] #27
# print(s.findNumberOfLIS(a5))

# a6 = [100,90,80,70,60,50,60,70,80,90,100] # 1
# print(s.findNumberOfLIS(a6))
# a7 = [1,3,2] # 2
# print(s.findNumberOfLIS(a7))

# a8 = [1,2,1,3,0,0,2,2,1,3,3]
# print(s.findNumberOfLIS(a8))
        








