class person:
    def __init__(self):
        self.__name=""
    def setter(self,value):
        self.__name=value
    def getter(self):
        return self.__name
p1=person()
p1.setter("vishnu")
re=p1.getter()
print(re)