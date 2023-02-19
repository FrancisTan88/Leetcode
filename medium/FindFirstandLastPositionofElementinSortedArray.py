from typing import List
class Solution:
    '''
    time: O(n), in the worst case, the starting position of "mid" is equal to target,
                 and it's also the only element that equal to target, 
                 i.e. those two while loops have to traverse the half of the array, respectively
    space: O(1)
    '''
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        def binary_search(nums, target):
            l = 0
            r = len(nums) - 1
            mid = (l+r) // 2
            while l < r:
                mid = (l+r) // 2
                if nums[mid] == target:
                    return mid, l, r
                elif target < nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            return mid, l, r
        mid, l, r = binary_search(nums, target)
        if l == r and nums[l] != target:
                return [-1, -1]
        while l < len(nums) and nums[l] != target:
            l += 1
        while r >= 0 and nums[r] != target:
            r -= 1
        return [l, r]