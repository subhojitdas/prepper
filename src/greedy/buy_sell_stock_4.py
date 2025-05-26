from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0

        B = [float('-inf')] * k
        S = [float('-inf')] * k

        for price in prices:
            B[0] = max(B[0], -price)
            S[0] = max(S[0], B[0] + price)
            for i in range(1, k):
                B[i] = max(B[i], S[i-1] - price)
                S[i] = max(S[i], B[i] + price)
        return S[k - 1]
