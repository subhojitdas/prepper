from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if len(words) == 0:
            return []
        R = len(board)
        C = len(board[0])

        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()



