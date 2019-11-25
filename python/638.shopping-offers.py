#
# @lc app=leetcode id=638 lang=python3
#
# [638] Shopping Offers
#
# https://leetcode.com/problems/shopping-offers/description/
#
# algorithms
# Medium (49.78%)
# Total Accepted:    23.8K
# Total Submissions: 47.8K
# Testcase Example:  '[2,5]\n[[3,0,5],[1,2,10]]\n[3,2]'
#
# 
# In LeetCode Store, there are some kinds of items to sell. Each item has a
# price.
# 
# 
# 
# However, there are some special offers, and a special offer consists of one
# or more different kinds of items with a sale price.
# 
# 
# 
# You are given the each item's price, a set of special offers, and the number
# we need to buy for each item.
# The job is to output the lowest price you have to pay for exactly certain
# items as given, where you could make optimal use of the special offers.
# 
# 
# 
# Each special offer is represented in the form of an array, the last number
# represents the price you need to pay for this special offer, other numbers
# represents how many specific items you could get if you buy this offer.
# 
# 
# You could use any of special offers as many times as you want.
# 
# Example 1:
# 
# Input: [2,5], [[3,0,5],[1,2,10]], [3,2]
# Output: 14
# Explanation: 
# There are two kinds of items, A and B. Their prices are $2 and $5
# respectively. 
# In special offer 1, you can pay $5 for 3A and 0B
# In special offer 2, you can pay $10 for 1A and 2B. 
# You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer
# #2), and $4 for 2A.
# 
# 
# 
# Example 2:
# 
# Input: [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]
# Output: 11
# Explanation: 
# The price of A is $2, and $3 for B, $4 for C. 
# You may pay $4 for 1A and 1B, and $9 for 2A ,2B and 1C. 
# You need to buy 1A ,2B and 1C, so you may pay $4 for 1A and 1B (special offer
# #1), and $3 for 1B, $4 for 1C. 
# You cannot add more items, though only $9 for 2A ,2B and 1C.
# 
# 
# 
# Note:
# 
# There are at most 6 kinds of items, 100 special offers.
# For each item, you need to buy at most 6 of them.
# You are not allowed to buy more items than you want, even if that would lower
# the overall price.
# 
# 
#
from functools import lru_cache
class Solution:
    # def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
    def shoppingOffers(self, price, special, needs):
        n = len(needs)

        def valid(special):
            return all([n-s>=0 for n,s in zip(needs, special)])
        valid_offers = filter(valid, special)
        
        specials = list(valid_offers)
        
        def get_options(item_idx, needs, costs):
            single = [0] * n
            single[item_idx] = 1
            options = [(single, price[item_idx],needs, costs)]
            for special in specials:
                item_list, cost = special[:-1], special[-1]
                if item_list[item_idx] > 0:
                    # print('checking', needs, item_list)
                    if all([ n - i >= 0 for n, i in zip(needs, item_list)]):
                        options.append((item_list, cost, needs, costs))
            # print(needs, options)
            return options

        self.costs = sum(p*n for p,n in zip(price, needs))
        if not specials:
            return self.costs
        # print('self.costs=', self.costs)

        

        @lru_cache(None)
        def dfs(needs, costs):
            # print('starting needs=', needs)
            if costs > self.costs:
                return
            if sum(needs) == 0:
                self.costs = min(costs, self.costs)
                # print("updated self.costs=", self.costs)
            for item_idx in range(n):
                if needs[item_idx] > 0:
                    # print('item_idx=', item_idx)
                    for item_list, cost, needs, costs in get_options(item_idx=item_idx, needs=needs, costs=costs):
                        # print('needs before purchase', needs, 'costs=', costs)
                        # print('purchase=', item_list, cost)
                        needs = list(need - qty for need, qty in zip(needs, item_list))
                        costs += cost
                        # print('updated needs=', needs)
                        # print('costs=', costs)
                        # print('='*30)
                        dfs(tuple(needs), costs)



        dfs(tuple(needs), costs=0)
        # print(self.costs)
        return self.costs


# s = Solution()
# price = [2,5]
# special = [[3,0,5],[1,2,10]]
# needs = [3,2]
# print(s.shoppingOffers(price, special, needs))




# price = [2,3,4]
# special = [[1,1,0,4],[2,2,1,9]]
# needs = [1,2,1]
# print(s.shoppingOffers(price, special, needs))




# price = [4,10,1,5,5,3]
# special = [[1,2,3,3,4,1,8],[3,4,5,5,5,2,14],[2,4,5,1,1,3,22]]
# needs = [1,6,5,1,1,4]
# print(s.shoppingOffers(price, special, needs))








        
