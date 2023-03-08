from collections import Counter, defaultdict
class Solution:
    """
    method: sliding window(best solution)
    time: O(26*n) = O(n), given that the number of alphabet is 26, and the n is the length of "s"
    space: O(n), which is the cost of hashmap used to count frequency of characters
    """
    def longestSubstring(self, s: str, k: int) -> int:
        counter_all = Counter(s)
        max_len = 0
        n = len(s)
        for nums_char in range(1, len(counter_all)+1):
            left = 0
            counter_curr = defaultdict(int)
            for right in range(n):
                counter_curr[s[right]] += 1
                while len(counter_curr) > nums_char:
                    counter_curr[s[left]] -= 1
                    if counter_curr[s[left]] == 0:
                        counter_curr.pop(s[left])
                    left += 1
                if all([v >= k for key, v in counter_curr.items()]):
                    max_len = max(max_len, right-left+1)
        return max_len