# def outer():
#     a=10
#     b=20
#     print(a)
#     print(b)
#     def inner():
#         nonlocal a
#         a=100
#         b=200
#         print(a)
#         print(b)
#     print(a)
#     inner()
#     print(a)
# outer()

# def outer():
#     a=10
#     b=20
#     print(a)
#     print(b)
#     def inner():
#         c=200
#         print(a)
#         print(c)
#     inner()
# outer()

# LEGB RULE
def outer():
    a=10
    b=20
    print(a)
    print(b)
    print(c)
    def inner():
        c=100
        print(c)
    inner()
outer()