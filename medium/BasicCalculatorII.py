class Solution:
    """
    (best solution)
    time: O(n), where n is the length of the given string
    space: O(n)
    """
    def calculate(self, s: str) -> int:
        n = len(s)
        num_stack = []
        curr_num = 0
        sign = "+"
        for i in range(n):
            if s[i].isdigit():
                curr_num = curr_num * 10 + int(s[i])
            if s[i] in "+-*/" or i == n-1:
                if sign == "+":
                    num_stack.append(curr_num)
                elif sign == "-":
                    num_stack.append(-curr_num)
                elif sign == "*":
                    num_stack.append(num_stack.pop() * curr_num)
                else:
                    num_stack.append(int(num_stack.pop() / curr_num))
                sign = s[i]
                curr_num = 0
        return sum(num_stack)   
