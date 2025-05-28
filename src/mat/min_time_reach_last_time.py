import heapq
from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        R = len(moveTime)
        C = len(moveTime[0])
        h = []
        best = [[float('inf')] * C for _ in range(R)]
        heapq.heappush(h, (0, 0, 0))
        best[0][0] = 0
        directions = [
            (0,1), (0,-1), (1,0), (-1,0),
        ]

        while h:
            d, x, y = heapq.heappop(h)
            if best[x][y] < d:
                continue
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < R and 0 <= ny < C:
                    cost = max(moveTime[nx][ny] + 1, d + 1)
                    if cost < best[nx][ny]:
                        best[nx][ny] = cost
                        heapq.heappush(h, (cost, nx, ny))
        return best[R - 1][C - 1]
