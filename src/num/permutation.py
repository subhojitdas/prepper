from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def backtrack(start):
            if start == len(nums):
                ans.append(nums.copy())
                return

            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start+1)
                nums[start], nums[i] = nums[i], nums[start]

        ans = []
        backtrack(0)
        return ans


a = Solution().permute([1,2,3])
print(a)

