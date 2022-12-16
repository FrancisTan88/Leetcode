class Solution:
    # clever method: using hash map

    # because it is guaranteed that the string is largest to small from left to right, so if there were exceptions, 
    # the cases must be (1,5), (10, 40), etc.
    # so if that way, just deduct the current number and we will get the right answer
    def romanToInt(self, s: str) -> int:
        map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        sum = 0
        for i in range(len(s)):
            if i+1 <= len(s)-1 and map[s[i+1]] > map[s[i]]:  
                sum -= map[s[i]]
            else:
                sum += map[s[i]]
        return sum
                