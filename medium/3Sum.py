from typing import List
class Solution:
    """
    time: O(n^3), pay attention to the "if candidate not in ans:"
    space: O(n^2)
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums = sorted(nums)
        for i in range(len(nums)-2):
            base = nums[i]
            if base > 0: break
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[left] + nums[right] < -1*base:
                   left += 1
                elif nums[left] + nums[right] > -1*base:
                     right -= 1
                else:
                    candidate = [base, nums[left], nums[right]]
                    if candidate not in ans:
                        ans.append(candidate)
                    left += 1
        return ans