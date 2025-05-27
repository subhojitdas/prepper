from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adjacency_map = {c: set() for w in words for c in w}

        for w1, w2 in zip(words[:-1], words[1:]):
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""
            for idx in range(min_len):
                if w1[idx] != w2[idx]:
                    adjacency_map[w1[idx]].add(w2[idx])
                    break
        visit = {}
        res = []

        def dfs(ch):
            if ch in visit:
                return visit[ch]
            visit[ch] = True

            for nei in adjacency_map[ch]:
                if dfs(nei):
                    return True

            visit[ch] = False
            res.append(ch)

        for c in adjacency_map:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)



a = Solution().alienOrder(["wrt","wrf","er","ett","rftt"])
print(a)


