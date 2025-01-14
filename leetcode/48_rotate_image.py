# https://leetcode.com/problems/rotate-image/


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)

        for i in range(n):
            for j in range(i + 1, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for line in matrix:
            l = 0
            r = n - 1
            while l < r:
                temp = line[l]
                line[l] = line[r]
                line[r] = temp
                l += 1
                r -= 1

    def rotate(self, matrix: list[list[int]]) -> None:
        matrix.reverse()

        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
