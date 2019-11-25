#
# @lc app=leetcode id=464 lang=python3
#
# [464] Can I Win
#
# https://leetcode.com/problems/can-i-win/description/
#
# algorithms
# Medium (27.86%)
# Total Accepted:    40.2K
# Total Submissions: 144.2K
# Testcase Example:  '10\n11'
#
# In the "100 game," two players take turns adding, to a running total, any
# integer from 1..10. The player who first causes the running total to reach or
# exceed 100 wins. 
# 
# What if we change the game so that players cannot re-use integers? 
# 
# For example, two players might take turns drawing from a common pool of
# numbers of 1..15 without replacement until they reach a total >= 100.
# 
# Given an integer maxChoosableInteger and another integer desiredTotal,
# determine if the first player to move can force a win, assuming both players
# play optimally. 
# 
# You can always assume that maxChoosableInteger will not be larger than 20 and
# desiredTotal will not be larger than 300.
# 
# 
# Example
# 
# Input:
# maxChoosableInteger = 10
# desiredTotal = 11
# 
# Output:
# false
# 
# Explanation:
# No matter which integer the first player choose, the first player will lose.
# The first player can choose an integer from 1 up to 10.
# If the first player choose 1, the second player can only choose integers from
# 2 up to 10.
# The second player will win by choosing 10 and get a total = 11, which is >=
# desiredTotal.
# Same with other integers chosen by the first player, the second player will
# always win.
# 
# 
#

from functools import lru_cache
class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        

        s = (1+maxChoosableInteger)*(maxChoosableInteger) //2

        if s < desiredTotal:
            return False

        pool = list(range(1, maxChoosableInteger+1))

        @lru_cache(maxsize=None)
        def recur2(pool, desiredTotal, A):

            # print(pool, desiredTotal, A)
            if pool[-1] >= desiredTotal:
                if A:
                    return True
                else:
                    return False
            if pool[0] + pool[-1] >= desiredTotal:
                # print(pool, desiredTotal, A)
                if A:
                    return False
                else:
                    return True
            if A:
                for i in range(len(pool)-1,-1,-1):
                    # print(pool[i])
                    pc = list(pool).copy()
                    p = pc.pop(i)
                    res = recur2(tuple(pc), desiredTotal - p, not A)
                    # print('p=', p, 'A=', A, 'pool=', pool,'res=', res)
                    if res:
                        return True
                else:
                    return False
            else:
                for i in range(len(pool)-1,-1,-1):
                    # print(pool[i])
                    pc = list(pool).copy()
                    p = pc.pop(i)
                    res = recur2(tuple(pc), desiredTotal - p, not A)
                    # if pool == list(range(1,10)):
                        # print('p=', p, 'A=', A, 'pool=', pool,'res=', res)
                    if not res:
                        return False
                else:
                    return True



        return recur2(tuple(pool), desiredTotal,A=True)






# s = Solution()
# maxChoosableInteger = 10
# desiredTotal = 11
# print(s.canIWin(maxChoosableInteger, desiredTotal) == False)


# maxChoosableInteger = 18
# desiredTotal = 188
# print(s.canIWin(maxChoosableInteger, desiredTotal) == False)


# maxChoosableInteger = 10
# desiredTotal = 40
# print(s.canIWin(maxChoosableInteger, desiredTotal) == False)


# maxChoosableInteger = 4
# desiredTotal = 6
# print(s.canIWin(maxChoosableInteger, desiredTotal))


# maxChoosableInteger = 18
# desiredTotal = 79
# print(s.canIWin(maxChoosableInteger, desiredTotal)) #True




# maxChoosableInteger = 20
# desiredTotal = 210
# print(s.canIWin(maxChoosableInteger, desiredTotal)) #time exceed






