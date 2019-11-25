#
# @lc app=leetcode id=1033 lang=python3
#
# [1033] Moving Stones Until Consecutive
#
# https://leetcode.com/problems/moving-stones-until-consecutive/description/
#
# algorithms
# Easy (35.05%)
# Total Accepted:    5.9K
# Total Submissions: 16.7K
# Testcase Example:  '1\n2\n5'
#
# Three stones are on a number line at positions a, b, and c.
# 
# Each turn, you pick up a stone at an endpoint (ie., either the lowest or
# highest position stone), and move it to an unoccupied position between those
# endpoints.  Formally, let's say the stones are currently at positions x, y, z
# with x < y < z.  You pick up the stone at either position x or position z,
# and move that stone to an integer position k, with x < k < z and k != y.
# 
# The game ends when you cannot make any more moves, ie. the stones are in
# consecutive positions.
# 
# When the game ends, what is the minimum and maximum number of moves that you
# could have made?  Return the answer as an length 2 array: answer =
# [minimum_moves, maximum_moves]
# 
# 
# 
# Example 1:
# 
# 
# Input: a = 1, b = 2, c = 5
# Output: [1,2]
# Explanation: Move the stone from 5 to 3, or move the stone from 5 to 4 to
# 3.
# 
# 
# 
# Example 2:
# 
# 
# Input: a = 4, b = 3, c = 2
# Output: [0,0]
# Explanation: We cannot make any moves.
# 
# 
# 
# Example 3:
# 
# 
# Input: a = 3, b = 5, c = 1
# Output: [1,2]
# Explanation: Move the stone from 1 to 4; or move the stone from 1 to 2 to
# 4.
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= a <= 100
# 1 <= b <= 100
# 1 <= c <= 100
# a != b, b != c, c != a
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
#
class Solution:
    # def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
    def numMovesStones(self, a, b, c):
        self.min = 0
        self.max = 0
        def recur_min(l, m, h):
            if h - l == 2:
                return self.min
            else:
                if m - l == 1:
                    self.min += 1
                    return recur_min(l, m, m+1)
                elif h - m == 1:
                    self.min += 1
                    return recur_min(m-1, m, h)
                else:
                    if m - l < h - m:
                        self.min += 1
                        return recur_min(l, l+1, m)
                    else:
                        self.min += 1
                        return recur_min(m, m+1, h)
        def recur_max(l, m, h):
            if h - l == 2:
                return self.max
            else:
                if m - l == 1:
                    self.max += 1
                    return recur_max(l, m, h-1)
                elif h - m == 1:
                    self.max += 1
                    return recur_max(l+1, m, h)
                elif h - m > 1:
                    self.max += 1
                    return recur_max(l, m, h - 1)
                elif m - l > 1:
                    self.max += 1
                    return recur_max(l+1, m, h)
        s = sorted([a, b, c])
        return [recur_min(*s), recur_max(*s)]


# s = Solution()
# a = 1
# b = 2
# c = 5
# print(s.numMovesStones(a, b, c) == [1,2])

# a = 4
# b = 3
# c = 2
# print(s.numMovesStones(a, b, c) == [0,0])


# a = 3
# b = 5
# c = 1
# print(s.numMovesStones(a, b, c) == [1, 2])

# a = 1
# b = 3
# c = 6
# print(s.numMovesStones(a, b, c))


