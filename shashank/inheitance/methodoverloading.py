# method overloading will not support python
class a:
    def disp(self,a):
        print(a)
class b(a):
    def disp(self,a,b):
        print(a)
        print(b)

        
class c(b):
    def disp(self,a,b,c):
        print(a)
        print(b)
        print(c)

c1=c()
c1.disp(10,20,30)
c1.disp(10,20)
c1.disp(10)      