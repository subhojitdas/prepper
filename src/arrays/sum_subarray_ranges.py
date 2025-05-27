from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        N = len(nums)
        total = 0

        for i in range(N):
            smallest = nums[i]
            largest = nums[i]

            for j in range(i+1, N):
                smallest = min(smallest, nums[j])
                largest = max(largest, nums[j])
                total += largest - smallest
        return total
