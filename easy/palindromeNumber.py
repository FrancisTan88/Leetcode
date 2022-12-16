class Solution:
    """
    Naive method: using two lists to store string forward and backward
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        ori_lst = [c for c in x]
        rev_lst = [x[i] for i in range(len(x)-1, -1, -1)]
        for i in range(len(ori_lst)):
            if ori_lst[i] != rev_lst[i]:
                return False
        return True

    """
    Naive method: using two inverse indexes to compare forward and backward 
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        start = 0
        end = len(x)-1
        while start < end:
            if x[start] != x[end]:
                return False
            start += 1
            end -= 1
        return True

    """
    TODO
    Advanced method: Math algorithm
    Time complexity: O(log(n))
    Space complexity: O(1)
    """
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if x >= 0 and x < 10:
            return True
        if x % 10 == 0:
            return False
        
        current = 0
        reverse = 0
        while reverse < x:
            current = x % 10
            reverse = reverse * 10 + current
            x = int(x/10)
        if reverse == x or int(reverse/10) == x:
            return True
        return False
            




