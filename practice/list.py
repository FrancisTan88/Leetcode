# # reverse range:
# string = "Francis"
# lst = [string[i] for i in range(len(string)-1, -1, -1)]
# # print(lst)

# # function zip:
# lst1 = [1,2,3]
# lst2 = [3,2,1]
# str1 = "abc"
# str2 = "cba"
# # for tuple in zip(str1, str2):
# #     print(tuple)
# # print(zip(lst1, lst2))
# # print(list(zip(lst1, lst2)))

# # add two lists:
# lst3 = [5,5,5]
# lst4 = [1,2,3]
# lst5 = [6,6,6]
# lst6 = [[1,2,3],[2,3,4]]
# print(lst3 + lst4)
# print(lst3 + lst6)
# lst3.append(lst5)
# print(lst3)

lst1 = [[1,2,3], [1,3,2]]
lst2 = [1,1,2]
lst3 = [1,2,1]
lst4 = [1,2,3]
print(lst2 == lst3)
print(lst4 in lst1)

nums = [1,2,3]
# print(nums.index(2))
# print(nums.index(3))

nums.pop(1)
print(nums)




