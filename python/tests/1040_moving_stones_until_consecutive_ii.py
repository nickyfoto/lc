#
# @lc app=leetcode id=1040 lang=python3
#
# [1040] Moving Stones Until Consecutive II
#
# https://leetcode.com/problems/moving-stones-until-consecutive-ii/description/
#
# algorithms
# Medium (52.07%)
# Likes:    152
# Dislikes: 231
# Total Accepted:    4.5K
# Total Submissions: 8.7K
# Testcase Example:  '[7,4,9]'
#
# On an infinite number line, the position of the i-th stone is given by
# stones[i].  Call a stone an endpoint stone if it has the smallest or largest
# position.
# 
# Each turn, you pick up an endpoint stone and move it to an unoccupied
# position so that it is no longer an endpoint stone.
# 
# In particular, if the stones are at say, stones = [1,2,5], you cannot move
# the endpoint stone at position 5, since moving it to any position (such as 0,
# or 3) will still keep that stone as an endpoint stone.
# 
# The game ends when you cannot make any more moves, ie. the stones are in
# consecutive positions.
# 
# When the game ends, what is the minimum and maximum number of moves that you
# could have made?  Return the answer as an length 2 array: answer =
# [minimum_moves, maximum_moves]
# 
# 
# 
# Example 1:
# 
# 
# Input: [7,4,9]
# Output: [1,2]
# Explanation: 
# We can move 4 -> 8 for one move to finish the game.
# Or, we can move 9 -> 5, 4 -> 6 for two moves to finish the game.
# 
# 
# 
# Example 2:
# 
# 
# Input: [6,5,4,3,10]
# Output: [2,3]
# We can move 3 -> 8 then 10 -> 7 to finish the game.
# Or, we can move 3 -> 7, 4 -> 8, 5 -> 9 to finish the game.
# Notice we cannot move 10 -> 2 to finish the game, because that would be an
# illegal move.
# 
# 
# 
# Example 3:
# 
# 
# Input: [100,101,104,102,103]
# Output: [0,0]
# 
# 
# 
# 
# 
# Note:
# 
# 
# 3 <= stones.length <= 10^4
# 1 <= stones[i] <= 10^9
# stones[i] have distinct values.
# 
# 
# 
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def numMovesStonesII(self, stones):
        """
        - n + 2 means minus number of elements in the middle

        [4,7,9]
        stones[-1] - stone[1] = 9 - 7 = 2
        stones[-1] - stone[1] - n + 2 = 9 - 7 - 3 + 2 = 1
        move every stone to the left of the last stone

        stones[-2] - stones[0] = 7 - 4 = 3
        stones[-2] - stones[0] - n + 2 = 7 - 4 - 3 + 2 = 2
        move every stone to the right of the first stone

        [3,4,5,6,10]
        10 - 4 vs 6 - 3

        stones[-1] - stone[1] = 10 - 4 = 6
        stones[-1] - stone[1] - n + 2 = 10 - 4 - 5 + 2 = 3
        stones[-2] - stones[0] = 6 - 3 = 3
        stones[-2] - stones[0] - n + 2 = 6 - 3 - 5 + 2 = 0
        
        stones[j] - stones[i] - 1 = number of slots between stones[j] and stones[i]
        j - i + 1 how many stones from i to j inclusive

        n = 5
        i = 0, j = 0
        stones[j] - stones[i] = 0
        j - i + 1 = 1, stones[j] - stones[i] = 0
        n - (j - i + 1) = 5 - 1 = 4
        
        i = 0, j = 1
        stones[j] - stones[i] = 1
        j - i + 1 = 2, stones[j] - stones[i] = 1
        n - (j - i + 1) = 5 - 2 = 3

        i = 0, j = 2
        stones[j] - stones[i] = 2
        j - i + 1 = 3, stones[j] - stones[i] = 2
        n - (j - i + 1) = 5 - 3 = 2
        
        i = 0, j = 3
        stones[j] - stones[i] = 3
        j - i + 1 = 4, stones[j] - stones[i] = 3 == n - 2
        low = min(2, 2)
        """
        stones.sort()
        i, n, low = 0, len(stones), len(stones)
        high = max(stones[-1] - stones[1] - n + 2 , stones[-2] - stones[0] - n + 2)
        for j in range(n):
            while stones[j] - stones[i] >= n:
                i += 1
            if j - i + 1 == n - 1 and stones[j] - stones[i] == n - 2:
                low = min(low, 2)
            else:
                low = min(low, n - (j - i + 1))
        return [low, high]
# @lc code=end
