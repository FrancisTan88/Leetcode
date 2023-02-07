from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        """
        time: O(n^2), means we traverse all the elements
        space: O(1)
        """
        def transpose(row, col, length):
            new_row = col
            new_col = length - 1 - row
            return (new_row, new_col)
        start_col, end_col = 0, len(matrix)-1
        row = 0
        while start_col < end_col:
            for col in range(start_col, end_col):
                start_point = (row, col)
                nxt_point = transpose(row, col, len(matrix))
                curr_num = matrix[row][col]
                while nxt_point != start_point :
                    tmp = matrix[nxt_point[0]][nxt_point[1]]
                    matrix[nxt_point[0]][nxt_point[1]] = curr_num
                    curr_num = tmp
                    nxt_point = transpose(nxt_point[0], nxt_point[1], len(matrix))

                matrix[nxt_point[0]][nxt_point[1]] = curr_num
            start_col += 1
            end_col -= 1
            row += 1