from typing import List

class Solution:
    """
    backtracking
    time: 
    space:
    """
    def canJump(self, nums: List[int]) -> bool:
        def backtracking(nums, curr_pos):
            if nums[curr_pos] >= len(nums)-1-curr_pos:
                return True
            for i in range(nums[curr_pos]):
                if backtracking(nums, curr_pos+i+1):
                    return True
            return False
        return backtracking(nums, 0)