from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            max_len = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    max_len = max(max_len, 1 + LIS[j])
            LIS[i] = max_len

        return max(LIS)


a = Solution().lengthOfLIS([10,9,2,5,3,7,101,18])
print(a)