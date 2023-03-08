from typing import List

class Solution:
    """
    method: prefix & suffix (two-pass)
    time: O(2n) = O(n)
    space: O(1), note that the array used to store the answer is not counted as extra space in this problem.
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        n = len(nums)
        for i in range(1, n):
            prefix.append(prefix[i-1] * nums[i-1])
        suffix = 1
        for i in range(n-1, -1, -1):
            prefix[i] *= suffix
            suffix *= nums[i]
        return prefix
    
    """
    method: prefix & suffix (one-pass, best solution)
    time: O(n)
    space: O(1), note that the array used to store the answer is not counted as extra space in this problem.
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        prefix, suffix = 1, 1
        forward, backward = 0, len(nums)-1
        while forward < len(nums):
            ans[forward] *= prefix
            prefix *= nums[forward]
            ans[backward] *= suffix
            suffix *= nums[backward]
            forward += 1
            backward -= 1
        return ans