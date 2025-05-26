from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf")] * len(nums)
        dp[len(nums) - 1] = 0

        def min_step(start, end):
            min_step = float("inf")
            for s_idx in range(start, min(end + 1, len(nums))):
                min_step = min(min_step, dp[s_idx])
            return min_step

        for idx in range(len(nums) - 2, -1, -1):
            idx_val = nums[idx]
            start, end = idx, idx + idx_val
            min_s = min_step(start, end)
            dp[idx] = min_s + 1

        return dp[0]


a = Solution().jump([2,3,0,1,4])
print(a)

