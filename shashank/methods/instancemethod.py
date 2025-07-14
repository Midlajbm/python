# no parameter with no return value
# class calci:
#     def __init__(self):
#         self.brand="casio"
#         self.price=1500
#     def add(self):
#         a=10
#         b=20
#         c=a+b
#         print(c)
# c1=calci()
# print(c1.brand)
# print(c1.price)
# c1.add()

# #no parameter with return value
# class car:
#     def __init__(self):
#         self.brand='nissan'
#         self.model="patrol"
#         self.engine='v8'
#     def mileage(self):
        
#         petrol=5
#         diesel=6
#         a=petrol
#         b=diesel
#         c=a+b
#         return c
# c1=car()
# print(c1.brand)
# print(c1.model)
# print(c1.engine)
# res=c1.mileage() 
# print(res)

# with parameter with no return value

# class calci:
#     def __init__(self):
#         self.brand="casio"
#         self.cost=1500
#     def add(self,a,b):
#         c=a+b
#         print(c)
# c1=calci()
# print(c1.brand)
# print(c1.cost)
# x=10
# y=20
# c1.add(x,y)

# with parameter with return value

class calci:
    def __init__(self):
        self.brand="casio"
        self.cost=1500
    def add(self,a,b):
        c=a+b
        print(c)
        return c
c1=calci()
print(c1.brand)
print(c1.cost)
x=10
y=20
res=c1.add(x,y)
print(res)