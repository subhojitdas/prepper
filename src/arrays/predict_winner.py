from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        N = len(nums)
        cache = {}
        # Minimax -- Game theory --- TODO: need to read in details
        def score(left, right):
            if left > right:
                return 0

            if (left, right) in cache:
                return cache[(left, right)]

            score_taking_from_left = nums[left] - score(left + 1, right)
            score_taking_from_right = nums[right] - score(left, right - 1)

            cache[(left, right)] = max(score_taking_from_left, score_taking_from_right)
            return cache[(left, right)]

        return score(0, N - 1) >= 0
