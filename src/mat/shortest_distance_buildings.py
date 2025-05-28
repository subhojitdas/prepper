from typing import List


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        best = float('inf')
        dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def solve(sx, sy):
            q = []
            dist = [[float('inf')] * C for _ in range(R)]
            q.append((sx, sy))
            dist[sx][sy] = 0
            while q:
                x, y = q.pop()
                for dx, dy in dir:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < R and 0 <= ny < C:
                        if grid[nx][ny] == 0 and dist[nx][ny] == float('inf'):
                            dist[nx][ny] = dist[x][y] + 1
                            q.append((nx, ny))
                        elif grid[nx][ny] == 1 and dist[nx][ny] == float('inf'):
                            dist[nx][ny] = dist[x][y] + 1
            total = 0
            for i in range(R):
                for j in range(C):
                    if grid[i][j] == 1:
                        total += dist[i][j]
            return total

        for r in range(R):
            for c in range(C):
                if grid[r][c] != 0:
                    continue
                v = solve(r, c)
                print(r, c, v)
                best = min(best, v)

        if best >= float('inf'):
            return -1
        return best

grid = [
    [1,1,1,1,1,0],
    [0,0,0,0,0,1],
    [0,1,1,0,0,1],
    [1,0,0,1,0,1],
    [1,0,1,0,0,1],
    [1,0,0,0,0,1],
    [0,1,1,1,1,0]
]
a = Solution().shortestDistance(grid)
print(a)

