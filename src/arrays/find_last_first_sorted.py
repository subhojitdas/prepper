from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]

        idx = self.binary_search(nums, target)
        if idx == -1:
            return [-1, -1]
        left, right = idx, idx
        while left >= 0 and nums[left] == target:
            left -= 1
        while right < len(nums) and nums[right] == target:
            right += 1

        return [left+1, right-1]

    def binary_search(self, arr, target):
        start = 0
        end = len(arr) - 1

        while start <= end:
            mid = (start + end) // 2
            if arr[mid] == target:
                return mid
            elif target > arr[mid]:
                start = mid + 1
            else:
                end = mid - 1
        return -1


a = Solution().searchRange([1], 1)
print(a)