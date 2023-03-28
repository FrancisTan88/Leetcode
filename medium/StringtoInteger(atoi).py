class Solution:
    """
    time: O(n), n is the length of the string
    space: O(1)
    """
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if len(s) == 0 or (not s[0].isdigit() and s[0] != "+" and s[0] != "-") : return 0
        
        negative = True if s[0] == "-" else False
        start = 1 if not s[0].isdigit() else 0
        end = start
        while end < len(s) and s[end].isdigit():
            end += 1
        if end > start:
            ans = -1 * int(s[start:end]) if negative else int(s[start:end])
            if ans > 2**31 - 1:
                return 2**31 - 1
            elif ans < -1 * 2**31:
                return -1 * 2**31
            else:
                return ans
        else:
            return 0