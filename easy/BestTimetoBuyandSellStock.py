from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        purchase_price = prices[0]
        max_profit = 0
        for p in prices:
            if p < purchase_price:
                purchase_price = p
            else:
                max_profit = max(max_profit, p - purchase_price)
        return max_profit