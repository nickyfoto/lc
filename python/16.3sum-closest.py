#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (45.76%)
# Total Accepted:    377.4K
# Total Submissions: 824.8K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
# 
# Example:
# 
# 
# Given array nums = [-1, 2, 1, -4], and target = 1.
# 
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 
#
class Solution:
    # def threeSumClosest(self, nums: List[int], target: int) -> int:
    def threeSumClosest2(self, nums, target):
        mn = float('inf')
        res = None
        n = len(nums)
        for i in range(n-2):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    total = nums[i]+nums[j]+nums[k]
                    if abs(total - target) < mn:
                        mn = abs(total - target)
                        res = total
        return res


    def threeSumClosest(self, nums, target):
        nums.sort()
        mn = float('inf')
        res = None
        n = len(nums)
        if n == 3:
            return sum(nums)
        for i in range(n-2):
            start = i+1
            end = n-1
            while start != end:
                s = nums[i] + nums[start] + nums[end]
                if s > target:
                    v = nums[end]
                    # print(start, end)
                    while nums[end] == v:
                        if end == start:
                            break
                        end -= 1
                elif s < target:
                    v = nums[start]
                    while nums[start] == v:
                        if start == end:
                            break
                        # print('here', start, end)
                        start += 1
                else:
                    return s
                # print('i=', i, start, end)
                if abs(s - target) < mn:
                    mn = abs(s - target)
                    res = s
                # print('i=', i, s, mn, res)
        return res




# s = Solution()
# # nums = [-1, 2, 1, -4]
# # target = 1
# # print(s.threeSumClosest(nums, target))
# nums = [0,0,0]
# target = 1
# print(s.threeSumClosest(nums, target))
# nums = [1,1,1,1]
# target = 0
# print(s.threeSumClosest(nums, target))
# nums = [1,1,1,0]
# target = -100
# print(s.threeSumClosest(nums, target)) #exp 2
# nums = [1,2,5,10,11]
# target = 12
# print(s.threeSumClosest(nums, target)) #exp 13

