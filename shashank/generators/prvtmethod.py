class bike:
    def __init__(self):
        self.brand="KTM"
    def __move(self):
        print("bike is moving")
    def helper(self):
        self.__move()

b1=bike()
b1.helper()