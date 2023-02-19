class Solution:
    '''
    time: O(2^n), given that the length of "said string" is at most two times itself for each function "say" called,
                    so in the worst case, the time complexity would be 
                        O(Sn) = O(S + 2S + 4S + ... + 2(n-2)S) 
                        = O(S(1 - 2^(n-1)) / (1 - 2))
                        = O(S(2^(n-1) - 1)) = O(2^n), consider that S=1  
    space: given that the longest "ans" would be the last term of the series above, i.e. 2(n-2)S, in the worst case.
            So, the space complexity would be O(n), consider that S=1
    '''
    def countAndSay(self, n: int) -> str:
        def say(string):
            ans = ""
            idx = 0
            count = 0
            curr = string[0]
            while idx < len(string):
                if string[idx] != curr:
                    ans += str(count)
                    ans += curr
                    curr = string[idx]
                    count = 1
                else:
                    count += 1
                idx += 1
            ans += str(count)
            ans += curr       
            return ans    
        ans = "1"
        if n == 1: return ans
        for i in range(n-1):
            ans = say(ans)
        return ans