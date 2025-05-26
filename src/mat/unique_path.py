# class Solution:
    # def uniquePaths(self, m: int, n: int) -> int:
    #     dir = [[0,1], [1,0]]
    #     visited = [[False] * n for _ in range(m)]
    #     ans = 0
    #
    #     def dfs(row, col):
    #         nonlocal ans
    #         if row == m-1 and col == n-1:
    #             ans += 1
    #             return
    #
    #         if row >= m or col >= n or row < 0 or col < 0 or visited[row][col]:
    #             return
    #         visited[row][col] = True
    #
    #         for d in dir:
    #             dfs(row + d[0], col + d[1])
    #         visited[row][col] = False
    #
    #     dfs(0, 0)
    #     return ans

import math

# lol!
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # (m-1) downs + (n-1) right choose (m-1) [or (n-1)]
        return math.comb(m + n - 2, m - 1)


a = Solution().uniquePaths(23, 12)
print(a)