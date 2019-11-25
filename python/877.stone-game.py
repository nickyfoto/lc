#
# @lc app=leetcode id=877 lang=python3
#
# [877] Stone Game
#
# https://leetcode.com/problems/stone-game/description/
#
# algorithms
# Medium (61.97%)
# Total Accepted:    32.4K
# Total Submissions: 52.1K
# Testcase Example:  '[5,3,4,5]'
#
# Alex and Lee play a game with piles of stones.  There are an even number of
# piles arranged in a row, and each pile has a positive integer number of
# stones piles[i].
# 
# The objective of the game is to end with the most stones.  The total number
# of stones is odd, so there are no ties.
# 
# Alex and Lee take turns, with Alex starting first.  Each turn, a player takes
# the entire pile of stones from either the beginning or the end of the row.
# This continues until there are no more piles left, at which point the person
# with the most stones wins.
# 
# Assuming Alex and Lee play optimally, return True if and only if Alex wins
# the game.
# 
# 
# 
# Example 1:
# 
# 
# Input: [5,3,4,5]
# Output: true
# Explanation: 
# Alex starts first, and can only take the first 5 or the last 5.
# Say he takes the first 5, so that the row becomes [3, 4, 5].
# If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10
# points.
# If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win
# with 9 points.
# This demonstrated that taking the first 5 was a winning move for Alex, so we
# return true.
# 
# 
# 
# 
# Note:
# 
# 
# 2 <= piles.length <= 500
# piles.length is even.
# 1 <= piles[i] <= 500
# sum(piles) is odd.
# 
#
class Solution:
    # def stoneGame(self, piles: List[int]) -> bool:
    def stoneGame2(self, piles):
        def recur(piles):
            n = len(piles)
            if n == 2:
                return abs(piles[0] - piles[1])
            elif n % 2 == 1:
                left = piles[0] - recur(piles[1:])
                right = piles[-1] - recur(piles[:-1])
                return - max(left, right)
                
            else:
                left = piles[0] + recur(piles[1:])
                right = piles[-1] + recur(piles[:-1])
                return max(left, right)
        res = recur(piles)
        if res > 0:
            return True
        return False
    

    def stoneGame(self, piles):
        n = len(piles)
        piles.sort(reverse=True)
        # print(piles)
        # print(list(range(0, 10, 2)))
        total = sum(piles)
        a = sum([piles[i] for i in range(0, n, 2)])
        # print(a)
        return a > total - a


# s = Solution()
# piles = [5,3,4,5]
# print(s.stoneGame(piles))

# import random
# while True:
#     piles = random.choices(range(1,10), k=22)
#     if sum(piles) % 2 == 1:
#         print(piles)
#         print(s.stoneGame(piles))
#         break

# piles = [7,7,12,16,41,48,41,48,11,9,34,2,44,30,27,12,11,39,31,8,23,11,47,25,15,23,4,17,11,50,16,50,38,34,48,27,16,24,22,48,50,10,26,27,9,43,13,42,46,24]
# print(s.stoneGame(piles))



