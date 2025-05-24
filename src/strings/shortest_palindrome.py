class Solution1: # O(n^2)
    def shortestPalindrome(self, s: str) -> str:

        def is_palindrome(s, l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        for r in reversed(range(len(s))):
            if is_palindrome(s, 0, r):
                suffix = s[r+1:]
                return suffix[::-1] + s
        return ""


class Solution: # O(n)

    def shortestPalindrome(self, s: str) -> str:
        prefix = 0
        suffix = 0
        base = 29
        power = 1
        mod = 10 ** 9 + 7
        last_index = 0

        for i, c in enumerate(s):
            char = (ord(c) - ord('a') + 1)

            prefix = (prefix * base) % mod
            prefix = (prefix + char) % mod
            suffix = (suffix + char * power) % mod
            power = (power * base) % mod

            if prefix == suffix:
                last_index = i

        suffix = s[last_index + 1:]
        return suffix[::-1] + s


a = Solution().shortestPalindrome("aacecaaa")
print(a)
