class Solution(object):
    """
    Method1: double for loops
    Time complexity: O(n^2), given that n is the integer "rowIndex"
    Space complexity: O(n^2)
    """
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ret_lst = []
        for i in range(rowIndex + 1):
            curr_lst = []
            for j in range(i+1):
                if j == 0 or j == i:
                    curr_lst.append(1)
                else:
                    curr_lst.append(ret_lst[i-1][j-1] + ret_lst[i-1][j])
            ret_lst.append(curr_lst)
        return ret_lst[rowIndex]