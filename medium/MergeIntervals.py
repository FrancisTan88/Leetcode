from typing import List

class Solution:
    """
    time: O(nlogn), which is the cost of sorting 
    space: O(n), which is the cost of the array "ans", or the implicit cost of sorting function
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
       
        
        intervals.sort(key=lambda x: x[0])  # theta(nlogn)
        ans = []
        idx = 0
        n = len(intervals)
        # theta(n)
        while idx < n:
            if not ans or ans[-1][1] < intervals[idx][0]:
                ans.append(intervals[idx])
            else:
                ans[-1][1] = max(ans[-1][1], intervals[idx][1])
            idx += 1
        return ans