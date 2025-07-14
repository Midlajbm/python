# creation of object & edit & delete
class employee:
    def __init__(self):
        self.name="rumaan"
        self.age=25
        self.gf="nil"
    def vehicle(self):
        print("rumaan has white access 125")

e1=employee()
print(e1.name)
print(e1.age)
print(e1.gf)

e1.vehicle()
e1.numOfGirls=17
print(e1.numOfGirls)

e1.wife="ramya"
print(e1.wife)

del e1.age
