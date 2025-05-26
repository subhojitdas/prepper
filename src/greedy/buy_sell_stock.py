from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            buy = prices[left]
            sell = prices[right]
            profit = sell - buy
            if profit < 0:
                left  = right
            right = right + 1
            max_profit = max(max_profit, profit)
        return max_profit


a = Solution().maxProfit([2,1,2,1,0,1,2])
print(a)