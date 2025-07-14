class demo:
    def display(self,x=10,y=20,z=30):
        print(x)
        print(y)
        print(z)
d1=demo()
a=11
b=22
c=33
# d1.display()
# d1.display(a,b,c)
# d1.display(a)
d1.display(x=b,y=c,z=a)