class person:
    def __init__(self):
        self.__name=""
    def getter(self):
        return self.__name
    def setter(self,name):
        self.__name=name
    getset=property(getter,setter)
p1=person()
p1.getset="vishnu"
res=p1.getset
print(res)
p1.getset="ravan"
res1=p1.getset

p1.getset="jojo"
re=p1.getset
print(re,res1)