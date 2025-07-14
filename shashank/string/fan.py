class fan:
    def __init__(self):
        self.brand="USHA"
        self.color="white"
        self.cost=2000
        self.numOfBlades=3

    def on(self):
        print("fan is on")
    def rotate(self):
        print("fan is rotating")
    def off(self):
        print("fan is off")
f=fan()
print(f.brand,f.color,f.cost,f.numOfBlades)

f.off(),f.on(),f.off(),f.rotate()

class student:
    def __init__(self):
        self.name="ruman"
        self.age=22
        self.sex="trans"
    def job(self):
        print(self.name,("is a kundan"))

m=student()
print(m.name)
print(m.sex)
m.job()