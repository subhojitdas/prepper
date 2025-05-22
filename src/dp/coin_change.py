from typing import List


class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != amount + 1 else -1

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        amount_arr = list(reversed(list(range(amount + 1))))
        dp = [[0] * amount + [1] for _ in range(len(coins))]
        for i in range(len(coins) - 1, -1, -1):
            for j in range(amount - 1, -1, -1):
                aright = 0
                if amount_arr[j] - coins[i] >= 0:
                    j_idx = amount - (amount_arr[j] - coins[i])
                    aright = dp[i][j_idx]
                abottom = 0
                if i < len(coins) - 1:
                    abottom = dp[i + 1][j]
                dp[i][j] = abottom + aright
        return dp[0][0]




a = Solution().change(3, [2])
print(a)