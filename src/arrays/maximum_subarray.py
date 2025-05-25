from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0
        max_sum_so_far = float('-inf')

        for num in nums:
            cur_sum += num
            max_sum_so_far = max(max_sum_so_far, cur_sum)
            if cur_sum <= 0:
                cur_sum = 0

        return max_sum_so_far


a = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(a)