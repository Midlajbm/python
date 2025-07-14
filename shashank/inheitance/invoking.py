# invoking parent class during overridingdf
class a:
    def disp(self):
        print("a")

class b(a):
    def disp(self):
        print("b")

class c(b):
    def disp(self):
        print("c")
        a.disp(self)
        b.disp(self)

c1=c()
c1.disp()