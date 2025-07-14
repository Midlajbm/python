# to connect the classes
# class parent:
#     def __init__(self):
#         self.a=10
# class child(parent):
#      def __init__(self):
#         parent.__init__(self)           # to connect the classes [parentclassname.__init__(self)]
#         self.b=20
# c1=child()
# print(c1.b)
# print(c1.a)



# 2 child
class a:
    def __init__(self):
        self.a=10

        
class b(a):
    def __init__(self):
        
        self.b=20
        a.__init__(self)

class c(b):
    def __init__(self):
        b.__init__(self)
        self.c=30
c1=c()
print(c1.c)
print(c1.b)
print(c1.a)