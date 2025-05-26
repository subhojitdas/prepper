from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for idx, val in enumerate(heights):
            last_idx = idx
            while stack and stack[-1][1] > val:
                last_val = stack.pop()
                area = (idx - last_val[0]) * last_val[1]
                max_area = max(max_area, area)
                last_idx = last_val[0]
            stack.append((last_idx, val))

        H = len(heights)
        while stack:
            last_val = stack.pop()
            area = (H - last_val[0]) * last_val[1]
            max_area = max(max_area, area)

        return max_area


a = Solution().largestRectangleArea([2,1,5,6,2,3])
print(a)
