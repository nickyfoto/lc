#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#
# https://leetcode.com/problems/hand-of-straights/description/
#
# algorithms
# Medium (49.84%)
# Total Accepted:    22K
# Total Submissions: 44.1K
# Testcase Example:  '[1,2,3,6,2,3,4,7,8]\n3'
#
# Alice has a hand of cards, given as an array of integers.
# 
# Now she wants to rearrange the cards into groups so that each group is size
# W, and consists of W consecutive cards.
# 
# Return true if and only if she can.
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].
# 
# Example 2:
# 
# 
# Input: hand = [1,2,3,4,5], W = 4
# Output: false
# Explanation: Alice's hand can't be rearranged into groups of 4.
# 
# 
# 
# Note:
# 
# 
# 1 <= hand.length <= 10000
# 0 <= hand[i] <= 10^9
# 1 <= W <= hand.length
# 
# 
#
from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    'Counter that remembers the order elements are first encountered'

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (OrderedDict(self),)

class Solution:
    # def isNStraightHand(self, hand: List[int], W: int) -> bool:
    def isNStraightHand(self, hand, W):
        hand.sort()
        d = OrderedCounter(hand)
        # print(d)
        for k in d:
            while d[k] > 0:
                d[k] -= 1
                for i in range(k+1, k+W):
                    if d.get(i):
                        if d[i] > 0:
                            d[i] -= 1
                        else:
                            return False
                    else:
                        # print('here', i, 'k=', k, d)
                        return False
        return True
            # return recur(d)
        # print(recur(d))
        # return recur(d)
            # print(d)
        # return all([v == 0 for k, v in d.items()]) 



# s = Solution()
# hand = [1,2,3,6,2,3,4,7,8]
# W = 3
# print(s.isNStraightHand(hand, W))
# hand = [1,2,3,4,5]
# W = 4
# print(s.isNStraightHand(hand, W))
# hand = [1,1,2,2,3,3]
# W = 3
# print(s.isNStraightHand(hand, W)) #true
















