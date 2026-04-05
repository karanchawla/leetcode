class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.P = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.P[i][j] = (
                    matrix[i - 1][j - 1]
                    + self.P[i - 1][j]
                    + self.P[i][j - 1]
                    - self.P[i - 1][j - 1]
                )

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return (
            self.P[r2 + 1][c2 + 1]
            - self.P[r1][c2 + 1]
            - self.P[r2 + 1][c1]
            + self.P[r1][c1]
        )
