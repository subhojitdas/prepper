from typing import List
import random


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        S = sum(nums)
        if S % 2 == 1:
            return False
        target = S // 2

        dp = set()
        dp.add(0)
        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if t + nums[i] == target:
                    return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return True if target in dp else False


    def binary_search(self, arr: List[int], target: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1




    def quick_sort(self, arr, left, right):
        if left >= right:
            return

        def partition(left, right):
            ran_index = random.randint(left, right)
            arr[ran_index], arr[right] = arr[right], arr[ran_index]
            pivot = arr[right]

            l, r = left - 1, left
            while l <= r and r < right:
                if arr[r] < pivot:
                    l += 1
                    arr[l], arr[r] = arr[r], arr[l]
                r += 1

            l += 1
            arr[l], arr[right] = arr[right], arr[l]
            return l
        pivot_idx = partition(left, right)
        self.quick_sort(arr, left, pivot_idx - 1)
        self.quick_sort(arr, pivot_idx + 1, right)


a = Solution().canPartition([2,2,1,1])
print(a)

# self.quick_sort(nums, 0, len(nums) - 1)
#         prefix_sum = []
#         sum_so_far = 0
#         for elem in nums:
#             sum_so_far += elem
#             prefix_sum.append(sum_so_far)
#
#         arr_sum = prefix_sum[-1]
#         bin_idx = self.binary_search(prefix_sum, arr_sum / 2)
#         return True if bin_idx > -1 else False