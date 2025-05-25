from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first_elem = nums[0]
        last_elem = nums[-1]

        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= first_elem:
                if target <= nums[mid] and target >= first_elem:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] <= first_elem:
                if target >= nums[mid] and target <= last_elem:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


a = Solution().search([1, 3], 3)
print(a)
