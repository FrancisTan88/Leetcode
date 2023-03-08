class Solution:
    """
    time: O(n^2)
    space: O(1)
    """

    def longestPalindrome(self, s: str) -> str:
        def expand(s, idx, one):
            if one:
                l = idx - 1
                r = idx + 1
            else:
                l = idx - 1
                r = idx + 2
            while l >= 0 and r < len(s):
                if s[l] == s[r]:
                    l -= 1
                    r += 1
                else:
                    break
            l += 1
            r -= 1
            return l, r

        def maintain(l, r, s, e):
            if (r - l) > (e - s):
                s = l
                e = r
            return s, e

        idx, start, end = 0, 0, 0
        while idx < len(s):
            l, r = expand(s, idx, True)
            start, end = maintain(l, r, start, end)
            if idx + 1 < len(s) and s[idx] == s[idx+1]:
                l, r = expand(s, idx, False)
                start, end = maintain(l, r, start, end)
            idx += 1
        return s[start:end+1]

    """
    dp
    time: O(n^2)
    space: O(n^2)
    """

    def longestPalindrome(self, s: str) -> str:
        dp = [[False] * len(s) for i in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        leftmost, rightmost = 0, 0
        for end in range(len(s)):
            for start in range(end-1, -1, -1):
                if s[start] == s[end]:
                    if (end - start == 1) or (dp[start+1][end-1] == True):
                        dp[start][end] = True
                        if (end - start) > (rightmost - leftmost):
                            leftmost = start
                            rightmost = end
        return s[leftmost:rightmost+1]
