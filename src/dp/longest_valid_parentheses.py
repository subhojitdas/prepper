from typing import List


class Solution1:
    def longestValidParentheses(self, s: str) -> int:
        left, right, max_len = 0, 0, 0

        for ch in s:
            if ch == '(':
                left += 1
            if ch == ')':
                right += 1

            if left == right:
                max_len = max(max_len, 2*left)
            if right > left:
                left, right = 0, 0

        left, right = 0, 0
        for ch in reversed(s):
            if ch == '(':
                left += 1
            if ch == ')':
                right += 1
            if left == right:
                max_len = max(max_len, 2*left)
            if left > right:
                left, right = 0, 0

        return max_len








a = Solution1().longestValidParentheses("(()")
print(a)
