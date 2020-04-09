#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#
# https://leetcode.com/problems/next-greater-element-ii/description/
#
# algorithms
# Medium (52.11%)
# Total Accepted:    59.2K
# Total Submissions: 113.6K
# Testcase Example:  '[1,2,1]'
#
# 
# Given a circular array (the next element of the last element is the first
# element of the array), print the Next Greater Number for every element. The
# Next Greater Number of a number x is the first greater number to its
# traversing-order next in the array, which means you could search circularly
# to find its next greater number. If it doesn't exist, output -1 for this
# number.
# 
# 
# Example 1:
# 
# Input: [1,2,1]
# Output: [2,-1,2]
# Explanation: The first 1's next greater number is 2; The number 2 can't find
# next greater number; The second 1's next greater number needs to search
# circularly, which is also 2.
# 
# 
# 
# Note:
# The length of given array won't exceed 10000.
# 
#

from collections import defaultdict

class Solution:
    # def nextGreaterElements(self, nums: List[int]) -> List[int]:
    def nextGreaterElements2(self, nums):
        n = len(nums)
        ans = [-1] * n
        for i in range(n):
            # arr = nums[i+1:] + nums[:i+1]
            for j in range(i+1,n+i):
                if nums[j%n] > nums[i]:
                    ans[i] = nums[j%n]
                    break
        return ans

    def nextGreaterElements1(self, nums):
        if not nums:
            return []
        n = len(nums)
        idx_stack = []
        ans = [-1] * n
        # d = defaultdict(lambda: False)
        i = 0
        idx_stack.append(i)
        while idx_stack:
            i += 1
            # print('i=', i % n, 'nums[i]=', nums[i%n], 'idx_stack=', idx_stack)
            # print('idx_stack[-1]=', idx_stack[-1], 'nums[idx_stack[-1]]=', nums[idx_stack[-1]])
            if i >= n:
                i = i%n
            while idx_stack and nums[i] > nums[idx_stack[-1]]:
                idx = idx_stack.pop()
                ans[idx] = nums[i]
                # d[idx] = True
                # print('poping')

            if idx_stack:
                if i%n == idx_stack[0]:
                    # d[idx_stack.pop(0)] = True
                    idx_stack.pop(0)
                    # print('here', idx_stack)
                else:
                    if i > idx_stack[-1]:
                        idx_stack.append(i)
            else:
                idx_stack.append(i)
                    
            # if not d[i%n]:
            # print('here again', idx_stack)
            # print('ans=', ans)
            # print('='*30)
            
        return ans

    def nextGreaterElements(self, nums):
        n = len(nums)
        res = [-1] * n
        stack = []
        for i in range(2 * n):
            v = nums[i % n]
            while stack and v > nums[stack[-1]]:
                res[stack.pop()] = v 
            if i < n:
                stack.append(i)
        return res
# import time

# start = time.time()

# s = Solution()
# # nums = []
# nums = [1,2,1]
# print(s.nextGreaterElements(nums) == [2, -1, 2])

# nums = [10,9,8,7,6,5,4,3,2,1]
# print(s.nextGreaterElements(nums))


# nums = [2,1,10,9,8,7,3,4,5,6]
# print(s.nextGreaterElements(nums))


# # nums = [1,1,1,1,1]



# end = time.time()
# print(end - start)          







