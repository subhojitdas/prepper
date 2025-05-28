from typing import List

class TrieNode:
    dictionary = {}
    end_of_word = False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if len(words) == 0:
            return []
        R = len(board)
        C = len(board[0])
        ans = set()

        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        used = [[False] * C for _ in range(R)]

        root = {}
        for word in words:
            current = root

            for c in word:
                if c not in current:
                    current[c] = {}
                current = current[c]
            current["$"] = ""

        def recurse(x, y, current, node):
            if "$" in node:
                ans.add("".join(current))
                del node["$"]
            for dx, dy in dir:
                nx, ny = x + dx, y + dy

                if 0 <= nx < R and 0 <= ny < C:
                    if not used[nx][ny] and board[nx][ny] in node:
                        used[nx][ny] = True
                        current.append(board[nx][ny])
                        recurse(nx, ny, current, node[board[nx][ny]])
                        if len(node[board[nx][ny]]) == 0:
                            del node[board[nx][ny]]
                        current.pop()
                        used[nx][ny] = False
        for i in range(R):
            for j in range(C):
                if board[i][j] in root:
                    used[i][j] = True
                    recurse(i, j, [board[i][j]], root[board[i][j]])
                    used[i][j] = False

        return list(ans)


s = [["a", "a"]]
w = ["aaa"]
a = Solution().findWords(s, w)
print(a)

