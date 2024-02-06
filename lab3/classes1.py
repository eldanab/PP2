class Strings:
    def __init__(self, str_p = ""):
        self.str = str_p
    def getString(self):
        self.str = input()
    def printString(self):
        print(self.str.upper())
str1 = Strings()
str1.getString()
str1.printString()