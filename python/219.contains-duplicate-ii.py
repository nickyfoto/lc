#
# @lc app=leetcode id=219 lang=python3
#
# [219] Contains Duplicate II
#
# https://leetcode.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (35.40%)
# Total Accepted:    204.6K
# Total Submissions: 575.8K
# Testcase Example:  '[1,2,3,1]\n3'
#
# Given an array of integers and an integer k, find out whether there are two
# distinct indices i and j in the array such that nums[i] = nums[j] and the
# absolute difference between i and j is at most k.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1], k = 3
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,0,1,1], k = 1
# Output: true
# 
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false
# 
# 
# 
# 
# 
#
class Solution:
    # def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    def containsNearbyDuplicate(self, nums, k):
        # distance of equal element at most k
        if not nums:
            return False
        d = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in d:
                d[nums[i]] = [i]
            else:
                d[nums[i]].append(i)
        # print(d)
        distances = [v for k, v in d.items() if len(v) > 1]
        # print(distances)
        def minDistance(l):
            if len(l) == 2:
                return l[1] - l[0]
            else:
                d = float('inf')
                for i in range(1, len(l)):
                    dist = l[i] - l[i-1]
                    if dist < d:
                        d = dist
                return d
        if not distances:
            return False
        if min(map(minDistance, distances)) > k:
            return False
        return True
# s = Solution()
# nums = [1,2,3,1]
# k = 3
# print(s.containsNearbyDuplicate(nums, k))

# nums = [1,0,1,1]
# k = 1
# print(s.containsNearbyDuplicate(nums, k))

# nums = [1,2,3,1,2,3]
# k = 2
# print(s.containsNearbyDuplicate(nums, k))
# nums = [1,2]
# k = 2
# print(s.containsNearbyDuplicate(nums, k))
