class p1:
    def __init__(self):
        self.__name=""
    @property
    def dataAccess(self):
        return self.__name
    @dataAccess.setter
    def dataAccess(self,value):
        self.__name=value
p1()
p1.dataAccess="vishnu"
res=p1.dataAccess
print(res)