from typing import List
class Solution:
    """
    method: shift the n-k elements
    time: max(O(n-k), O(k)) = O(n)
    sapce: O(k) = O(n)
    """
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        rotate = nums[n-k:]
        for i in range(n-1,k-1,-1):
            nums[i] = nums[i-k]
        for i in range(k):
            nums[i] = rotate[i]

    """
    method: reverse the array
    time: O(n)
    sapce: O(1)
    """
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end]= nums[end], nums[start]
                start += 1
                end -= 1
            return nums
        n = len(nums)
        k %= n
        nums = reverse(nums, 0, n-1)
        nums = reverse(nums, 0, k-1)
        nums = reverse(nums, k, n-1)

