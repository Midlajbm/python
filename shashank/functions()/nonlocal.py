# non local variable
def outer():
    a=10                #non local var
    b=20                #non local var
    print(a)
    print(b)

    def inner():
        x=300           #non local var
        y=400           #non local var
        print(x)
        print(y)

        def middle():
            u=88        #local var  :- the inner most variable is local variable
            m=90        #local var
            print(u)
            print(m)
        middle()
    inner()
outer()