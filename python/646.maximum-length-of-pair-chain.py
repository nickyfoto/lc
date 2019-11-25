#
# @lc app=leetcode id=646 lang=python3
#
# [646] Maximum Length of Pair Chain
#
# https://leetcode.com/problems/maximum-length-of-pair-chain/description/
#
# algorithms
# Medium (49.67%)
# Total Accepted:    42.3K
# Total Submissions: 85.2K
# Testcase Example:  '[[1,2], [2,3], [3,4]]'
#
# 
# You are given n pairs of numbers. In every pair, the first number is always
# smaller than the second number.
# 
# 
# 
# Now, we define a pair (c, d) can follow another pair (a, b) if and only if b
# < c. Chain of pairs can be formed in this fashion. 
# 
# 
# 
# Given a set of pairs, find the length longest chain which can be formed. You
# needn't use up all the given pairs. You can select pairs in any order.
# 
# 
# 
# Example 1:
# 
# Input: [[1,2], [2,3], [3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4]
# 
# 
# 
# Note:
# 
# The number of given pairs will be in the range [1, 1000].
# 
# 
#
class Solution:
    # def findLongestChain(self, pairs: List[List[int]]) -> int:
    def findLongestChain(self, pairs) -> int:
        pairs.sort()
        n = len(pairs)
        L = [1] * n
        for i in range(n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0] and L[j] + 1 > L[i]:
                    L[i] = L[j] + 1
        # print(L)

        return max(L)

s = Solution()
pairs = [[1,2], [2,3], [3,4]]
print(s.findLongestChain(pairs))
































        
