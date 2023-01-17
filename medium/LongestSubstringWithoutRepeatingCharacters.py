
class Solution:
    '''
    time: O(n^2)
    space: O(n^2)
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        lst = []
        for i in range(len(s)):
            record = set()
            for j in range(i, len(s)):
                if s[j] not in record:
                    record.add(s[j])
                else:
                    lst.append(j-i)
                    break
                if j == len(s)-1:
                    lst.append(j-i+1)
        return max(lst)
    
    '''
    time: O(n)
    space: O(n)
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = {}
        l = 0
        max_len = 0
        for r, char in enumerate(s):
            if char not in hashmap:
                max_len = max(max_len, r-l+1)
            else:
                if hashmap[char] >= l:
                    l = hashmap[char] + 1
                else:
                    max_len = max(max_len, r-l+1)
            hashmap[char] = r
        return max_len
