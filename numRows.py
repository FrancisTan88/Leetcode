from typing import List
"""
Time complexity: O(n^2)
Space complexity: O(n^2)
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret_lst = []
        for j in range(numRows):
            lst = []
            for i in range(j+1):
                if i == 0 or i == j:
                    lst.append(1)
                else:
                    lst.append(ret_lst[j-1][i-1] + ret_lst[j-1][i])
            ret_lst.append(lst)
        return ret_lst