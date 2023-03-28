from typing import List
class Solution:
    """
    method: divide and conquer
    time: O(logn)
    space: O(logn), which is the cost of recursive stack
    """
    def findPeakElement(self, nums: List[int]) -> int:
        def divide(nums, l, r):
            if l >= r:
                return nums[l], l
            mid = (l + r) // 2
            value_l, idx_l = divide(nums, l, mid)
            value_r, idx_r = divide(nums, mid+1, r)
            if value_l > value_r:
                return value_l, idx_l
            else:
                return value_r, idx_r
        largest, idx = divide(nums, 0, len(nums)-1)
        return idx
    
    """
    method: iterative binary search(best solution)
    time: O(logn)
    space: O(1)
    """
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        while l < r:
            mid = (l+r) // 2
            if nums[mid] < nums[mid+1]:
                l = mid+1
            else:
                r = mid
        return l