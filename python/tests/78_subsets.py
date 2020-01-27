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
        
        def backtrack(lst, nums, temp, start):
            # print("start=", start)
            lst.append(temp.copy())
            for i in range(start, len(nums)):
                temp.append(nums[i])
                backtrack(lst, nums, temp, i + 1)
                temp.pop()
        lst = []
        nums.sort()
        backtrack(lst, nums, [], 0)
        return lst
        

# s = Solution()
# nums = [1,2,3]
# print(s.subsets(nums))










