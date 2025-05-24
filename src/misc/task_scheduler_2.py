from typing import List


class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        counts = {}
        for task in tasks:
            counts[task] = 1

        idx = 0
        t = 0
        while idx < len(tasks):
            t += 1
            task = tasks[idx]
            if task in counts:
                next_awake_time = counts[task]
                if next_awake_time <= t:
                    idx += 1
                    counts[task] = t + space + 1
                else:
                    t = next_awake_time
                    idx += 1
                    counts[task] = t + space + 1
            else:
                idx += 1
                counts[task] = t + space
        return t


a = Solution().taskSchedulerII([4,10,10,9,10,4,10,4], 8)
print(a)