from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        A = -prices[0]
        B = float('-inf')
        C = float('-inf')
        D = float('-inf')

        for price in prices:
            A = max(A, -price)
            B = max(B, A + price)
            C = max(C, B - price)
            D = max(D, C + price)
        return D

a = Solution().maxProfit([3,3,5,0,0,3,1,4])
print(a)
