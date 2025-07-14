#alpabets,digits,alpha/digits
str=input("enter a string ")
print(str)
if str.isalpha():
    print("str contains alpha")
elif str.isdigit():
    print("str contains only digits")
elif str.isalnum():
    print("str contains alpha & digits")
else:
    print("it contains speacial characters")