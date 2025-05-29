import collections
from typing import List


class Solution:
    def maxWeight(self, N: int, edges: List[List[int]], k: int, t: int) -> int:
        e = collections.defaultdict(list)
        for u, v, w in edges:
            e[u].append((v, w))
            # e[v].append((u, w)) # It is a DAG

        # print(e)
        best = -1
        cache = {}

        def go(node, kleft, tleft):
            if (node, kleft, tleft) in cache:
                return cache[(node, kleft, tleft)]
            if tleft <= 0:
                return
            if kleft == 0:
                nonlocal best
                best = max(best, t - tleft)
                return

            for v, w in e[node]:
                cache[node, kleft, tleft] = go(v, kleft - 1, tleft - w)


        for i in range(N):
            go(i, k, t)
        return best


ed = [[0,1,1],[1,2,2]]
a = Solution().maxWeight(3, ed, k = 2, t = 4)
print(a)
