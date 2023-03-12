from typing import List
class Solution:
    """
    time: O(n^2), given that for every "base number" that <= 0, we scan all the number on its right side.
    space: O(n), which is the cost of the set.
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums = sorted(nums)
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            target = -1 * nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    ans.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        ans = list(map(list, ans))
        return ans