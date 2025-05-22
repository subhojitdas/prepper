from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        max_len = 0
        dir = [[0,1], [0,-1], [1,0], [-1,0]]
        cache = {}

        visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        def dfs(i, j, elems):
            if (i,j) in cache:
                return cache[(i,j)]
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or visited[i][j]:
                return 0

            max_len = 1
            no_match = True
            elems.append(matrix[i][j])
            for d in dir:
                if i >= 0 and i + d[0] < len(matrix) and j >= 0 and j + d[1] < len(matrix[0]):
                    nei = matrix[i + d[0]][j + d[1]]
                    if matrix[i][j] < nei:
                        visited[i][j] = True
                        path_len = 1 + dfs(i + d[0], j + d[1], elems)
                        max_len = max(max_len, path_len)
                        visited[i][j] = False
                        no_match = False
            if no_match:
                print(elems)
            elems.pop()
            cache[(i,j)] = max_len
            return max_len

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                max_len = max(dfs(i, j, []), max_len)
        return max_len


a = Solution().longestIncreasingPath([[0,9,7,0],[7,4,1,9],[2,6,1,3],[8,0,9,9]])
print(a)