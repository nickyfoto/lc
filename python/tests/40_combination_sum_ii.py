#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#
# https://leetcode.com/problems/combination-sum-ii/description/
#
# algorithms
# Medium (45.18%)
# Likes:    1286
# Dislikes: 54
# Total Accepted:    279.3K
# Total Submissions: 618.3K
# Testcase Example:  '[10,1,2,7,6,1,5]\n8'
#
# Given a collection of candidate numbers (candidates) and a target number
# (target), find all unique combinations in candidates where the candidate
# numbers sums to target.
# 
# Each number in candidates may only be used once in the combination.
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
# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
# ⁠ [1, 7],
# ⁠ [1, 2, 5],
# ⁠ [2, 6],
# ⁠ [1, 1, 6]
# ]
# 
# 
# Example 2:
# 
# 
# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
# [1,2,2],
# [5]
# ]
# 
# 
#

# @lc code=start
class Solution:
    # def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    def _combinationSum2(self, candidates, target):
        n = len(candidates)
        candidates.sort(reverse=True)
        # print(candidates)
        res = {}
        def backtrack(temp, less, start):
            if less == 0:
                if tuple(temp) not in res:
                    res[tuple(temp)] = True
            else:
                for i in range(start, n):
                    if candidates[i] > less:
                        continue
                    temp.append(candidates[i])
                    less -= candidates[i]
                    backtrack(temp, less, i + 1)
                    less += candidates[i]
                    temp.pop()
        backtrack([], target, 0)
        
        return map(list, res.keys())


    def combinationSum2(self, candidates, target):
        n = len(candidates)
        candidates.sort(reverse=True)
        # print(candidates)
        res = []
        def backtrack(temp, less, start):
            if less == 0:
                res.append(temp.copy())
            else:
                for i in range(start, n):
                    if candidates[i] > less or (i > start and candidates[i-1] == candidates[i]):
                        continue
                    temp.append(candidates[i])
                    less -= candidates[i]
                    backtrack(temp, less, i + 1)
                    less += candidates[i]
                    temp.pop()
        backtrack([], target, 0)
        
        return res
# @lc code=end
