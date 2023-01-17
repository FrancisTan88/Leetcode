
class practice():
    # empty string is not iterable
    def empty_str():
        empty_str = ""
        for i in empty_str:
            print(i)
            print("Hi")
    
    # list itself is not empty although it only has an empty string
    def empty_str_lst():
        lst = [""]
        if lst:
            print("list is not empty")
        for s in lst:
            print(s)


# practice.empty_str()
practice.empty_str_lst()
