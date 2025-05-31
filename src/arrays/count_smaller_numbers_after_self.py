from typing import List


# class Solution1: # O(N^2)
#     def countSmaller(self, nums: List[int]) -> List[int]:
#         N = len(nums)
#         count = []
#         for idx, x in enumerate(nums):
#             curr = nums[idx]
#             min_count = 0
#             for j in range(idx + 1, N):
#                 if curr > nums[j]:
#                     min_count += 1
#             count[idx] = min_count
#         return count


LSB = lambda x: x & -x

class BinaryIndexTreeThree:
    def __init__(self, N):
        self.stree = [0] * (N + 1)

    def increase(self, i, x):
        while i < len(self.stree):
            self.stree[i] += x
            # i |= (i + 1)
            i += LSB(i)

    def total(self, i):
        s = 0
        while i > 0:
            s += self.stree[i]
            # i &= i + 1
            # i -= 1
            i -= LSB(i)
        return s


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        N = len(nums)
        count = [0] * N
        

