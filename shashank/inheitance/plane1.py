import time
class plane:
    def takeoff(slef):
        print("plae is ready to taek off")
    def fly(slef):
        print("plane is flying")
    def land(self):
        print("plane is landing")

class passenger(plane):
    def carry_p(self):
        print("plane carries passengers")
        time.sleep(2)
        print("____________________________")

class cargo(plane):
    def carry_g(self):
        print("cp carries goods")
        time.sleep(2)
        print("____________________________")

class fighter(plane):
     def carry_w(self):
        print("fp carries weapons")
        time.sleep(2)
        print("____________________________")

p1=passenger()
c1=cargo()
f1=fighter()

p1.takeoff()
p1.fly()
p1.land()
p1.carry_p()

c1.takeoff()
c1.fly()
c1.land()
c1.carry_g()

f1.takeoff()
f1.fly()
f1.land()
f1.carry_w()