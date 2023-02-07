
class Solution:
    '''
    time: O(n)
    space: O(n)
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        l = 0
        max_len = 0
        for r, char in enumerate(s):
            if (char in hashmap) and (hashmap[char] >= l) :
                l = hashmap[char] + 1
            else:
                max_len = max(max_len, r - l + 1)
            hashmap[char] = r
        return max_len
