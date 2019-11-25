#
# @lc app=leetcode id=1128 lang=python3
#
# [1128] Number of Equivalent Domino Pairs
#
# https://leetcode.com/problems/number-of-equivalent-domino-pairs/description/
#
# algorithms
# Easy (44.76%)
# Total Accepted:    9.5K
# Total Submissions: 21.2K
# Testcase Example:  '[[1,2],[2,1],[3,4],[5,6]]'
#
# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] =
# [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is,
# one domino can be rotated to be equal to another domino.
# 
# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and
# dominoes[i] is equivalent to dominoes[j].
# 
# 
# Example 1:
# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1
# 
# 
# Constraints:
# 
# 
# 1 <= dominoes.length <= 40000
# 1 <= dominoes[i][j] <= 9
# 
#
from collections import Counter

class Solution:
    # def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
    def numEquivDominoPairs(self, dominoes) -> int:
        def f(l):
            if l[0] > l[1]:
                return tuple(l[::-1])
            return tuple(l)
        d = list(map(f, dominoes))
        c = Counter(d)
        # print(c)
        res = 0
        for v in c.values():
            if v == 2:
                res += 1
            if v > 2:
                res += v*(v-1) // 2

        # d.sort()
        # res = 0
        # for i in range(len(dominoes) - 1):
            # if d[i] == d[i+1]:
                # res += 1
        # print(d)

        return res

# s = Solution()
# dominoes = [[1,2],[2,1],[3,4],[5,6]]
# print(s.numEquivDominoPairs(dominoes) == 1)
# dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
# print(s.numEquivDominoPairs(dominoes) == 3)

# dominoes = [[2,1],[1,2],[1,2],[1,2],[2,1],[1,1],[1,2],[2,2]]
# print(s.numEquivDominoPairs(dominoes))
# '[[2,1],[1,2],[1,2],[1,2],[2,1],[1,2]'


