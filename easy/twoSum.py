from typing import List

class Solution:
    """
    Advanced method:
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for idx, num in enumerate(nums):
            if str(num) not in hashmap:
                hashmap[str(num)] = idx
            if str(target-num) in hashmap and \
                hashmap[str(target-num)] != idx:
                return [idx, hashmap[str(target-num)]]
                    