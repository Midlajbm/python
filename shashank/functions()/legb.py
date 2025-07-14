# legb rule
# a=10               #global scope
# def outer():
#     a=15            #enclosed scope
#     def inner():
#         a=20         #local scope
#         print(a)
#     inner()
# outer()


# built in scope which is already built or available in the system or software
from math import pi
#pi=10               #global scope
def outer():
    #pi=15            #enclosed scope
    def inner():
        #pi=20         #local scope
        print(pi)
    inner()
outer()