class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        if len(prices) == 1:
            return maxProfit

        left, right = 0, 1

        while left < len(prices)-1:
            profit = prices[right] - prices[left]

            if maxProfit < profit:
                maxProfit = profit

            if right >= len(prices)-1:
                left +=1
                right = left+1
            else:
                right+=1
        return maxProfit 
            

