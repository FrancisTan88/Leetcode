def recursion(lst, num, end, validation):
    if num > end:
        return lst
    lst.append(num)
    validation.append(num)
    num += 1
    lst = recursion(lst, num, end, validation)
    print(validation)
    return lst

recursion([], 1, 8, [])