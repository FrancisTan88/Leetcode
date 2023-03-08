from typing import List

class Solution:
    """
    method: two pointers
    time: O(n)
    space: O(1) 
    """
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]

        curr_max, curr_min, ans = nums[0], nums[0], nums[0]
        for i in range(1, n):
            if nums[i] < 0:
                curr_max, curr_min = curr_min, curr_max
            curr_max = max(nums[i], curr_max * nums[i])
            curr_min = min(nums[i], curr_min * nums[i])
            ans = max(ans, curr_max)
        return ans