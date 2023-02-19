from typing import List

class Solution:
    """
    time: O(n * 2^n)
    space: O(n)
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, curr, ans, idx):
            ans.append(curr)
            for i in range(idx, len(nums)):
                ans = dfs(nums, curr + [nums[i]], ans, i+1)
            return ans
        return dfs(nums, [], [], 0)