from typing import List


class Solution:
    def minSwaps(self, src: List[int]) -> int:
        N = len(src)

        def dsum(x):
            ans = 0
            while x:
                ans += x % 10
                x //= 10
            return ans

        target = src[:]
        target.sort(key=lambda x: (dsum(x), x))
        lookup = {}

        for idx, elem in enumerate(src):
            lookup[elem] = idx
        print("Target: ", target)

        swap = 0

        for idx, x in enumerate(target):
            required_idx = lookup[x]
            if required_idx != idx:
                swap += 1
                src[required_idx], src[idx] = src[idx], src[required_idx]
                lookup[x] = idx
                lookup[src[required_idx]] = required_idx

        print("Source: ", src)
        return swap


arr = [978678783,989995084,465932830,37255967]
a = Solution().minSwaps(arr)
print(a)

