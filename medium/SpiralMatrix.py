from typing import Optional, List

class Solution:
    """
    method: use four pointers and just do spiral traverse
    time: O(m*n), means that we traverse all elements in the matrix
    space: O(m*n)
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        start_row, end_row = 0, len(matrix)-1
        start_col, end_col = 0, len(matrix[0])-1
        ans = []
        while start_row <= end_row and start_col <= end_col:
            for i in range(start_col, end_col+1):
                ans.append(matrix[start_row][i])
            start_row += 1
        
            for i in range(start_row, end_row+1):
                ans.append(matrix[i][end_col])
            end_col -= 1
            
            if start_row <= end_row:
                for i in range(end_col, start_col-1, -1):
                    ans.append(matrix[end_row][i])
                end_row -= 1
                
            if start_col <= end_col:
                for i in range(end_row, start_row-1, -1):
                    ans.append(matrix[i][start_col])
                start_col += 1
        return ans
    

    """
    method: pop and rotate
    time: O(m*n), but the total time is definitely larger than the above
    space: O(m*n)
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        while matrix:
            ans += matrix.pop(0)
            if matrix:
                matrix = list(zip(*matrix))[::-1]
        return ans 