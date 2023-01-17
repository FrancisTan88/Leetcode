


"""
practice for string-related function
"""
class practice():
    def __init__(self, s) -> None:
        self.string = s

    def lower_case(self):
        print(self.string.lower())
    
    def check(self):
        print(self.string.isalnum())


trans = practice("ABC123abc!")
trans.lower_case()
trans.check()




