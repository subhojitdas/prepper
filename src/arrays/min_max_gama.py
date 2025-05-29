from typing import List


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        while len(nums) > 1:
            N = len(nums)
            rn = int(N / 2)
            new_nums = [0] * rn
            for i in range(rn):
                if i % 2 == 0:
                    new_nums[i] = min(nums[2 * i], nums[2 * i + 1])
                else:
                    new_nums[i] = max(nums[2 * i], nums[2 * i + 1])
            nums = new_nums
        return nums[0]
