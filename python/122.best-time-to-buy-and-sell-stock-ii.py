#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
#
# algorithms
# Easy (52.09%)
# Total Accepted:    333.6K
# Total Submissions: 639.6K
# Testcase Example:  '[7,1,5,3,6,4]'
#
# Say you have an array for which the ith element is the price of a given stock
# on day i.
# 
# Design an algorithm to find the maximum profit. You may complete as many
# transactions as you like (i.e., buy one and sell one share of the stock
# multiple times).
# 
# Note: You may not engage in multiple transactions at the same time (i.e., you
# must sell the stock before you buy again).
# 
# Example 1:
# 
# 
# Input: [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit =
# 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 =
# 3.
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit =
# 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you
# are
# engaging multiple transactions at the same time. You must sell before buying
# again.
# 
# 
# Example 3:
# 
# 
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# 
#
class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    def maxProfit(self, prices):
        n = len(prices)
        i = 0
        profit = 0
        while i < n:
            j = i+1
            # print(i,j)
            update = False
            while j < n:
                k = j+1
                # print(i,j,k)
                if k < n and prices[j] - prices[i] > 0 and prices[j] - prices[k] > 0:
                    profit += prices[j] - prices[i]
                    # print('update', i, j, k)
                    # print(prices[i], prices[j], prices[k])
                    # print('profit=', profit)
                    i = j+1
                    j = i+1
                    update = True
                # elif k < n and prices[i] - prices[j] > 0 and prices[k] - prices[j] > 0:
                elif k < n and prices[i] - prices[j] >= 0:
                    # print('here', i,j,k)
                    i = j
                    j = i+1
                    update = True
                elif k == n - 1 and prices[k] - prices[i] > 0:
                    profit += prices[k] - prices[i]
                    i = n
                    j = n
                elif k == n and prices[j] > prices[i]:
                    # print('here')
                    profit += prices[j] - prices[i]
                    i = n
                    j = n
                else:
                    # print('here')
                    j += 1
            if not update:
                i += 1
        return profit


# s = Solution()
# prices = [7,1,5,3,6,4]
# print(s.maxProfit(prices) == 7)

# prices = [1,2,3,4,5]
# print(s.maxProfit(prices) == 4)

# prices = [7,6,4,3,1]
# print(s.maxProfit(prices) == 0)

# prices = [6,1,3,2,4,7]
# print(s.maxProfit(prices) == 7)


# prices = [1,2]
# print(s.maxProfit(prices) == 1)







# # print(len(prices))
# # print(prices[10003], prices[10004], prices[10005])
# print(s.maxProfit(prices) == 4)


















        
