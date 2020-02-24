#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (49.57%)
# Likes:    2558
# Dislikes: 95
# Total Accepted:    250.1K
# Total Submissions: 503.9K
# Testcase Example:  '3'
#
# Given n, how many structurally unique BST's (binary search trees) that store
# values 1 ... n?
# 
# Example:
# 
# 
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
# 
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
# 
# 
#

# @lc code=start
from functools import lru_cache
class Solution:
    def numTrees(self, n: int) -> int:
        """
        Catalan number
        n = 3
        dp = [1,1,0,0]
        for i in range(2, 4):
            when i == 2
                j in range(1, 3)
                when j == 1
                dp[2] += dp[0] * dp[1]
                when j == 2
                dp[2] += dp[1] * dp[0]
            dp = [1,1,2,0]
            when i == 3
                j in range(1, 4)
                when j == 1
                dp[3] += dp[0] * dp[2]
                when j == 2
                dp[3] += dp[1] * dp[1]
                when j == 3
                dp[3] += dp[2] * dp[0]
            dp = [1,1,2,5]
        return 5
        """
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]


    
    def numTrees(self, n):
        @lru_cache(maxsize=None)
        def recur(left, right):
            if left >= right:
                return 1
            res = 0
            for i in range(left, right + 1):
                res += recur(left, i - 1) * recur(i + 1, right)
            return res
        return recur(1, n)
# @lc code=end
