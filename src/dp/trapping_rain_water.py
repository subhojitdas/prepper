from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) - 1
        maxL, maxR = 0, 0
        while left <= right:
            if maxL <= maxR:
                water_stored = maxL - height[left]
                if water_stored > 0:
                    res += water_stored
                maxL = max(maxL, height[left])
                left += 1
            else:
                water_stored = maxR - height[right]
                if water_stored > 0:
                    res += water_stored
                maxR = max(maxR, height[right])
                right -= 1
        return res

a = Solution().trap([4,2,0,3,2,5])
print(a)


