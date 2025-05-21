from typing import List


class Solution1(object):
    def twoSum(self, nums, target):
        num_hash = {}

        for i in range(len(nums)):
            choosed = target - nums[i]
            if choosed not in num_hash:
                num_hash[nums[i]] = i
            else:
                t = num_hash[choosed]
                return [t, i]


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s > target:
                r = r - 1
            elif s < target:
                l = l + 1
            else:
                return [l, r]
        return []
