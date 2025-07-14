# closure:0in a nested function calling inner function outside then outer function
# # using 2 function
# def outer():
#     a=10                #non local var
#     b=20                #non local var
#     print(a)
#     print(b)

#     def inner():
#         x=300           #non local var
#         y=400           #non local var
#         print(x)
#         print(y)
#     return inner
# ptr=outer()
# ptr()

# using three functions
def outer():
    print("inside outer")
    def inner():
        print("inside inner")
        def innerlast():
            print("inside innerlast")
        return innerlast
    ref=inner()
    ref()
    return inner
ref1=outer()
ref1()

