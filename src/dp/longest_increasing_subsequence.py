import bisect
from typing import List


class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            max_len = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    max_len = max(max_len, 1 + LIS[j])
            LIS[i] = max_len

        return max(LIS)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        INF = 10 ** 20

        # longest[t] = the longest increasing subsequence of length t that ends with this number
        longest = [-INF]

        for x in nums:
            index = bisect.bisect_left(longest, x)

            if index >= len(longest):
                longest.append(x)
            else:
                longest[index] = x

        return len(longest) - 1




a = Solution().lengthOfLIS([10,9,2,5,3,7,101,6])
print(a)