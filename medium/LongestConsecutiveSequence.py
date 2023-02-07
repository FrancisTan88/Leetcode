from typing import List

class Solution:
    """
    time: O(nlogn)
    space: O(1)
    """
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        nums.sort() # this line costs O(nlogn)
        max_len = 1
        curr_len = 1
        prev_num = nums[0]
        for i in range(1, len(nums)):
            if abs(nums[i] - prev_num) > 1:
                curr_len = 1
            elif nums[i] - prev_num == 1:
                curr_len += 1
            prev_num = nums[i]
            max_len = max(max_len, curr_len)
        return max_len 

    """
    time: O(n)
    space: O(n)
    """    
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        s = set()
        for i in nums:
            s.add(i)
        max_len = 1
        curr_len = 1
        for j in nums:
            if j-1 not in s:
                curr_len = 1
                prev_num = j
                while prev_num+1 in s:
                    curr_len += 1
                    prev_num += 1
            max_len = max(max_len, curr_len)
        return max_len