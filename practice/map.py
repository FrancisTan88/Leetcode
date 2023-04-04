# s = set()
# # t1 = (1,2,3)
# # t2 = (1,3,2)
# nums = [(1,2,3), (1,3,2)]
# for t in nums:
#     s.add(t)
# print(s)
# print(map(list, s))
# print(list(map(list, s)))


nums = [[1,2,3], [1,3,2]]
for t in range(len(nums)):
    for i in range(len(nums[t])):
        nums[t][i] = str(nums[t][i])
print(nums)

nums = [[(1,2), (2,3), (4,4)], [(1,3), (2,2), (5,6)]]
nums = [[tuple(map(str, t)) for t in lst] for lst in nums]
print(nums)

