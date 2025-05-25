from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_store = 0
        while l < r:
            min_hei = min(height[l], height[r])
            curr_store = (r - l) * min_hei
            if max_store < curr_store:
                max_store = curr_store
            if min_hei == height[l]:
                l += 1
            else:
                r -= 1
        return max_store


a = Solution().maxArea([1,8,6,2,5,4,8,3,7])
print(a)