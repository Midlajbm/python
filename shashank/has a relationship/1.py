class radio:
    def turnOn(self,x):
        if x==1:
            print("the radio is on ")
        else:
            print("the radio is off")
class car:
    def __init__(self,max,min):
        self.cmax=max
        self.cmin=min
        self.r=radio()

c1=car(180,30)
print(c1.cmax)
print(c1.cmin)
c1.r.turnOn(1)
c1.r.turnOn(0)
