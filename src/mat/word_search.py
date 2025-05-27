from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(word) == 0:
            return False
        R = len(board)
        C = len(board[0])

        dir = [[0,1], [0,-1], [1,0], [-1,0]]
        visited = set()
        def dfs(r, c, idx):
            if idx == len(word):
                return True
            if (r, c) in visited:
                return False

            if r < 0 or r >= R or c < 0 or c >= C:
                return False

            if board[r][c] != word[idx]:
                return False

            visited.add((r, c))
            matched = False
            for dx, dy in dir:
                m1 = dfs(r + dx, c + dy, idx + 1)
                matched = m1 or matched
            visited.remove((r, c))
            return matched

        for rx in range(R):
            for cx in range(C):
                if dfs(rx, cx, 0):
                    return True
        return False


a = Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED")
print(a)



