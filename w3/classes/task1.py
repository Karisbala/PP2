class String():
    def __init__(self):
        self.s = ''
    
    def getString(self):
        self.s = input()
    
    def printString(self):
        print(self.s.upper())

s = String()

s.getString()
s.printString()