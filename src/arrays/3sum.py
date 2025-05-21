from typing import List
import random

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.quick_sort(nums, 0, len(nums) - 1)
        res = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                t = a + nums[l] + nums[r]
                if t < 0:
                    l += 1
                elif t > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res


    def quick_sort(self, nums: List[int], left, right) -> List[List[int]]:
        if left >= right:
            return

        def partition(left, right):
            ran_index = random.randint(left, right)
            pivot = nums[ran_index]
            nums[ran_index], nums[right] = nums[right], nums[ran_index]

            l, r = left - 1, left

            while r < right:
                if nums[r] < pivot:
                    l += 1
                    nums[l], nums[r] = nums[r], nums[l]
                r += 1
            nums[l + 1], nums[right] = nums[right], nums[l + 1]
            return l + 1

        pivot = partition(left, right)
        self.quick_sort(nums, left, pivot - 1)
        self.quick_sort(nums, pivot + 1, right)

#
# for i in range(10):
#     a = [5,1, 2, 6]
#     Solution().quick_sort(a, 0, len(a)-1)
#     print(a)

a = Solution().threeSum([0, 0, 0])
print(a)


