#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#
# https://leetcode.com/problems/combination-sum/description/
#
# algorithms
# Medium (52.78%)
# Likes:    2887
# Dislikes: 90
# Total Accepted:    450.8K
# Total Submissions: 853.9K
# Testcase Example:  '[2,3,6,7]\n7'
#
# Given a set of candidate numbers (candidates) (without duplicates) and a
# target number (target), find all unique combinations in candidates where the
# candidate numbers sums to target.
# 
# The same repeated number may be chosen from candidates unlimited number of
# times.
# 
# Note:
# 
# 
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# 
# 
# Example 1:
# 
# 
# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
# ⁠ [7],
# ⁠ [2,2,3]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
# [2,2,2,2],
# [2,3,3],
# [3,5]
# ]
# 
# 
#

# @lc code=start
class Solution:
    # def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    def combinationSum(self, candidates, target):
        n = len(candidates)
        candidates.sort(reverse=True)
        # print(candidates)
        res = []
        def backtrack(temp, less, start):
            if less == 0:
                res.append(temp.copy())
            else:
                for i in range(start, n):
                    if candidates[i] > less:
                        continue
                    temp.append(candidates[i])
                    less -= candidates[i]
                    if candidates[i] <= less:
                        backtrack(temp, less, i)
                    else:
                        backtrack(temp, less, i + 1)
                    less += candidates[i]
                    temp.pop()
        backtrack([], target, 0)
        return res
# @lc code=end
