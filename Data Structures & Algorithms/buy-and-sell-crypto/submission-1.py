class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        small = prices[0]
        for i in prices: #get small number
            if i < small:
                small = i
            profit = i - small   #calculate profit

            if profit > max_profit: #get bigger profit
                max_profit = profit 
            
        return max_profit




                


        