from typing import List

class Solution:
    """
    method: DP
    time: O(n)
    space: O(n)
    """
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]

        dp = [nums[0], max(nums[1], nums[0])]
        for i in range(2, len(nums)):
            dp.append(max(nums[i] + dp[i-2], dp[i-1]))
        return dp[-1]