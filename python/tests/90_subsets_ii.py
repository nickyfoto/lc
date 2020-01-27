#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (44.96%)
# Likes:    1291
# Dislikes: 56
# Total Accepted:    244.8K
# Total Submissions: 544.4K
# Testcase Example:  '[1,2,2]'
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: [1,2,2]
# Output:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 
# 
#

# @lc code=start
class Solution:
    # def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    def subsetsWithDup(self, nums):
        def backtrack(lst, temp, nums, start):
            lst.append(temp.copy())
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                temp.append(nums[i])
                backtrack(lst, temp, nums, i + 1)
                temp.pop()
        lst = []
        nums.sort()
        backtrack(lst, [], nums, 0)
        return lst
# @lc code=end
