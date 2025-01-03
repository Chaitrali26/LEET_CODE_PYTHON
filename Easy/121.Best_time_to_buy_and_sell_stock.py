class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # prices = [7,1,5,3,6,4]
        '''
        profit = sell - buy
        buy = 1
        sell = 5
        profit = -6
        '''

        max_profit = 0
        buy = prices[0] 
        for i in range(1, len(prices)):
            sell = prices[i] 
            profit = sell - buy 
            '''
            if profit > max_profit:
                max_profit = profit
            '''
            max_profit = max(profit,max_profit)
            buy = min(buy,sell) 
        return max_profit