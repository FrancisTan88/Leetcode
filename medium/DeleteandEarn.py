from typing import List
from collections import Counter
class Solution:
    """
    method: DP(best solution)
    time: O(max(max_number in nums, nums.length))
    space: O(max_number in nums)
    """
    def deleteAndEarn(self, nums: List[int]) -> int:
        dp = [0] * 10001
        for i in nums:
            dp[i] += i
        for i in range(2, len(dp)):
            dp[i] = max(dp[i]+dp[i-2], dp[i-1])
        return dp[-1]