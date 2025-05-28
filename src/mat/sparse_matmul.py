import collections
from typing import List


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:

        def to_sparse_matrix(mat):
            R = len(mat)
            C = len(mat[0])
            f = collections.defaultdict(lambda: collections.Counter())
            for i in range(R):
                for j in range(C):
                    if mat[i][j] != 0:
                        f[i][j] = mat[i][j]
            return f, R, C

        s1, R1, C1 = to_sparse_matrix(mat1)
        s2, R2, C2 = to_sparse_matrix(mat2)

        # R1, R2 = len(mat1), len(mat2)
        # C1, C2 = len(mat1[0]), len(mat2[0])
        ans = [[0] * C2 for _ in range(R1)]
        for i in range(R1):
            if i in s1:
                for j in range(C1):
                    if j in s1[i] and j in s2:
                        for k in range(C2):
                            if k in s2[j]:
                                ans[i][k] += s1[i][j] * s2[j][k]
        return ans


m1 = [[1,0,0],[-1,0,3]]
m2 = [[7,0,0],[0,0,0],[0,0,1]]
a = Solution().multiply(m1, m2)
print(a)