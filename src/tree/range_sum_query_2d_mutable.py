from typing import List

LSB = lambda idx: idx & (-idx)

class BinaryIndexTreeTwo:

    def __init__(self, mat):
        self.R = len(mat)
        self.C = len(mat[0])

        self.stree = [[0] * (self.C + 1) for _ in range(self.R + 1)]

        for i in range(self.R):
            for j in range(self.C):
                self.increase(i + 1, j + 1, mat[i][j])

    def increase(self, row, col, val):
        r = row
        while r <= self.R:
            c = col
            while c <= self.C:
                self.stree[r][c] += val
                c += LSB(c)
            r += LSB(r)

    def query(self, row, col):
        s = 0
        while row > 0:
            c = col
            while c > 0:
                s += self.stree[row][c]
                c -= LSB(c)
            row -= LSB(row)
        return s


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        self.bit = BinaryIndexTreeTwo(matrix)
        self.pretty_print_matrix(matrix)
        print(); print(); print(); print()
        self.pretty_print_matrix(self.bit.stree)

    def update(self, row: int, col: int, val: int) -> None:
        delta = val - self.mat[row][col]
        self.bit.increase(row + 1, col + 1, delta)
        self.mat[row][col] = val

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        add1 = lambda x: x + 1
        row2, col2, row1, col1 = add1(row2), add1(col2), add1(row1), add1(col1)

        return self.bit.query(row2, col2) + self.bit.query(row1 - 1, col1 - 1) - self.bit.query(row1 - 1, col2) - self.bit.query(row2, col1 - 1)

    def pretty_print_matrix(self, mat):
        for row in mat:
            print('  '.join(str(r) for r in row))


mat = [[1]]
obj = NumMatrix(mat)
a = obj.sumRegion(0, 0, 0, 0)
obj.update(0,0,-1)
print(a)
b = obj.sumRegion(0, 0, 0, 0)
print(b)