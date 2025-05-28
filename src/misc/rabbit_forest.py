import collections
from typing import List
import math


class Solution:
    def numRabbits(self, answers: List[int]) -> int:

        freq = collections.Counter(answers)
        total = 0
        for k in freq.keys():
            groups = math.ceil(freq[k] / (k + 1))
            rabbits_per_group = (k + 1)
            total += groups * rabbits_per_group
        return total


a = Solution().numRabbits([1,1,2])
print(a)