from typing import List


class Solution:
    def specialGrid(self, n: int) -> List[List[int]]:
        def fill(x):
            if x == 0:
                return [[0]]

            pgrid = fill(x - 1)

            D = (1 << x)
            D2 = (1 << (x - 1))

            r = [[None] * D for _ in range(D)]
            # upper right
            for i in range(D2):
                for j in range(D2):
                    r[i][j + D2] = pgrid[i][j]

            # lower right
            offset = D2 * D2
            for i in range(D2):
                for j in range(D2):
                    r[i + D2][j + D2] = pgrid[i][j] + offset

            # lower left
            offset = D2 * D2 * 2
            for i in range(D2):
                for j in range(D2):
                    r[i + D2][j] = pgrid[i][j] + offset

            # upper left
            offset = D2 * D2 * 3
            for i in range(D2):
                for j in range(D2):
                    r[i][j] = pgrid[i][j] + offset
            return r

        return fill(n)


a = Solution().specialGrid(3)
for row in a:
    print('  '.join(str(elem) for elem in row))