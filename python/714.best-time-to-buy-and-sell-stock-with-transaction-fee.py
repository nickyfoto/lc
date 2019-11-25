#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/
#
# algorithms
# Medium (51.57%)
# Total Accepted:    46.3K
# Total Submissions: 89.8K
# Testcase Example:  '[1,3,2,8,4,9]\n2'
#
# Your are given an array of integers prices, for which the i-th element is the
# price of a given stock on day i; and a non-negative integer fee representing
# a transaction fee.
# You may complete as many transactions as you like, but you need to pay the
# transaction fee for each transaction.  You may not buy more than 1 share of a
# stock at a time (ie. you must sell the stock share before you buy again.)
# Return the maximum profit you can make.
# 
# Example 1:
# 
# Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# Buying at prices[0] = 1Selling at prices[3] = 8Buying at prices[4] = 4Selling
# at prices[5] = 9The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
# 
# 
# 
# Note:
# 0 < prices.length .
# 0 < prices[i] < 50000.
# 0 .
# 
#
class Solution:
    # def maxProfit(self, prices: List[int], fee: int) -> int:
    def maxProfit(self, prices, fee: int) -> int:
        

        cash, hold = 0, -prices[0]
        for i in range(1, len(prices)):
            # hold 是假使买了股票之后剩的钱
            # cash - prices[i] 如果买了i股票，剩的钱
            # hold + prices[i] - fee 卖掉手里股票，得到的现金
            # 
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
            # print(cash, hold, prices[i])
        return cash


# s = Solution()
# prices = [1, 3, 2, 8, 4, 9]
# fee = 2
# print(s.maxProfit(prices, fee))

