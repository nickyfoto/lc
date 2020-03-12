#
# @lc app=leetcode id=132 lang=python3
#
# [132] Palindrome Partitioning II
#
# https://leetcode.com/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (29.24%)
# Likes:    864
# Dislikes: 29
# Total Accepted:    121.2K
# Total Submissions: 413.4K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# Return the minimum cuts needed for a palindrome partitioning of s.
# 
# Example:
# 
# 
# Input: "aab"
# Output: 1
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1
# cut.
# 
# 
#

# @lc code=start
from functools import lru_cache
class Solution:
    # def minCut(self, s: str) -> int:
    def minCut(self, s):
        """

        dp[j] represents, 


        take "aab" as example
        dp = [-1,0,1,2]

        for i in [1,2]:
            for l, r in (i, i), (i - 1, i):
                # when i == 1
                    l = 1, r = 1
                    while l >= 0 and r < 3 and s[l] == s[r]:
                        dp[r + 1] = min(dp[r + 1], dp[l] + 1)   dp[2] remains the same
                        l <- 0
                        r <- 2
                        s[l] != s[r], break

                    l = 0, r = 1
                    whle l >= 0 and r < 3 and s[l] == s[r]:
                        dp[r + 1] = min(dp[r + 1], dp[l] + 1) dp[2] = 0, dp = [-1,0,0,2]
                        l <- -1
                        r <- 2
                        l < 0, break
                # when i == 2
                    l = r = 2
                    while l >= 0 and r < 3 and s[l] == s[r]:
                        dp[r + 1] = min(dp[r + 1], dp[l] + 1) dp[3] = 1, dp = [-1,0,0,1]
                        l <- 1
                        r <- 3
                        break
                    l = 1, r = 2
                    s[l] != s[r], break
                    
        """
        n = len(s)
        dp = list(range(-1, n))
        # for idx in range(1, n):
        #     for low, high in (idx, idx), (idx - 1, idx):
        #         while low >= 0 and high < n and s[low] == s[high]:
        #             dp[high + 1] = min(dp[high + 1], dp[low] + 1)
        #             low -= 1
        #             high += 1
        # return dp[-1]


        # below can pass OJ but runtime and memory is very high

        # @lru_cache(None)
        # def is_parlindrome(l, r):
        #     if r - l == 1 or r == l:
        #         return True
        #     st = s[l:r]
        #     if st[0] != st[-1]:
        #         return False
        #     return is_parlindrome(l + 1, r - 1)

        # for i in range(2, n + 1):
        #     for j in range(i):
        #         if is_parlindrome(j, i):
        #             dp[i] = min(dp[j] + 1, dp[i])
        # return dp[-1]


        # use matrix to check is_parlindrome
        matrix = [[0] * n for _ in range(n)]
        for mid in range(n):
            i = j = mid
            while 0 <= i and j < n and s[i] == s[j]:
                matrix[i][j] = 1
                i -= 1
                j += 1
            i = mid
            j = mid + 1
            while 0 <= i and j < n and s[i] == s[j]:
                matrix[i][j] = 1
                i -= 1
                j += 1
        for i in range(2, n + 1):
            for j in range(i):
                if matrix[j][i-1]:
                    dp[i] = min(dp[j] + 1, dp[i])
        return dp[-1]
# @lc code=end
