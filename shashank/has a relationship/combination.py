class brain:
    def __init__(self):
        self.status="Active"
        print("brain is ready")

    def getbrain(self):
        print("brain is working")

class car:
    def __init__(self,name):
        self.cname=name
        

    def getcar(self):
        print("car is ready")
        
class person:
    def __init__(self,name):
        self.pname=name
        self.b=brain()
        self.c=""
        

    def hascar(self,p):
        self.c=p
        
c1=car("porsche")
p1=person("rumaan")

p1.hascar(c1)
print(p1.b.status)
print(p1.pname)

del c1
print(p1.name)