from typing import List


class Solution:
    """
    time: O(n^2), where n is the length of given array
    space: O(1)
    """
    def canJump(self, nums: List[int]) -> bool:
        idx = 0
        last = len(nums) - 1
        while idx < last:
            if idx + nums[idx] >= last:
                return True
            if nums[idx] == 0:
                return False
            maximum = -1
            for i in range(idx+1, idx + nums[idx] + 1):
                if i + nums[i] > maximum:
                    idx = i
                    maximum = i + nums[i]
        return True
