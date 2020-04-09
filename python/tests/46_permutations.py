#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
# https://leetcode.com/problems/permutations/description/
#
# algorithms
# Medium (59.68%)
# Likes:    2928
# Dislikes: 91
# Total Accepted:    498.5K
# Total Submissions: 835.4K
# Testcase Example:  '[1,2,3]'
#
# Given a collection of distinct integers, return all possible permutations.
# 
# Example:
# 
# 
# Input: [1,2,3]
# Output:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# 
#

# @lc code=start
from functools import reduce
class Solution:
    # def permute(self, nums: List[int]) -> List[List[int]]:
    # def permute(self, nums):
    #     """
    #     https://leetcode.com/problems/permutations/discuss/18241/One-Liners-in-Python
    #     """
    #     return reduce(lambda P, n: [p[:i] +  [n] + p[i:]
    #                                for p in P
    #                                    for i in range(len(p) + 1)],
    #                   nums, [[]])
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        n = len(nums)
        
        def backtrack(temp, used):
            if len(temp) == n:
                self.res.append(temp)
            else:
                for i in range(n):
                    if i not in used or not used[i]:
                        used[i] = True
                        backtrack(temp + [nums[i]], used)
                        used[i] = False
        
        backtrack([], {})
        
        return self.res

    def permute(self, nums):

        def backtrack(first):
            if first == n:
                res.append(nums[:])
            else:
                for i in range(first, n):
                    nums[first], nums[i] = nums[i], nums[first]
                    backtrack(first + 1)
                    nums[first], nums[i] = nums[i], nums[first]
        n = len(nums)
        res = []
        backtrack(0)
        return res
# @lc code=end
