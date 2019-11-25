#
# @lc app=leetcode id=1040 lang=python3
#
# [1040] Moving Stones Until Consecutive II
#
# https://leetcode.com/problems/moving-stones-until-consecutive-ii/description/
#
# algorithms
# Medium (48.16%)
# Total Accepted:    2.4K
# Total Submissions: 5.1K
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
class Solution:
    # def numMovesStonesII(self, stones: List[int]) -> List[int]:
    def numMovesStonesII(self, stones):
        n = len(stones)
        stones.sort()
        low = n
        i = 0
        high = max(stones[-1] - n + 2 - stones[1], stones[-2] - stones[0] - n + 2)
        for j in range(n):
            while stones[j] - stones[i] >= n:
                i += 1
            # j - i + 1 refers to number of stones 
            # between stones[i] and stones[j], i <= j
            # when i < j means stones[i] and stones[j] are within range n
            # when i == j means for stones[j], there's no neighboring stones
            # within distance n
            # print('j=', j, 'i=', i)
            # print(stones[i], stones[j])
            if j - i + 1 == n - 1 and stones[j] - stones[i] == n - 2:
                print('here', j, i, 'low=', low)
                low = min(low, 2)
                print('after here low=', low)
            else:
                # print('j=', j, 'i=', i, 'low=', low)
                low = min(low, n - (j - i + 1))
                # print('low=', low)
        return [low, high]


s = Solution()
stones = [7,4,9]
print(s.numMovesStonesII(stones) == [1,2])

stones = [100,101,104,102,103]
# print(s.numMovesStonesII(stones) == [0,0])


stones = [6,5,4,3,10]
print(s.numMovesStonesII(stones) == [2,3])

stones = [872744873,407745415,920265824,78944478,811582493,159387457,73610667,679739704,934249520,484866256,806947986,515330462,635589397,454065412,623990088,702300851,680116257,956576624,627580519,862260761,535974224,610386154,147996010,995188988,697589181,774334991,975600945,349769864,439419437,759685564,468162177,245675630,618666885,534580630,600325762,986524516,161373519,515248771,925900095,557803426,201601082,982652719,295010345,293049701,338675863,649482376,24971924,518429551,298902749,525841475,207922745,786121605,278541349,171822421,3627955,941822192,327185070,282505850,375060226,263830781,375519322,394162353,159428107,698554237,386248496,401174973,713865493,151618885,43008984,135449254,903873357,926871727,700962,415801910,241575747,913603096,921875839,515695485,801132907,210025056,991525254,776633422,319846045,510206317,433255537,964734911,487539862,958994600,267736477,640426157,348772981,813284734,165097998,328011830,107586878,920355296,822257896,74535996,508877402,55905987,912504311,238858217,101604373,866717345,889976872,236460070,243264031,676579831,222034958,233732642,746488332,719718853,630787678,511639505,672351188,959300625,169663603,191716458,681437267,415179364,252436682,427793128,335408586,585450571,894449031]
# print(s.numMovesStonesII(stones))




















        
