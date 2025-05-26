from typing import List


class Solution:

    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[len(nums) - 1] = True

        def any_path(start, end):
            for i in range(start, end + 1):
                if dp[i]:
                    return True
            return False

        for idx in range(len(nums) - 2, -1, -1):
            idx_val = nums[idx]
            start, end = idx, idx + idx_val
            dp[idx] = any_path(start, end)

        return dp[0]



