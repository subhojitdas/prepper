class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}

        for ch in t:
            countT[ch] = countT.get(ch, 0) + 1

        have, need = 0, len(countT)
        res, res_len = [-1, -1], float('inf')
        l = 0

        for r, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1

            if ch in countT and window[ch] == countT[ch]:
                have += 1

            while need == have:
                if r - l + 1 < res_len:
                    res_len = r - l + 1
                    res = [l, r]
                curr_ch = s[l]
                window[curr_ch] -= 1
                if curr_ch in countT and window[curr_ch] < countT[curr_ch]:
                    have -= 1
                l += 1

        return s[res[0]:res[1] + 1] if res_len != float('inf') else ""




a = Solution().minWindow("ADOBECODEBANC", "ABC")
print(a)

