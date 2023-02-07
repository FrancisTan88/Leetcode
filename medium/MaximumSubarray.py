from typing import List

class Solution:
    """
    time: O(n)
    space: O(1)
    """
    def maxSubArray(self, nums: List[int]) -> int:
        tmp_sum = 0
        maximum = -10001
        for num in nums:
            tmp_sum += num
            maximum = max(maximum, tmp_sum)
            if tmp_sum < 0:
                tmp_sum = 0
        return maximum