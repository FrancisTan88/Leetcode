from typing import List

class Solution:
    """
    time: O(2^2n), given that there are two choices for each single bracket, that is, 
                    the recursive function will call itself twice for each single bracket. 
                        Either it goes left and try to add a left bracket, or it goes right and try to add a right bracket,
                            and there are 2n single brackets in total.
    space: O(2^2n), which is the space for the system stack, just like the analysis above.
    """
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, ans, curr):
            if left < 0:
                return ans
            if not left and not right:
                ans.append(curr)
                return ans
            ans = dfs(left-1, right, ans, curr+"(")
            
            if left < right:
                ans = dfs(left, right-1, ans, curr+")")
            return ans
        return dfs(n, n, [], "")