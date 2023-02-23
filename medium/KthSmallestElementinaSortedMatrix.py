from heapq import heappop, heappush, heapify
from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minheap = [] 
        for i in range(len(matrix)):
            heappush(minheap, (matrix[i][0], i, 0))
        
        for i in range(k):
            ans, r, c = heappop(minheap)
            if c < len(matrix)-1:
                heappush(minheap, (matrix[r][c+1], r, c+1))
        return ans