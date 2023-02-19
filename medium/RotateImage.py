from typing import List

class Solution:
    """
    time: O(n^2), means we traverse all the elements
    space: O(1)
    """
    def rotate_by_90(self, matrix: List[List[int]]):
        """
        Do not return anything, modify matrix in-place instead.
        """
        def transpose(i, j, n):
            new_r = j
            new_c = n - 1 - i
            return new_r, new_c
        def modify(i, j, matrix, n):
            start_r, start_c = i, j
            curr = matrix[i][j]
            nxt_r, nxt_c = transpose(i, j, n)    
            nxt = matrix[nxt_r][nxt_c]
            while nxt_r != start_r or nxt_c != start_c:
                matrix[nxt_r][nxt_c] = curr
                curr = nxt
                nxt_r, nxt_c = transpose(nxt_r, nxt_c, n)
                nxt = matrix[nxt_r][nxt_c]
            matrix[nxt_r][nxt_c] = curr    
            return matrix
        n = len(matrix)
        start_col, end_col = 0, n - 1
        row = 0
        while start_col < end_col:
            for i in range(start_col, end_col):
                matrix = modify(row, i, matrix, n)
            row += 1
            start_col += 1
            end_col -= 1
        return matrix
    
    """
    time: O(n^2), means we traverse all the elements
    space: O(1)
    """
    def rotate_by_180(self, matrix: List[List[int]]):
        mid = (len(matrix[0]) - 1) // 2
        # swap columns
        for i in range(len(matrix)):
            for j in range(mid + 1):
                matrix[i][j], matrix[i][-1*(j+1)]= matrix[i][-1*(j+1)], matrix[i][j]
        # swap rows
        for i in range(mid + 1):
            matrix[i], matrix[-1*(i+1)]= matrix[-1*(i+1)], matrix[i]
        return matrix

    """
    time: O(n^2), means we traverse all the elements
    space: O(1)
    """
    def rotate_by_270(self, matrix: List[List[int]]):
        # transpose
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i]= matrix[j][i], matrix[i][j]
        # swap rows
        mid = len(matrix) // 2
        for i in range(mid):
            matrix[i], matrix[-1*(i+1)]= matrix[-1*(i+1)], matrix[i]
        return matrix


obj = Solution()
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(obj.rotate_by_90(matrix))
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(obj.rotate_by_180(matrix))
matrix = [[1,2,3], [4,5,6], [7,8,9]]
print(obj.rotate_by_270(matrix))