from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])
        dir = [[0, 1], [1, 0]]
        cache = {}

        def dfs(r, c):
            if (r, c) in cache:
                return cache[(r,c)]
            if r >= ROW or c >= COL or r < 0 or c < 0:
                return float('inf')
            if r == ROW - 1 and c == COL - 1:
                return grid[r][c]

            min_path = float('inf')
            for dr, dc in dir:
                p1 = dfs(r + dr, c + dc)
                min_path = min(min_path, p1)
            cache[(r,c)] = min_path + grid[r][c]
            return cache[(r,c)]

        p = dfs(0, 0)
        return p

grid = [[1,3,1],[1,5,1],[4,2,1]]
a = Solution().minPathSum(grid)
print(a)


