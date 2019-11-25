#
# @lc app=leetcode id=594 lang=python3
#
# [594] Longest Harmonious Subsequence
#
# https://leetcode.com/problems/longest-harmonious-subsequence/description/
#
# algorithms
# Easy (43.92%)
# Total Accepted:    38.2K
# Total Submissions: 86.6K
# Testcase Example:  '[1,3,2,2,5,2,3,7]'
#
# We define a harmounious array as an array where the difference between its
# maximum value and its minimum value is exactly 1.
# 
# Now, given an integer array, you need to find the length of its longest
# harmonious subsequence among all its possible subsequences.
# 
# Example 1:
# 
# 
# Input: [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].
# 
# 
# 
# 
# Note: The length of the input array will not exceed 20,000.
# 
#
from collections import Counter
class Solution:
    # def findLHS(self, nums: List[int]) -> int:
    def findLHS(self, nums):
        d = Counter(nums)
        res = 0
        for k, v in d.most_common():
            # print(k, v)
            if k - 1 in d:
                total = v + d[k-1]
                if total > res:
                    res = total
            if k + 1 in d:
                total = v + d[k+1]
                if total > res:
                    res = total
        return res
# s = Solution()
# nums = [1,3,2,2,5,2,3,7]
# print(s.findLHS(nums))