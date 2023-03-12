"""
This is to prove that the object returned by function in Python 
    is the same object that we pass as parameter into it.
        In other words, function does not allocate extra memory space to do the jobs.
"""
def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end]= nums[end], nums[start]
        start += 1
        end -= 1
    return nums

lst = [1,2,3,4,5,6,7]
print(hex(id(lst)))
print(hex(id(reverse(lst, 0, len(lst)-1))))

