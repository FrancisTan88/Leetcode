from collections import defaultdict
from typing import Optional, List


class Solution:
    """
    (best solution)
    time: O(N*K), where N, K are the length of the "strs", the longest string in the "strs", respectively.
    space: O(N*K)
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord("a")] += 1
            group[tuple(counter)].append(s)
        return group.values()
