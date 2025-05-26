from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROW = len(obstacleGrid)
        COL = len(obstacleGrid[0])
        dir = [[0,1], [1,0]]
        # visited = [[False] * COL for _ in range(ROW)]
        cache = {}

        def dfs(r, c):
            if obstacleGrid[r][c] == 1:
                return 0
            if (r, c) in cache:
                return cache[(r,c)]
            if r == ROW - 1 and c == COL - 1:
                return 1
            if r >= ROW or c >= COL or r < 0 or c < 0:
                return 0
            count = 0
            for dx, dy in dir:
                if (r+dx) < ROW and (r+dx) >= 0 and (c+dy) < COL and (c+dy) >= 0 and obstacleGrid[r+dx][c+dy] == 0:
                    count += dfs(r + dx, c + dy)
            cache[(r,c)] = count
            return count

        return dfs(0, 0)


obs = [[0,0,0],[0,0,0],[0,0,0]]
a = Solution().uniquePathsWithObstacles(obs)
print(a)





