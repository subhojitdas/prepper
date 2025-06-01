    class Solution:
        def myAtoi(self, s: str) -> int:
            s = s.lstrip()
            negative = 1

            if s.startswith('-'):
                negative = -1
                s = s[1:]
            elif s.startswith('+'):
                s = s[1:]

            N = len(s)
            current = 0
            for i in range(N):
                if not s[i].isdigit():
                    break
                current = current * 10 + int(s[i])

            current *= negative
            current = min(current, 2**31 - 1)
            current = max(current, -2**31)
            return current






a = Solution().myAtoi("+1")
print(a)



# res = ""
#         if not s:
#             return 0
#         ch = s[0]
#         idx = 0
#         while ch == " ":
#             idx += 1
#             ch = s[idx]
#         if idx == len(s):
#             return 0
#         if s[idx] != '-' and s[idx] != '+' and not s[idx].isdigit():
#             return 0
#         if s[idx] == '+' or s[idx] == '-':
#             res += s[idx]
#             idx = idx + 1
#
#         if idx == len(s):
#             return 0
#
#         while s[idx] == '0':
#             idx += 1
#
#         if s[idx].isalpha():
#             return 0
#
#         while idx < len(s) and s[idx].isdigit():
#             res += s[idx]
#             idx += 1
#
#         i = int(res)
#         if i > 2**31 - 1:
#             return 2**31 - 1
#         elif i < -2**31:
#             return 2**-31
#         return i