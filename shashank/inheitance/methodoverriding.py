# method overriding will suppot python
class a:
    def disp(self):
        print("a")

class b(a):
    def disp(self):
        print("b")

class c(b):
    def disp(self):
        print("c")

c1=c()
c1.disp()

c1.disp()

c1.disp()