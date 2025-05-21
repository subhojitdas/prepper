from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def gen(open, close, curr_run):
            if open > n or close > n:
                return
            if open == n and close == n:
                res.append(curr_run)
                return
            if close > open:
                return
            gen(open + 1, close, curr_run + "(")
            gen(open, close + 1, curr_run + ")")

        gen(1, 0, "(")
        return res


a = Solution().generateParenthesis(3)
print(a)








