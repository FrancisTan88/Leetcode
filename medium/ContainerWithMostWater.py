from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max_cont = (right - left) * min(height[left], height[right])
        while left < right:
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            new_cont = (right - left) * min(height[left], height[right])
            max_cont = max(max_cont, new_cont)
        return max_cont