from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        lookup = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        comb_arr = []
        for d in digits:
            comb_arr.append(lookup[d])

        N = len(digits)
        res = []
        if N == 0:
            return []

        def recurse(idx, current):
            if idx == N:
                res.append(''.join(current))
                return

            for c in lookup[digits[idx]]:
                current.append(c)
                recurse(idx + 1, current)
                current.pop()

        recurse(0, [])
        return res