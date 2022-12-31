from typing import List

class Solution:
    '''
    time: O(n)
    space: O(n)
    '''
    def plusOne(self, digits: List[int]) -> List[int]:
        result = "".join(list(map(str, digits)))
        result = int(result)+1
        return [int(i) for i in str(result)]

    """
    Time complexity: O(N), given that N is the length of the list
    Space complexity: O(1)
    """
    def plusOne(self, digits: List[int]) -> List[int]:
        ind = len(digits)-1
        while ind >= 0:
            if digits[ind] < 9:
                digits[ind] += 1
                return digits
            digits[ind] = 0
            ind -= 1
        return [1] + digits 