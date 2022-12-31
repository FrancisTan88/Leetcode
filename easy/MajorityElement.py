from typing import List

class Solution:
    """
    time: O(n)
    space: O(n)
    """
    def majorityElement(self, nums: List[int]) -> int:
        standard = len(nums)/2
        hashmap = {}
        for i in nums:
            i = str(i)
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
            if hashmap[i] > standard: return int(i)

    """
    time: O(nlogn)
    space: O(1)
    """
    def majorityElement(self, nums: List[int]) -> int:
        position = len(nums)//2
        nums = sorted(nums)
        return nums[position]

    """
    time: O(n)
    space: O(1)
    """
    def majorityElement(self, nums: List[int]) -> int:
        majority = 0
        count = 0
        for idx, num in enumerate(nums):
            if count == 0:
                majority = num
            if num == majority:
                count += 1
            else:
                count -= 1
        return majority