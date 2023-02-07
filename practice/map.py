s = set()
# t1 = (1,2,3)
# t2 = (1,3,2)
nums = [(1,2,3), (1,3,2)]
for t in nums:
    s.add(t)
print(s)
print(map(list, s))
print(list(map(list, s)))
