from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0:
            return []

        N = len(s)
        words_len = len(words[0])
        num_words = len(words)
        ss_size = num_words * words_len
        res = []

        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        # check if there are any match starting at index idx
        def check(idx):
            remaining = word_count.copy()
            matched = 0
            for j in range(idx, idx + ss_size, words_len):
                sub = s[j:j + words_len]
                if sub in remaining and remaining.get(sub, 0) > 0:
                    remaining[sub] -= 1
                    matched += 1
                else:
                    break
            return matched == num_words

        for i in range(0, N - ss_size + 1):
            is_matched = check(i)
            if is_matched:
                res.append(i)
        return res


a = Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"])
print(a)







