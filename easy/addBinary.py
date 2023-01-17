class Solution:
    """
    Method: Using the properties of Arithmetic: %, //
    Time complexity: O(n)
    Space complexity: O(1)
    """
    def addBinary(self, a: str, b: str) -> str:
        idx1 = len(a)-1
        idx2 = len(b)-1
        carry = False
        ans = ""
        while idx1 >= 0 or idx2 >= 0:
            if idx1 >= 0 and idx2 >= 0:
                curr = int(a[idx1]) + int(b[idx2]) + carry
                idx1 -= 1
                idx2 -= 1
            elif idx1 >= 0:
                curr = int(a[idx1]) + carry
                idx1 -= 1
            else:
                curr = int(b[idx2]) + carry
                idx2 -= 1
            ans = str((curr % 2)) + ans
            carry = True if curr >= 2 else False
        return "1" + ans if carry else ans