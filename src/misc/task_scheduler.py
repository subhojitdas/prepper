from collections import deque
from typing import List


class MaxHeap:
    def __init__(self, nums: List[int]):
        self.nums = []
        self._heapify(nums)

    def _heapify(self, nums: List[int]):
        for elem in nums:
            self.insert(elem)

    def insert(self, elem):
        self.nums.append(elem)
        length = len(self.nums)
        self._swim(length - 1)

    def pop(self):
        elem = self.nums[0]
        self.nums[0], self.nums[-1] = self.nums[-1], self.nums[0]
        self.nums.pop()
        self.sink(0)
        return elem

    def _swim(self, idx):
        par_idx = self._parent(idx)
        while par_idx >= 0 and self.nums[par_idx] < self.nums[idx]:
            self.nums[par_idx], self.nums[idx] = self.nums[idx], self.nums[par_idx]
            idx = par_idx
            par_idx = self._parent(idx)

    def sink(self, idx):
        left, right = self._children(idx)
        while left < len(self.nums):
            switch_idx = left
            if right < len(self.nums) and self.nums[left] < self.nums[right]:
                switch_idx = right
            self.nums[idx], self.nums[switch_idx] = self.nums[switch_idx], self.nums[idx]
            idx = switch_idx
            left, right = self._children(idx)

    def empty(self):
        return len(self.nums) == 0

    def _children(self, idx: int) -> List[int]:
        left = 2 * idx + 1
        right = 2 * idx + 2
        return left, right

    def _parent(self, idx: int) -> int:
        parent = (idx - 1) // 2
        return parent

    def print_heap(self):
        print(self.nums)

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = {}
        for task in tasks:
            counts[task] = counts.get(task, 0) + 1

        max_heap = MaxHeap(counts.values())
        t = 0
        q = deque()
        while not max_heap.empty() or q:
            t += 1
            if not max_heap.empty():
                max_idx = max_heap.pop()
                next_awake_time = t + n
                cnt = max_idx - 1
                if cnt > 0:
                    q.append([cnt, next_awake_time])
            if q and q[0][1] == t:
                elem = q.popleft()
                max_heap.insert(elem[0])
        return t

#
# m = MaxHeap([1,5,11,5, 6, 18, 12, 24])
# m.print_heap()

a = Solution().leastInterval(["A","B","C","A","B"], 2)
print(a)



