import bisect
import collections


class Solution:
    def maxSubstrings(self, word: str) -> int:
        N = len(word)

        indices = collections.defaultdict(list)
        for idx, ch in enumerate(word):
            indices[ch].append(idx)

        events = [None] * N
        for idx, ch in enumerate(word):
            nindex = bisect.bisect_left(indices[ch], idx + 3)
            if nindex < len(indices[ch]):
                events[idx] = indices[ch][nindex]


        current = 0
        best = [0] * (N + 1)
        for i in range(N):
            if events[i] is not None:
                nindex = events[i]
                best[nindex] = current + 1
            current = max(current, best[i])
        return current


a = Solution().maxSubstrings("abcdeafdef")
print(a)