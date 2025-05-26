class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)

        if s_len == 0 and p_len == 0:
            return True
        if s_len > 0 and p_len == 0:
            return False

        new_p = p[0]
        for idx in range(1, p_len):
            if p[idx] == "*" and p[idx - 1] == "*":
                continue
            else:
                new_p += p[idx]
        p_len = len(new_p)
        p = new_p

        dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]
        dp[0][0] = True

        if p_len > 0 and p[0] == "*":
            dp[0][1] = True
        for s_idx in range(1, s_len + 1):
            for p_idx in range(1, p_len + 1):
                if s[s_idx-1] == p[p_idx-1] or p[p_idx-1] == '?':
                    dp[s_idx][p_idx] = dp[s_idx-1][p_idx-1]
                elif p[p_idx-1] == '*':
                    dp[s_idx][p_idx] = dp[s_idx-1][p_idx] or dp[s_idx][p_idx-1]

        return dp[s_len][p_len]



a = Solution().isMatch("aaab", "b**")
print(a)
