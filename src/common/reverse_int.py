class Solution1:
    def reverse(self, x: int) -> int:
        sign = [1, -1][x < 0]
        rev, x = 0, abs(x)
        while x:
            rem = x % 10
            x = x // 10
            rev = rev * 10 + rem
            if rev > 2**31 - 1:
                return 0
        return sign * rev


class Solution:
    def myAtoi(self, s: str) -> int:
        res = ""
        digit_started = False
        sign_encountered = False
        for ch in s:
            if not digit_started and not sign_encountered:
                if ch.isdigit():
                    sign_encountered = True
                    if ch != '0':
                        digit_started = True
                        res += ch
                elif ch == '+' or ch == '-':
                    res += ch
                    sign_encountered = True
                elif ch == ' ':
                    continue
                else:
                    return 0
            elif sign_encountered and not digit_started:
                if ch.isdigit():
                    if ch != '0':
                        digit_started = True
                        res += ch
                    elif not ch.isdigit():
                        return 0
            elif sign_encountered and digit_started:
                if ch.isdigit():
                    res += ch
                else:
                    break
        i = int(res)
        if i > 2**31 - 1:
            return 2**31 - 1
        elif i < -2**31:
            return 2**-31
        return i


a = Solution().myAtoi("0-1")
print(a)


# a = Solution1().reverse(-11123)
# print(a)