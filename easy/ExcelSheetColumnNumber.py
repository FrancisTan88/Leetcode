class Solution:
    '''
    time: O(n)
    space: O(1), given the number of alphabet is fixed at 26
    '''
    def titleToNumber(self, columnTitle: str) -> int:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        hashmap = {letter: idx+1 for idx, letter in enumerate(alphabet)}
        n = 0
        ans = 0
        for i in range(len(columnTitle)-1, -1, -1):
            ans += 26**n * hashmap[columnTitle[i]]
            n += 1
        return ans