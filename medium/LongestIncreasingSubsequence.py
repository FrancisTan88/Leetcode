from typing import List
class Solution:
    """
    method: dp
    time: O(n^2), given that for every element in "nums", we find LIS by check DP backward.
    space: O(n), which is the cost of DP table.
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        total_maxlen = 1
        for i in range(n):
            curr_maxlen = dp[i]
            for j in range(i, -1, -1):
                if nums[i] > nums[j]:
                    curr_maxlen = max(curr_maxlen, dp[j]+1)
            dp[i] = curr_maxlen
            total_maxlen = max(total_maxlen, dp[i])
        return total_maxlen