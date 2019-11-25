#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (56.30%)
# Total Accepted:    238.3K
# Total Submissions: 422.9K
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given a non-empty array of integers, return the k most frequent elements.
# 
# Example 1:
# 
# 
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# 
# 
# 
# Example 2:
# 
# 
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Note: 
# 
# 
# You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
# Your algorithm's time complexity must be better than O(n log n), where n is
# the array's size.
# 
# 
#

from collections import Counter

class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    def topKFrequent(self, nums, k):
        c = Counter(nums)
        res = [x[0] for x in sorted([(k,v) for k,v in c.items()], key=lambda x:x[1], reverse=True)[:k]]
        # print(res)
        return res

# s = Solution()
# nums = [1,1,1,2,2,3]
# k = 2
# print(s.topKFrequent(nums, k))
# nums = [1]
# k = 1
# print(s.topKFrequent(nums, k))


