import time
class plane:
    def takeoff(slef):
        print("plae is ready to taek off")
    def fly(slef):
        print("plane is flying")
    def land(self):
        print("plane is landing")

class passenger(plane):
    def carry(self):
        print("plane carries passengers")
        time.sleep(2)
        print("____________________________")

class cargo(plane):
    def carry(self):
        print("cp carries goods")
        time.sleep(2)
        print("____________________________")

class fighter(plane):
     def carry(self):
        print("fp carries weapons")
        time.sleep(2)
        print("____________________________")

p1=passenger()
c1=cargo()
f1=fighter()


def allowplane(ref):
    ref.takeoff()
    ref.fly()
    ref.land()
    ref.carry()

allowplane(p1)
allowplane(c1)
allowplane(f1)
