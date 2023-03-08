from collections import defaultdict

# d = defaultdict(list)
# prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# for i in prerequisites:
#     d[i[1]].append(i[0])
# if 0 in d:
#     print("f")
# # print(d)

d = defaultdict(int)
lst = [1,2,3]
for i in lst:
    d[i] += 1
print(d)

all()