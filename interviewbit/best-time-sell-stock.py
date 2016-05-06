"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like 
(ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple
 transactions at the same time (ie, you must sell the stock before you buy again).

Example :

Input : [1 2 3]
Return : 2




arr = [1, 5, 1, 2, 8]
Return: 10

arr = [1, 5, 5, 2, 8]


Input : [1 2 3]
Return : 2

"""

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, prices):
        if not prices: return 0
        n = len(prices)
        total = 0
        for i in range(n - 1):
            if prices[i] < prices[i + 1]:
                total += prices[i + 1] - prices[i]
        return total
        