from typing import List

class Solution:
    # Method1: sort it first, then compare them
    # time: O(nlogn) -> the cost of built-in function sorted() 
    # space: O(1) 
    def singleNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)
        ind = 0
        while nums:
            if ind == len(nums)-1:
                return nums[ind]
            if nums[ind] != nums[ind+1]:
                return nums[ind]
            ind += 2
    
    # Method2: XOR
    # time: O(n)
    # space: O(1)
    def singleNumber(self, nums: List[int]) -> int:
        tmp = 0
        for i in nums:
            tmp ^= i
        return tmp

