from typing import List


class BinaryIndexTree:
    def __init__(self, N):
        self.stree = [0] * (N + 1)

    def increase(self, i, x):
        while i < len(self.stree):
            self.stree[i] += x
            # i |= (i + 1)
            i += (i & -i)

    def total(self, i):
        s = 0
        while i > 0:
            s += self.stree[i]
            # i &= i + 1
            # i -= 1
            i -= (i & -i)
        return s


class NumArray:

    def __init__(self, nums: List[int]):
        self.bit = BinaryIndexTree(len(nums))
        for idx, x in enumerate(nums):
            self.bit.increase(idx + 1, x)
        self.nums = nums

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.bit.increase(index + 1, delta)
        self.nums[index] += delta

    def sumRange(self, left: int, right: int) -> int:
        return self.bit.total(right + 1) - self.bit.total(left)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)