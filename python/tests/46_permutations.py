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
    def permute(self, nums):
        """
        https://leetcode.com/problems/permutations/discuss/18241/One-Liners-in-Python
        """
        return reduce(lambda P, n: [p[:i] +  [n] + p[i:]
                                   for p in P
                                       for i in range(len(p) + 1)],
                      nums, [[]])
# @lc code=end
