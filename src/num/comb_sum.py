from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(idx, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target or idx >= len(candidates):
                return

            cur.append(candidates[idx])
            prev_total = total
            total += candidates[idx]
            dfs(idx, cur, total)
            cur.pop()
            dfs(idx + 1, cur, prev_total)
        dfs(0, [], 0)
        return res


a = Solution().combinationSum([2, 3, 6, 7], 7)
print(a)
