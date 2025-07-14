a=10
def ex():
    global a
    a=100
    v=400
    print(a)
    print(v)
def ex1():
    global a
    b=80
    print(a)
    print(b)
print(a)
ex()
print(a)
ex1()
print(a)