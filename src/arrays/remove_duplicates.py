from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        slow = 0
        fast = 1
        dist_count = 1
        while fast < len(nums):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow], nums[fast] = nums[fast], nums[slow]
                dist_count += 1
            fast += 1
        return dist_count


arr = [1, 1, 2, 3, 3]
a = Solution().removeDuplicates(arr)
print(arr)
print(a)

