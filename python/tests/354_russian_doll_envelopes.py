#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#
# https://leetcode.com/problems/russian-doll-envelopes/description/
#
# algorithms
# Hard (34.83%)
# Likes:    871
# Dislikes: 34
# Total Accepted:    58.2K
# Total Submissions: 167K
# Testcase Example:  '[[5,4],[6,4],[6,7],[2,3]]'
#
# You have a number of envelopes with widths and heights given as a pair of
# integers (w, h). One envelope can fit into another if and only if both the
# width and height of one envelope is greater than the width and height of the
# other envelope.
# 
# What is the maximum number of envelopes can you Russian doll? (put one inside
# other)
# 
# Note:
# Rotation is not allowed.
# 
# Example:
# 
# 
# 
# Input: [[5,4],[6,4],[6,7],[2,3]]
# Output: 3 
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3]
# => [5,4] => [6,7]).
# 
# 
# 
#

# @lc code=start
from bisect import bisect_left
class Solution:
    # def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
    def maxEnvelopes(self, envelopes):
        """
        brute force ETL
        """
        # if not envelopes: return 0
        # n = len(envelopes)
        # s = sorted(envelopes)
        # dp = [1] * n
        # for i in range(n):
        #     temp = [dp[j] + 1 for j in range(i) if s[j][0] < s[i][0] and s[j][1] < s[i][1]]
        #     if temp:
        #         dp[i] = max(temp)
        # return max(dp)

        # envelopes.sort(key=lambda x: (x[0], -x[1]))
        # make sure that we only need to find LIS of the height because 
        # envelope with same width must be before current because 
        # high height is before low height

        ########################################

        envelopes.sort(key=lambda x: (x[0], -x[1]))

        def lis(nums):
            dp = []
            for i in range(len(nums)):
                idx = bisect_left(dp, nums[i])
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
            return len(dp)
        return lis([i[1] for i in envelopes])

# @lc code=end
