from typing import List

class Solution:
    """
    Method: Binary search (iteration)
    Time complexity: O(log n)
    Space complexity: O(1)
    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left < right:
            middle = (right+left) // 2
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                right = middle
            else:
                left = middle + 1
        return len(nums) if target > nums[-1] else left

    """
    Method: Binary search (recursive)
    Time complexity: O(logn)
    Space complexity: O(logn)
    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binary_search(nums, target, left, right):
            if left >= right:
                return left
            middle = (left + right) // 2
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                return binary_search(nums, target, left, middle)
            else:
                return binary_search(nums, target, middle+1, right)
        return len(nums) if target > nums[-1] \
            else binary_search(nums, target, 0, len(nums)-1)


       


