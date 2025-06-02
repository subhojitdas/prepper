class Solution:
    def countAndSay(self, n: int) -> str:

        def say(n):
            if n == 1:
                return '1'

            prev = say(n - 1)
            res = ''
            N = len(prev)
            idx = 0
            while idx < N:

                right = idx + 1
                while right < N:
                    if prev[idx] != prev[right]:
                        break
                    right +=1
                count = right - idx
                digit = prev[idx]
                res += str(count) + str(digit)
                idx = right
            return res

        return say(n)

