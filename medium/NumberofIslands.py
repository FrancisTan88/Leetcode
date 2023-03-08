from typing import List

class Solution:
    """
    method: DFS(best)
    time: O(m*n), given that m, n are the number of rows and columns, respectively
                    Note:the func dfs() has to traverse all cells in the matrix in the worst case, which costs O(m*n),
                            but in return, it only costs O(1)'s for other starting point.
                                So, it costs O(m*n) in total.
    space: O(m*n), given that func dfs() has to traverse all cells in the matrix in the worst case,
                    and the recursive stack would store m*n elements in that case.
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or grid[i][j] != "1":
                return grid
            grid[i][j] = "#"
            grid = dfs(grid, i-1, j)
            grid = dfs(grid, i+1, j)
            grid = dfs(grid, i, j+1)
            grid = dfs(grid, i, j-1)
            return grid
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    grid = dfs(grid, i, j)
                    count += 1
        return count