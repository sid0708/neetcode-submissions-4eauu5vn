class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # transpose and inverse rows
        n =len(matrix)
        # transpose
        for r in range(n):
            for c in range(r+1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        # reverse
        for row in matrix:
            row.reverse()
        