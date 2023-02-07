class Solution:
    '''
    time: O(n)
    space: O(n)
    '''
    def reverseBits(self, n: int) -> int:
        inp = bin(n)[2:]
        inp = '0'*(32-len(inp)) + inp
        inp = inp[::-1]
        return int(inp, 2)