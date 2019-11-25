#
# @lc app=leetcode id=914 lang=python3
#
# [914] X of a Kind in a Deck of Cards
#
# https://leetcode.com/problems/x-of-a-kind-in-a-deck-of-cards/description/
#
# algorithms
# Easy (34.26%)
# Total Accepted:    18.1K
# Total Submissions: 53K
# Testcase Example:  '[1,2,3,4,4,3,2,1]'
#
# In a deck of cards, each card has an integer written on it.
# 
# Return true if and only if you can choose X >= 2 such that it is possible to
# split the entire deck into 1 or more groups of cards, where:
# 
# 
# Each group has exactly X cards.
# All the cards in each group have the same integer.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,3,4,4,3,2,1]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,1,1,2,2,2,3,3]
# Output: false
# Explanation: No possible partition.
# 
# 
# 
# Example 3:
# 
# 
# Input: [1]
# Output: false
# Explanation: No possible partition.
# 
# 
# 
# Example 4:
# 
# 
# Input: [1,1]
# Output: true
# Explanation: Possible partition [1,1]
# 
# 
# 
# Example 5:
# 
# 
# Input: [1,1,2,2,2,2]
# Output: true
# Explanation: Possible partition [1,1],[2,2],[2,2]
# 
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= deck.length <= 10000
# 0 <= deck[i] < 10000
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
# 
#
class Solution:
    # def hasGroupsSizeX(self, deck: List[int]) -> bool:
    def hasGroupsSizeX(self, deck):
        n = len(deck)
        st = list(set(deck))
        st.sort()
        num_unique = len(st)
        count = [deck.count(x) for x in st]
        if len(set(count)) == 1 and list(set(count))[0] > 1:
            return True
        # print(st)
        # print(count)
        order_by_count = sorted(range(num_unique), key=lambda k: count[k])
        # print(order_by_count)
        # print([count[o] for o in order_by_count])
        

        import math
        def primeFactors(n): 
            res = []
            # Print the number of two's that divide n 
            while n % 2 == 0: 
                # print(2, end=',')
                if 2 not in res:
                    res.append(2)
                n = n // 2
                  
            # n must be odd at this point 
            # so a skip of 2 ( i = i + 2) can be used 
            for i in range(3,int(math.sqrt(n))+1,2): 
                  
                # while i divides n , print i ad divide n 
                while n % i == 0: 
                    # print(i,end=',') 
                    if i not in res:
                        res.append(i)
                    n = n // i 
                      
            # Condition if n is a prime 
            # number greater than 2 
            if n > 2: 
                res.append(n)
            return res      


        if count[order_by_count[0]] < 2:
            return False
        factors = primeFactors(count[order_by_count[0]])
        # factors = primeFactors(315)
        # print(factors)
        
        for f in factors:
            if all([x % f == 0 for x in count]):
                return True

        return False




























