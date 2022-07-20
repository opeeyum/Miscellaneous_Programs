def maximalSquare(mat) -> int:
    row = len(mat)
    col = len(mat[0])

    def Ar(r, c):
        if r < row and c < col:
            if mat[r][c] == 1:
                return 1 + min(Ar(r, c + 1), Ar(r + 1, c + 1), Ar(r + 1, c))
        return 0

    max_area = 0

    for i in range(row):
        for j in range(col):
            if mat[i][j] == 1:
                temp = Ar(i, j)
                max_area = max(max_area, temp)

    return max_area**2


mat = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
print(mat)
