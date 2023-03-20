class Solution:
    """
    method: expand from every center
    time: O(n^2)(best solution)
    space: O(1)
    """
    def longestPalindrome(self, s: str) -> str:
        def expand(s, l, r, leftmost, rightmost):
            while (l >= 0 and r < len(s)) and (s[l] == s[r]):
                l -= 1
                r += 1
            l += 1
            r -= 1
            if r-l > rightmost-leftmost: return l, r
            else: return leftmost, rightmost
        leftmost = 0
        rightmost = 0
        for i in range(len(s)-1):
            leftmost, rightmost = expand(s, i, i, leftmost, rightmost)
            leftmost, rightmost = expand(s, i, i+1, leftmost, rightmost)
        return s[leftmost:rightmost+1]

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
