from typing import List

class Solution:
    """
    method: dfs(backtracking) and use DP to accelerate "palindrome check"
    time: 
    space: 
    """
    def partition(self, s: str) -> List[List[str]]:  
        # O(2^n)
        def dfs(s, curr, ans, start, dp):
            if start >= len(s):
                ans.append(curr)
                return ans
            for end in range(start, len(s)):
                if dp[start][end]:  # O(1)
                    ans = dfs(s, curr + [s[start:end+1]], ans, end+1, dp)
            return ans
        n = len(s)
        dp = [[False] * n for i in range(n)]  # costs n^2 space
        # O(n)
        for i in range(n):
            dp[i][i] = True
        # O(n^2)
        for end in range(1, n):
            for start in range(end-1, -1, -1):
                if s[start] == s[end]:
                    if dp[start+1][end-1] or start == end-1:
                        dp[start][end] = True
        return dfs(s, [], [], 0, dp)