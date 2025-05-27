from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        total = 0
        left = 0
        count = 0
        mx = max(nums)
        for right in range(N):
            if nums[right] == mx:
                count += 1
            while count >= k:
                if nums[left] == mx:
                    count -= 1
                left += 1
            total += left
        return total