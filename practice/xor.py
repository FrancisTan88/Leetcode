"""
XOR: 邏輯互斥
"""

# a = True
# b = False
# print(a^b)

# a = True
# b = True
# print(a^b)

# a = 100
# b = 100
# print(a^b)

# a = 100
# b = 0
# print(a^b)

# a = 0
# b = 0
# print(a^b)

lst = [1,1,2,3,3]
tmp = 0
for i in lst:
    tmp ^= i
    print(tmp)
