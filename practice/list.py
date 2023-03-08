import numpy as np

# lst = [[], []]
# lst = [None, None, None]
# print(any(lst))


# lst = [1,2,3]
# t = (4,5,6)
# d = {7,8,9}
# lst += t
# print(lst)
# lst += d
# print(lst)

lst = [[1,2,3], [1,2,3,4], [1,2]]
print(max(lst, key=lambda x: len(x)))
