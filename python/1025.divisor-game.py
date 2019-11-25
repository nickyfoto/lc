#
# @lc app=leetcode id=1025 lang=python3
#
# [1025] Divisor Game
#
# https://leetcode.com/problems/divisor-game/description/
#
# algorithms
# Easy (61.35%)
# Total Accepted:    9K
# Total Submissions: 14.6K
# Testcase Example:  '2'
#
# Alice and Bob take turns playing a game, with Alice starting first.
# 
# Initially, there is a number N on the chalkboard.  On each player's turn,
# that player makes a move consisting of:
# 
# 
# Choosing any x with 0 < x < N and N % x == 0.
# Replacing the number N on the chalkboard with N - x.
# 
# 
# Also, if a player cannot make a move, they lose the game.
# 
# Return True if and only if Alice wins the game, assuming both players play
# optimally.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: 2
# Output: true
# Explanation: Alice chooses 1, and Bob has no more moves.
# 
# 
# 
# Example 2:
# 
# 
# Input: 3
# Output: false
# Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more
# moves.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 1000
# 
# 
# 
#
class Solution:
    # def divisorGame(self, N: int) -> bool:
    def divisorGame(self, N, debug=False):
        # print(self.get_max_divisor(10))
        L = [0] * N
        if N > 1:
            L[1] = 1
        if N > 2:
            L[2] = 0
            for i in range(3, N):
                if debug:
                    print("i=", i, L)
                    print(list(range(i-1, -1, -1)))
                for j in range(i-1, -1 ,-1):
                    if L[j] == 0 and (i+1) % (i - j) == 0:
                        if debug:
                            print("j=", j)
                        L[i] = 1
                if debug:
                    print("L=", L)
        if debug:
            print("final L=", L)
        if L[N-1]:
            return True
        return False








# s = Solution()
# N = 1
# print(s.divisorGame(N))
# N = 2
# print(s.divisorGame(N))
# N = 3
# print(s.divisorGame(N))
# N = 4
# print(s.divisorGame(N))
# N = 5
# print(s.divisorGame(N))













