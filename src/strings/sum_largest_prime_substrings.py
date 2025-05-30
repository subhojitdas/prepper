class Solution:
    def sumOfLargestPrimes(self, s: str) -> int:
        N = len(s)

        def is_prime(x):
            if x <= 1:
                return False
            t = 2
            while t*t <= x:
                if x % t == 0:
                    return False
                t += 1
            return True
        prime_store = set()
        for i in range(N):
            for j in range(i+1, N + 1):
                sub = int(s[i:j])
                if is_prime(sub):
                    prime_store.add(sub)
        r = sorted(set(prime_store), reverse=True)
        return sum(r[:3])


a = Solution().sumOfLargestPrimes("73")
print(a)