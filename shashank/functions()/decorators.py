def main():
    print("inside main")

def outer(ptr):
    print("inside outer")

    def inner():
        print("entering inner")
        ptr1=ptr
        ptr1()
        print("leaving inner")
    return inner
ref=outer(main)          #main as parameter
ref()


