from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        count = 0
        for x in nums:
            while len(stack) > 0:
                if x > stack[-1]:
                    stack.append(x)
                    count += 1
                    break
                elif x == stack[-1]:
                    break
                else:
                    stack.pop()
        return count

