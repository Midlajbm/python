import time
class  charger:
    def __init__(self,name):
        self.cname=name
    def getcharger(self):
        print("charger is ready")

class mobile:
    def __init__(self,name):
        self.mname=name
        self.c=""
    def hasmobile(self,p):
        self.c=p
m1=mobile("vivo")
c1=charger("fastcharger")
m1.hasmobile(c1)
print(m1.mname)
print(m1.c.cname)
m1.c.getcharger()
time.sleep(2)
print("______________________")
del m1
print(c1.cname)
c1.getcharger()
time.sleep(2)
print("______________________")
print(m1.mname)
