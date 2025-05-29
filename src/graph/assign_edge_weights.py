import collections
from typing import List


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        adj = collections.defaultdict(list)
        for u, v in edges:
            if u < v:
                adj[u].append(v)
            else:
                adj[v].append(u)

        def max_depth(node):
            if len(adj[node]) == 0:
                return 0
            mx_depth = 0
            for e in adj[node]:
                if e > node:
                    m1 = max_depth(e)
                    mx_depth = max(mx_depth, m1)
            return mx_depth + 1

        po = (max_depth(1) - 1)
        return (2**po) % MOD


ed = [[3,2],[2,1]]
a = Solution().assignEdgeWeights(ed)
print(a)

