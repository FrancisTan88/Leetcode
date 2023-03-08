from typing import List

class Solution:
    """
    method: DFS(best)
    time: O(m*n), given that m, n are the number of rows and columns, respectively
    space: O(m*n), given that func dfs() has to traverse all cells in the matrix in the worst case,
                    and the recursive stack would store m*n elements in that case.
    """
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(board, i, j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) \
                or board[i][j] != "O":
                return board
            board[i][j] = "#"
            board = dfs(board, i-1, j)
            board = dfs(board, i, j+1)
            board = dfs(board, i+1, j)
            board = dfs(board, i, j-1)
            return board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or i == len(board)-1 or \
                    j == 0 or j == len(board[0])-1:
                    board = dfs(board, i, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
        return board