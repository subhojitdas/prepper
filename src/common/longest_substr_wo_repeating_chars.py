class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        max_len = start = 0
        for i, ch in enumerate(s):
            if ch in seen and seen[ch] >= start:
                start = seen[ch] + 1
            else:
                max_len = max(max_len, i - start + 1)

            seen[ch] = i
        return max_len

Solution().lengthOfLongestSubstring("abba")