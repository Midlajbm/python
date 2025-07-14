class farmer:
    def __init__(self,name,p,t,r):
        self.name=name
        self.principle=p

        self.time=t
        self.rate=r
    def loan(self):
        si=(self.principle*self.time*self.rate)/100
        return si
        
f1=farmer("raamu",500000,5,2.5)
f2=farmer("rooma",300000,7,2.5)

print(f1.name)
res=f1.loan()
print(res)

print(f2.name)
res=f2.loan()
print(res)