class os:
    def __init__(self):
        self.status=True
        print("os is ready")

    def getos(self):
        print("os is installing ")
class mobile:
    def __init__(self,name):
        self.mname=name
        self.o=os()
        print("mobile is ready")
        print("with os installing")

m1=mobile("vivo")
print(m1.mname)
print(m1.o.status)
m1.o.getos()
del m1
print(m1.o.status)
# del m1
# print(m1.o.status)  it is used to prove that composed method cannot work without main class