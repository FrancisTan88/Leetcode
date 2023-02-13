from typing import List

class Solution:
    """
    time: O(M*N*(M+N)), given that func "fill_up" costs O(M+N) for each call,
                        and the matrix is full of zeroes in worst case(i.e. M*N zeroes)
    space: O(M*N), given that the matrix is full of zeroes in worst case(i.e. M*N zeroes)
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def fill_up(matrix, i, j):
            tmp = i
            while i >= 0:
                matrix[i][j] = 0
                i -= 1
            i = tmp
            while i < len(matrix):
                matrix[i][j] = 0
                i += 1
            i = tmp
            tmp = j
            while j < len(matrix[0]):
                matrix[i][j] = 0
                j += 1
            j = tmp
            while j >= 0:
                matrix[i][j] = 0
                j -= 1
            return matrix
        zero_pos = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zero_pos.append((i, j))
        for tup in zero_pos:
            matrix = fill_up(matrix, tup[0], tup[1])

    """
    time: O(M*N)
    space: O(1)
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        first_row, first_col = False, False
        for j in range(len(matrix[0])):
            if matrix[0][j] == 0:
                first_row = True
                break
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col = True
                break
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        if first_row:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
        if first_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0