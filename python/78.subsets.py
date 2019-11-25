#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (54.72%)
# Total Accepted:    407.6K
# Total Submissions: 744.5K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#
class Solution:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    def subsets(self, nums):
        
        def recur(l):
            n = len(l)
            if n == 1:
                return [[], l]
            else:
                # print(l[:n-1])
                prev = recur(l[:n-1])
                temp = []
                for s in prev:
                    temp.append(s + [l[-1]])
                return prev + temp

        return recur(nums)
        
# s = Solution()
# nums = [1,2,3]
# print(s.subsets(nums))










