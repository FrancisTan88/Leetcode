from typing import List
class Solution:
    """
    method: two pointers(best solution)
    time: O(n)
    space: O(1)
    """
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = 2**31
        second = 2**31
        for i in nums:
            if i <= first:
                first = i
            elif i <= second:
                second = i
            else:
                return True
        return False