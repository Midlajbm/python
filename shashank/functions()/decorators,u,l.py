def main():
    str=input("enter a string")
    return str
def outer(ptr):
    print("inside outer")
    def inner():
        print("entering inner")
        ptr1=ptr()
        str1=ptr1.upper()
        print(str1)
    return inner
ref=outer(main)
ref()




                
