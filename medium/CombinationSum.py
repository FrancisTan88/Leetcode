from typing import List

class Solution:
    '''
    time: pending...
    space: pending...
    '''
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, sub_arr, ans, summation, idx):
            if summation > target:
                return ans
            if summation == target:
                ans.append(sub_arr)
                return ans
            for i in range(idx, len(candidates)):
                ans = dfs(candidates, target, sub_arr+[candidates[i]], ans, summation+candidates[i], i)
            return ans

        return dfs(candidates, target, [], [], 0, 0)