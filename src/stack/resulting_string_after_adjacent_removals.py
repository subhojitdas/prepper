class Solution:
    def resultingString(self, s: str) -> str:
        stack = []

        def good_to_remove(ch1, ch2):
            if abs(ord(ch1) - ord(ch2)) == 1:
                return True
            elif ch1 + ch2 == "az" or ch1 + ch2 == "za":
                return True
            else:
                return False

        for ch in s:
            stack.append(ch)
            while len(stack) >= 2 and good_to_remove(stack[-2], stack[-1]):
                stack.pop()
                stack.pop()
        return "".join(stack)

# a = Solution().resultingString("adcb")
# print(a)